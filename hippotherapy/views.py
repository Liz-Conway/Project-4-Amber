from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from hippotherapy.forms import ClientForm, SessionForm, ObservationForm
from hippotherapy.models import Hat, Client, Course, Session, Function, Skill,\
    Hint, SkillScore
from django.db.models.aggregates import Max
from _datetime import date
from django.db.models.expressions import F
from administration.models import Horse, Task, Diagnosis
from django.http import response

# Create your views here.
class HomePage(TemplateView):
    template_name = "hippo/index.html"


class AddClient(TemplateView):
    template_name = "hippo/addClient.html"
    form_class = ClientForm
    
    
    """
    In class-based views:
    Instead of using an if statement to check the request method,  
    we simply create class methods called GET, POST, or any other HTTP verb.
    """
    def get(self, request, *args, **kwargs):
        """
        '*args' = Standard arguments parameter
        '**kwargs' = Standard keyword arguments parameter
        """
        form = ClientForm()
        hat_sizes = Hat.objects.all()
        diagnoses = Diagnosis.objects.all()
        
        return render(
            request, 
            self.template_name, # view to render
            # Context - passed into the HTML template
            {
                "form": form, 
                "hat_sizes": hat_sizes,
                "diagnoses": diagnoses,
            }
        )
        
    """
    In class based views -
    GET & POST are supplied as class methods
    """
    def post(self, request, *args, **kwargs):
        """
        '*args' = Standard arguments parameter
        '**kwargs' = Standard keyword arguments parameter
        """
            
        """
        Get the data from our form
        and assign it to a variable.
        Gets all of the data that we posted from our form
        """
        add_client_form = ClientForm(data=request.POST)
        
        """
        Form is valid => If all the fields have been completed
        """
        if add_client_form.is_valid():
            saved_client = add_client_form.save()
            save_diagnoses(saved_client.id, request.POST)
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            messages.success(request,
                             f'New client <span class="name">{first_name} {last_name}</span> added successfully.',
                             extra_tags='safe')
        else:
            """
            If the form is NOT valid  
            then return an  empty 'add client' form instance
            showing the errors
            """
            messages.error(request, 'Invalid form submission.')
            messages.error(request, add_client_form.errors)

        """
        Send all of this information to our render method
        """
        return render(
            request, 
            'addClient.html', # View to render
            # Context - passed into the HTML template
            { 
                'form': ClientForm(request.GET)
            }
        )
        

def get_course_for_client(client_id):
    courses = Course.objects.filter(client=client_id)
    
    if courses.count() == 0:
        # First course for this client
        # Retrieve an instance of the client
        client = Client.objects.filter(id=client_id)[0]
        # Create a new course for this client
        last_course = Course(client=client)
        # Save the course to the database
        last_course.save()
    elif courses.count() == 1:
        # Use this course
        last_course = courses[0]
    else:
        # Find the course with the latest Session date
        # course = Course.objects.filter(client=client).select_related('Session').filter('course__client'==client_id, Max('session__session_date'))[0]
        # Find the courses for this client
        courses = Course.objects.filter(client=client_id)
        # Create an array with the course ids
        course_ids = []
        for course in courses:
            course_id = course.id
            course_ids.append(course_id)
        # Find the latest date for any session for these courses
        last_session_date = Session.objects.filter(course__in=course_ids).aggregate(max_date=Max('session_date'))[0]
        
        # Find the session with the latest date for any courses for this client
        last_session = Session.objects.filter(session_date=last_session_date)[0]
        
        last_course = last_session.course
        
    
    return last_course


def get_next_session_week(course):
    
    # queryset = Course.objects.filter(id=course.id).select_related('Session').aggregate(Max('session__week_number'))
    # last_week = Course.objects.filter(id=course.id).annotate(Max('session_course__week_number'))
    # last_week = Course.objects.filter(id=course.id).all().annotate(max_week=F('session_course__week_number'))
    sessions = Session.objects.filter(course=course.id)
    # Entire object -> 'None' if nothing matches
    # sessions = Session.objects.filter(course=course.id).order_by('week_number').last() # Entire session object

    if sessions.count() > 0:
        # Already have some sessions for this course
        last_week = sessions.aggregate(Max('week_number'))
        next_session_week = last_week['week_number__max'] + 1
    else:
        # No Sessions for this Course yet
        next_session_week = 1 
    
    return next_session_week


def save_tasks(session_id, post):
    total_tasks = Task.objects.count()
    
    session_query = Session.objects.filter(id=session_id)
    session = get_object_or_404(session_query)
    
    for i in range(1, total_tasks + 1):
        task_identifier = f"task_{i}"

        if post.get(task_identifier) != None:
            task_query = Task.objects.filter(id=i)
            task = get_object_or_404(task_query)

            session.tasks.add(task)
        

def save_diagnoses(client_id, post):
    print("post")
    print(post)
    total_diagnoses = Diagnosis.objects.count()
    
    client = Client.objects.get(id=client_id)
    
    for i in range(1, total_diagnoses + 1):
        diagnosis_identifier = f"diagnosis_{i}"
        if post.get(diagnosis_identifier) != None:
            diagnosis = Diagnosis.objects.get(id=i)
            client.diagnosis.add(diagnosis)


class RecordSession(TemplateView):
    template_name = "hippo/recordSession.html"
    form_class = SessionForm
    
    
    """
    In class-based views:
    Instead of using an if statement to check the request method,  
    we simply create class methods called GET, POST, or any other HTTP verb.
    """
    def get(self, request, *args, **kwargs):
        """
        '*args' = Standard arguments parameter
        '**kwargs' = Standard keyword arguments parameter
        """
        form = SessionForm()
        horsies = Horse.objects.all()
        unmounted_tasks = Task.objects.filter(mounted=False)
        mounted_tasks = Task.objects.filter(mounted=True)
        
        # Get the client id that was passed in the URL
        client_id = kwargs['client']
        client_query = Client.objects.filter(id=client_id)
        client = get_object_or_404(client_query)
        course = get_course_for_client(client.id)
        
        # Create a new session for this course
        session_week = get_next_session_week(course)
        
        session_number = f'{course.id}/{session_week}'
        
        # Get the client name
        client_name = f'{client.first_name} {client.last_name}'
        
        # Get today's date - this will be the default date for the session
        session_date = date.today()
        # https://stackabuse.com/how-to-format-dates-in-python/
        session_date_string = session_date.strftime('%d-%m-%Y')
        
        return render(
            request, 
            self.template_name, # view to render
            # Context - passed into the HTML template
            {
                "form": form, 
                "course_number": course.id,
                "session_week": session_week,
                "client": client_name,
                "session_date": session_date,
                "session_date_string": session_date_string,
                "horsies": horsies,
                "unmounted": unmounted_tasks,
                "mounted": mounted_tasks,
            }
        )
        
    """
    In class based views -
    GET & POST are supplied as class methods
    """
    def post(self, request, client, *args, **kwargs):
        """
        '*args' = Standard arguments parameter
        '**kwargs' = Standard keyword arguments parameter
        """
        """
        Get the data from our form
        and assign it to a variable.
        Gets all of the data that we posted from our form
        """
        record_session_form = SessionForm(data=request.POST)
        
        """
        Form is valid => If all the fields have been completed
        """
        if record_session_form.is_valid():
            form_saved = record_session_form.save()
            save_tasks(form_saved.id, request.POST)
            course_number = request.POST['course']
            week_number = request.POST['week_number']
            messages.success(request,
                             f'New session for Session# <span class="boldEntry">{course_number} / {week_number}</span> added successfully.',
                             extra_tags='safe')

            # Redirect to the 'observeSession' page after adding a new Session
            # Works by going to the URL paths defined in 'urls.py'
            # Finds the method whose 3rd ('name=') parameter is the String passed into redirect
            # https://www.tutorialspoint.com/django/django_page_redirection.htm
            return redirect(
                "observeSession",               # view to render
                session=form_saved.id  # parameter to pass to URL
            )

        else:
            """
            If the form is NOT valid  
            then return an  empty 'record session' form instance
            showing the errors
            """
            messages.error(request, 'Invalid form submission.')
            messages.error(request, record_session_form.errors)

            """
            Postback to the recordSession page when the form is not valid
            """
            # https://www.tutorialspoint.com/django/django_page_redirection.htm
            return redirect(
                'recordSession',       # view to render
                client=client   # parameter to pass to URL
            )

        

class SelectClient(TemplateView):
    template_name = "hippo/selectClient.html"
    
    """
    In class-based views:
    Instead of using an if statement to check the request method,  
    we simply create class methods called GET, POST, or any other HTTP verb.
    """
    def get(self, request, target, *args, **kwargs):
        """
        '*args' = Standard arguments parameter
        '**kwargs' = Standard keyword arguments parameter
        """
        clients = Client.objects.all()
        
        return render(
            request, 
            self.template_name, # view to render
            # Context - passed into the HTML template
            {
                "clients": clients,
                "target": target, 
            }
        )
        
    """
    In class based views -
    GET & POST are supplied as class methods
    """
    def post(self, request, *args, **kwargs):
        """
        '*args' = Standard arguments parameter
        '**kwargs' = Standard keyword arguments parameter
        """
            
        """
        Get the data from our form
        and assign it to a variable.
        """
        client = request.POST['client']
        page_url = request.POST['targetPage']
        
        # https://www.tutorialspoint.com/django/django_page_redirection.htm
        return redirect(
            page_url,       # view to render
            client=client   # parameter to pass to URL
        )

class ObserveSession(TemplateView):
    template_name = "hippo/observeSession.html"

    """
    In class-based views:
    Instead of using an if statement to check the request method,  
    we simply create class methods called GET, POST, or any other HTTP verb.
    """
    def get(self, request, *args, **kwargs):
        """
        '*args' = Standard arguments parameter
        '**kwargs' = Standard keyword arguments parameter
        """
        form = ObservationForm()
        
        # Get the session id that was passed in the URL
        session_id = kwargs['session']
        session_query = Session.objects.filter(id=session_id)
        session = get_object_or_404(session_query)
        course = session.course
        client = course.client
        functions = Function.objects.all()
        skills = Skill.objects.all()
        hints = Hint.objects.all()
        
        return render(
            request, 
            self.template_name, # view to render
            # Context - passed into the HTML template
            {
                "session": session,
                "functions": functions,
                "skills": skills,
                "hints": hints,
                "client": client,
                "score_range": range(1, 6),
            }
        )
        
    """
    In class based views -
    GET & POST are supplied as class methods
    """
    def post(self, request, *args, **kwargs):
        """
        '*args' = Standard arguments parameter
        '**kwargs' = Standard keyword arguments parameter
        """
        """
        Get the data from our form
        and assign it to a variable.
        Gets all of the data that we posted from our form
        """
        observation_data=request.POST
        session_id = kwargs['session']
        
        for observation in observation_data:
            # First post data is the CSRF token - So skip this data point
            if observation.startswith('csrf'):
                continue
            
            # observation will be of the form 'scoreX' or scoreXX' where X is a digit
            # Splitting the string leaves a blank character as the first element
            # of the returned array, so take the element at index 1 and convert to an int
            # This gives the id of the skill associated with this score
            skill_id = int(observation.split('score')[1])
            score = observation_data[observation]
            
            # Get the skill object for this skill ID
            skill_query = Skill.objects.filter(id=skill_id)
            skill = get_object_or_404(skill_query)
            # Get the session object for the session ID passed into the post method
            session_query = Session.objects.filter(id=session_id)
            session = get_object_or_404(session_query)
            
            # Create a SkillScore object for this Skill, during this Session
            # having the observed score
            skill_score = SkillScore(session=session, skill=skill, score=score)
            # Save the SkillScore object to the 'through' table
            skill_score.save()
        
        return redirect('viewPostedSession', session=session_id)


class ChooseSession(TemplateView):
    template_name = "hippo/chooseSession.html"
    
    
    """
    In class-based views:
    Instead of using an if statement to check the request method,  
    we simply create class methods called GET, POST, or any other HTTP verb.
    """
    def get(self, request, *args, **kwargs):
        """
        '*args' = Standard arguments parameter
        '**kwargs' = Standard keyword arguments parameter
        """
        
        # Get the client id that was passed in the URL
        client_id = kwargs['client']
        client_query = Client.objects.filter(id=client_id)
        client = get_object_or_404(client_query)
        
        # Get all sessions for this client
        sessions = Session.objects.filter(course__client=client)
        # sessions = get_object_or_404(sessions_query)
        for session in sessions:
            print(session)
            print(session.session_date)
            print()
        
        # Get the client name
        client_name = f'{client.first_name} {client.last_name}'
        
        return render(
            request, 
            self.template_name, # view to render
            # Context - passed into the HTML template
            {
                "client": client_name,
                "sessions": sessions,
            }
        )
        

        
class ViewSession(TemplateView):
    template_name = "hippo/viewSession.html"

    """
    In class-based views:
    Instead of using an if statement to check the request method,  
    we simply create class methods called GET, POST, or any other HTTP verb.
    """
    def get(self, request, *args, **kwargs):
        """
        '*args' = Standard arguments parameter
        '**kwargs' = Standard keyword arguments parameter
        """
        # Get the session id that was passed in the URL
        session_id = kwargs['session']
        """
        Get the Scores for the chosen session
        """
        session_scores = SkillScore.objects.filter(session_id__id=session_id)
        
        """
        Get the Tasks for the chosen session
        """
        tasks = Task.objects.filter(performed__id=session_id).order_by('-mounted')
        
        return render(
            request, 
            self.template_name, # view to render
            # Context - passed into the HTML template
            {
                "scores": session_scores,
                "tasks" : tasks,
            }
        )
        
    """
    In class based views -
    GET & POST are supplied as class methods
    """
    def post(self, request, *args, **kwargs):
        """
        '*args' = Standard arguments parameter
        '**kwargs' = Standard keyword arguments parameter
        """
        """
        Get the data from our form
        and assign it to a variable.
        Gets all of the data that we posted from our form
        """
        session_id = request.POST['chosenSession']
        
        """
        Get the Scores for the chosen session
        """
        session_scores = SkillScore.objects.filter(session_id__id=session_id)
        
        """
        Get the Tasks for the chosen session
        """
        tasks = Task.objects.filter(performed__id=session_id).order_by('-mounted')
        
        return render(
            request, 
            self.template_name, # view to render
            # Context - passed into the HTML template
            {
                "scores": session_scores,
                "tasks" : tasks,
            }
        )
