from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from hippotherapy.forms import ClientForm, SessionForm, ObservationForm
from hippotherapy.models import Hat, Client, Course, Session, Function, Skill,\
    Hint, SkillScore
from django.db.models.aggregates import Max, Sum, Count, Min
from _datetime import date
from django.db.models.expressions import F
from administration.models import Horse, Task, Diagnosis
from django.http import response
import json
import datetime
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from hippotherapy.hippotherapy_utils import get_course_for_client,\
    get_next_session_week, save_tasks, save_diagnoses,\
    get_scored_courses_for_client, convert_observations

# Create your views here.
class HomePage(TemplateView):
    template_name = "index.html"


class AddClient(TemplateView):
    template_name = 'hippo/addClient.html'
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
        add_user_form = ClientForm(data=request.POST)
        
        """
        Form is valid => If all the fields have been completed
        """
        if add_user_form.is_valid():
            saved_client = add_user_form.save()
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
            messages.error(request, '<span class="boldEntry">Invalid form submission.</span>', extra_tags='safe')
            messages.error(request, add_user_form.errors)

        hat_sizes = Hat.objects.all()
        diagnoses = Diagnosis.objects.all()
        """
        Send all of this information to our render method
        """
        # https://stackoverflow.com/questions/6318074/django-bypass-form-validation
        # Bypass Django validating the date field even though it never was asked to
        # To add insult to injury, Django then informs that a valid date is not valid
        initial = dict(map(lambda x:(x[0], x[1][0]), dict(request.GET).items()))
        return render(
            request, 
            self.template_name, # View to render
            # Context - passed into the HTML template
            { 
                'form': ClientForm(initial=initial),
                'hat_sizes': hat_sizes,
                "diagnoses": diagnoses,
            }
        )


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
        
        session = Session(course=course, session_date=session_date, week_number=session_week)
        
        return render(
            request, 
            self.template_name, # view to render
            # Context - passed into the HTML template
            {
                "form": form, 
                "course_number": course.id,
                "session_week": session_week,
                "client": client_name,
                "session_date": session_date_string,
                "session_date_string": session_date_string,
                "horsies": horsies,
                "unmounted": unmounted_tasks,
                "mounted": mounted_tasks,
                "session": session,
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
        session_client = get_object_or_404(Client.objects.filter(id=client))
        
        """
        Form is valid => If all the fields have been completed
        """
        if record_session_form.is_valid():
            form_saved = record_session_form.save()
            save_tasks(form_saved.id, request.POST)
            course_number = request.POST['course']
            week_number = request.POST['week_number']
            messages.success(request,
                             f'New session for <span class="boldEntry">{session_client}</span> ({course_number}/{week_number}) added successfully.',
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
        last_session = None
        
        if page_url == 'generateChart':
            page_url = 'chooseCourse'
            
        elif page_url == 'recordSession':
            courses = Course.objects.filter(client=client)
            if courses.count() != 0:
                page_url = 'newCourse'
                # Get the latest sessions for any Courses taken by this client
                max_session_dates = Session.objects.filter(course__in=courses).values('course').annotate(max_date=Max('session_date')).order_by('-max_date', '-course')
                # Get the date of the last session taken by this client
                last_session_date = max_session_dates[0]
                # Get the sessions of the last Course taken by this client
                sesh = Session.objects.filter(session_date=last_session_date['max_date'], course=last_session_date['course']).order_by('-week_number')
                # Get the last session of the last Course taken by this client
                last_sesh = sesh[0]
                # Get the id of the last session of the last Course taken by this client 
                last_session = last_sesh.id
        
                # https://www.tutorialspoint.com/django/django_page_redirection.htm
                return redirect(
                    page_url,       # view to render
                    client=client,   # parameter to pass to URL
                    session=last_session,
                )
            else:
                # First Course for this client
                get_course_for_client(client, True)
                
        # https://www.tutorialspoint.com/django/django_page_redirection.htm
        return redirect(
            page_url,       # view to render
            client=client,   # parameter to pass to URL
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
        # form = ObservationForm()
        previous_observations =  request.session.get('observations', None)
        # Clear the session data
        request.session.flush()
        previous = None
        
        if previous_observations != None:
            previous = convert_observations(previous_observations)    
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
                "previous": previous,
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
        session_id = kwargs['session']
        observation_data=request.POST
        number_of_skills = Skill.objects.count()

        if len(observation_data) == number_of_skills + 1:
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
            
            course = get_object_or_404(Course.objects.filter(courses__id=session_id))
            course_id = course.id
            # return redirect('viewSession', session=session_id)
            return redirect('generateChart', course=course_id)
        
        else:
            request.session['observations'] = observation_data
            messages.error(request, 'You need to add a score on <span class="boldEntry">every</span> skill in <span class="boldEntry">all</span> functions', extra_tags='safe')
            return HttpResponseRedirect(reverse('observeSession', args=[session_id]))


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
        # Where the session has been scored
        sessions = Session.objects.filter(course__client=client).exclude(score_session = None)
        
        # Get the client name
        client_name = f'{client.first_name} {client.last_name}'
        
        return render(
            request, 
            self.template_name, # view to render
            # Context - passed into the HTML template
            {
                "client": client_name,
                "sessions": sessions,
                "client_id": client_id,
            }
        )


    """
    In class-based views:
    Instead of using an if statement to check the request method,  
    we simply create class methods called GET, POST, or any other HTTP verb.
    """
    def post(self, request, *args, **kwargs):
        """
        '*args' = Standard arguments parameter
        '**kwargs' = Standard keyword arguments parameter
        """
        client_id = request.POST['client']
        try:
            session_id = request.POST['chosenSession']
        except KeyError:
            messages.error(request, "You need to select one of the sessions before clicking the button")
            return HttpResponseRedirect(reverse('chooseSession', args=[client_id]))
        
        return HttpResponseRedirect(reverse('viewSession', args=[session_id]))
       
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
        session = get_object_or_404(Session.objects.filter(id=session_id))
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
                "session": session,
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
        session = get_object_or_404(Session.objects.filter(id=session_id))
        
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
                "session": session,
            }
        )
        
class ChartPage(TemplateView):
    template_name = "hippo/generateChart.html"

    """
    In class-based views:
    Instead of using an if statement to check the request method,  
    we simply create class methods called GET, POST, or any other HTTP verb.
    We will be showing the current score and the baseline score for each function
    in a chart.
    We need to retrieve Labels, current scores and baseline scores from the database.
    We also need to retrieve and calculate the maximum score for each Function.
    We then need to convert the actual scores to scores as a percentage of the total.
    We need to pass Labels, current scores and baseline scores to the chart page.
    """
    def get(self, request, *args, **kwargs):
        """
        '*args' = Standard arguments parameter
        '**kwargs' = Standard keyword arguments parameter
        """
        
        try:
            course_id = request.POST['course']
            print(f"POSTed course ID")
        except KeyError:
            # No Course was chosen - redisplay the page with an error message
            # Key Error - No 'course' in POST data
            try:
                course_id = kwargs['course']
            except:
                # Throw error -> 404 page
                pass
                
        client = get_object_or_404(Client.objects.filter(participates__id=course_id))
        
        # We need to find the latest week for a given course that has scores
        latest_week = Session.objects.filter(course=course_id).exclude(score_session=None).aggregate(Max('week_number'))['week_number__max']
        # Find the session for the last scoring week of a given course
        last_session = Session.objects.filter(course=course_id, week_number=latest_week)[0]
        latest_session = last_session.id
        # Find the scores for the last scoring week of a given course
        # Need to have .values() before .annotate() in order to perform GROUP BY
        scores_query = SkillScore.objects.values('skill__function__id').filter(session=latest_session).annotate(Sum('score')).order_by('skill__function_id')
        scores_list = [score_query.get('score__sum') for score_query in scores_query]
        
        # Find the number of skills in each Function
        total_query = Skill.objects.values('function__function_name').annotate(Count('function_id')).order_by('function_id')
        # Get the labels for the chart
        functions = json.dumps([ total['function__function_name'] for total in total_query])
        # Calculate the maximum score for each Function
        totals = [ total['function_id__count'] * 5 for total in total_query]
        # Calculate each score as a percentage of its total
        percent_scores = [ round(score * 100 / total) for score, total in zip(scores_list, totals)]
        # Format the percent scores to be sent to the chart
        scores = json.dumps(percent_scores)
        
        # We need to find the first week for a given course that has scores, in order to calculate a baseline
        first_week = Session.objects.filter(course=course_id).exclude(score_session=None).aggregate(Min('week_number'))['week_number__min']
        # Find the session for the first scoring week of a given course
        first_session = Session.objects.filter(course=course_id, week_number=first_week).values('id')[0]['id']
        # Find the scores for the last scoring week of a given course
        # Need to have .values() before .annotate() in order to perform GROUP BY
        baselines_query = SkillScore.objects.values('skill__function__id').filter(session=first_session).annotate(Sum('score')).order_by('skill__function_id')
        baseline_list = [baseline_query.get('score__sum') for baseline_query in baselines_query]
        # Calculate each baseline score as a percentage of its total
        percent_baselines = [ round(score * 100 / total) for score, total in zip(baseline_list, totals)]
           
        baselines = json.dumps(percent_baselines)
        
        # retrieve the course data stored in the Session
        course_info = get_scored_courses_for_client(client.id)
        
        return render(
            request, 
            self.template_name, # view to render
            # Context - passed into the HTML template
            {
                "client": client,
                "functions": functions,
                "scores": scores,
                "baselines": baselines,
                "scored_courses": course_info,
                "session": last_session,
            }
        )
        

class ChooseCourse(TemplateView):
    template_name = "hippo/chooseCourse.html"
    
    
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
        
        # Get all courses for this client
        courses = get_scored_courses_for_client(client_id)
        
        return render(
            request, 
            self.template_name, # view to render
            # Context - passed into the HTML template
            {
                "client": client,
                "courses": courses,
            }
        )

    """
    In class-based views:
    Instead of using an if statement to check the request method,  
    we simply create class methods called GET, POST, or any other HTTP verb.
    """
    def post(self, request, *args, **kwargs):
        """
        Get the course the Occupational Therapist chose.
        Then generate a chart for it!
        """
        client_id = request.POST['client']
        try:
            course_id = request.POST['chosenCourse']
        except KeyError:
            messages.error(request, 'You must select one of the courses below')
            return HttpResponseRedirect(reverse('chooseCourse', args=[client_id]))
        
        return HttpResponseRedirect(reverse('generateChart', args=[course_id]))


class NewCourse(TemplateView):
    template_name = "hippo/newCourse.html"
    
    """
    In class-based views:
    Instead of using an if statement to check the request method,  
    we simply create class methods called GET, POST, or any other HTTP verb.
    """
    def get(self, request, *args, **kwargs):
        session = kwargs['session']
        
        last_session = get_object_or_404(Session.objects.filter(id=session))
        
        return render(
            request, 
            self.template_name, # view to render
            # Context - passed into the HTML template
            {
                "session": last_session,
            }
        )

    """
    In class-based views:
    Instead of using an if statement to check the request method,  
    we simply create class methods called GET, POST, or any other HTTP verb.
    """
    def post(self, request, *args, **kwargs):
        create_new_course = False
        new_course = ''
        try:
            new_course = request.POST['newCourse']
            create_new_course = True
        except KeyError:
            # Do nothing - create_new_course is already false
            pass
        

        client = kwargs['client']
        
        if create_new_course:
            get_course_for_client(client, True)

        # https://www.tutorialspoint.com/django/django_page_redirection.htm
        return redirect(
            'recordSession',       # view to render
            client=client,   # parameter to pass to URL
        )


