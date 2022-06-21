'''
Created on 8 Jun 2022

@author: liz
'''
from hippotherapy.models import Course, Client, Session
from django.db.models.aggregates import Max, Min
from django.shortcuts import get_object_or_404
from administration.models import Task, Diagnosis

def get_course_with_no_sessions(client_id):
    courses = Course.objects.filter(client=client_id, courses=None).order_by('-id')
    if courses.count() == 0:
        # No brand new Courses
        return None
    
    # Otherwise return the 'brand new' course with the highest id
    return courses[0]



def get_course_for_client(client_id, new_course=False):
    courses = Course.objects.filter(client=client_id)
    brand_new_course = get_course_with_no_sessions(client_id)
    
    if courses.count() == 0 or new_course:
        # First course for this client
        # Retrieve an instance of the client
        client = Client.objects.filter(id=client_id)[0]
        # Create a new course for this client
        last_course = Course(client=client)
        # Save the course to the database
        last_course.save()
    elif brand_new_course != None:
        # We started a brand new course for this client
        return brand_new_course
    else:
        latest_course = None
        for course in courses:
            course_dates = {"course": course.id}
            # We need to find the latest week for a given course
            latest_week = Session.objects.filter(course=course.id).values('course').aggregate(Max('week_number'))['week_number__max']
            course_dates['last_week'] = latest_week
            # We need to find the date of the latest week for a given course
            latest_date = Session.objects.filter(week_number=latest_week, course=course.id).values('session_date')
            course_dates['last_date'] = latest_date[0]['session_date']
            if latest_course == None:
                latest_course = course_dates
            elif course_dates['last_date'] > latest_course['last_date']:
                # Replace latest_course with this course since this course is later
                latest_course = course_dates
            elif course_dates['last_date'] == latest_course['last_date']:
                # Need to find the latest course for the same date
                if course_dates['course'] > latest_course['course']:
                    latest_course = course_dates
        
        last_course = Course(id=latest_course['course'])
    
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
    
    session_query = Session.objects.filter(id=session_id)
    session = get_object_or_404(session_query)
    
    all_tasks = Task.objects.all()
    for task in all_tasks:
        task_identifier = f'task_{task.id}'
        
        if post.get(task_identifier) != None:
            session.tasks.add(task)
            
def save_diagnoses(client_id, post):
    client = Client.objects.get(id=client_id)
    
    for diagnosis in Diagnosis.objects.all():
        diagnosis_identifier = f'diagnosis_{diagnosis.id}'
        if post.get(diagnosis_identifier) != None:
            client.diagnosis.add(diagnosis)          
            
def update_diagnoses(client_id, post):
    client = Client.objects.get(id=client_id)
    
    for diagnosis in Diagnosis.objects.all():
        diagnosis_identifier = f'diagnosis_{diagnosis.id}'
        if post.get(diagnosis_identifier) != None:
            client.diagnosis.add(diagnosis)
        else:
            client.diagnosis.remove(diagnosis)        
            
def convert_observations(previous_observations):
    converted = []
    for observation in previous_observations:
        if observation.startswith('csrf'):
            continue
        skill_id = int(observation.split('score')[1])
        score = int(previous_observations[observation])
        
        observation_score = {'skill': skill_id, 'score': score}
        converted.append(observation_score)
    
    return converted

def create_course_for_client(client_id):
    # Retrieve an instance of the client
    client = get_object_or_404(Client.objects.filter(id=client_id))
    # Create a new course for this client
    new_course = Course(client=client)
    # Save the course to the database
    new_course.save()

def get_scored_courses_for_client(client):
    scored_courses = []
    courses = Course.objects.filter(client=client)
    for course in courses:
        course_dates = {"course":course.id} 
        # We need to find the latest week for a given course that has scores
        latest_week = Session.objects.filter(course=course.id).exclude(score_session=None).values('course').aggregate(Max('week_number'))['week_number__max']
        course_dates['last_week'] = latest_week
        # We need to find the date of the latest week for a given course that has scores
        latest_date = Session.objects.filter(week_number=latest_week, course=course.id).values('session_date')
        course_dates['last_date'] = latest_date[0]['session_date'].strftime("%a, %d %b %Y")
        # We need to find the first week for a given course that has scores
        first_week = Session.objects.filter(course=course.id).exclude(score_session=None).values('course').aggregate(Min('week_number'))['week_number__min']
        course_dates['first_week'] = first_week
        # We need to find the date of the first week for a given course that has scores
        first_date = Session.objects.filter(week_number=first_week, course=course.id).values('session_date')
        course_dates['first_date'] = first_date[0]['session_date'].strftime("%a, %d %b %Y")
        scored_courses.append(course_dates)
    
    return scored_courses

