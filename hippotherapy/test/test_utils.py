'''
Created on 8 Jun 2022

@author: liz
'''
from django.test import TestCase
from hippotherapy.hippotherapy_utils import get_course_for_client,\
    get_course_with_no_sessions, get_next_session_week, save_tasks,\
    save_diagnoses, convert_observations, create_course_for_client,\
    get_scored_courses_for_client
from hippotherapy.models import Client, Course, Hat, Session, Function, Skill,\
    SkillScore
import datetime
from datetime import datetime
from administration.models import Horse, Task, Diagnosis

class UtilTest(TestCase):


    def setUp(self):
        self.hat = Hat.objects.create(size='3 1/2')
        self.hip_client = Client.objects.create(
            first_name = 'Mister',
            last_name = 'Blobby',
            gender = 'M',
            date_of_birth = datetime.today(),
            hat_size = self.hat,
        )
        
        self.course = Course.objects.create(
            client = self.hip_client
        )
        
        self.horse = Horse.objects.create(
            horse_name = 'Neddie'
        )
        
        self.hip_session = Session.objects.create(
            course = self.course,
            week_number = 1,
            horse = self.horse
        )
        
        self.hip_session_second = Session.objects.create(
            course = self.course,
            week_number = 2,
            horse = self.horse
        )
        
        self.task1 = Task.objects.create(task_name='Dance merengue', mounted=True)
        self.task2 = Task.objects.create(task_name='Pole vault', mounted=False)
        
        self.diagnosis1 = Diagnosis.objects.create(diagnosis='hysteria')
        self.diagnosis2 = Diagnosis.objects.create(diagnosis='Rickets')
        
        # Create some skills
        self.function = Function.objects.create(function_name='Test Function')
        self.basket_weaving = Skill.objects.create(skill_name="Basket Weaving", function=self.function)
        self.flower_arranging = Skill.objects.create(skill_name="Flower Arranging", function=self.function)
        self.embroidery = Skill.objects.create(skill_name="Embroidery", function=self.function)

        # Score some skills
        self.basket_score = SkillScore.objects.create(session=self.hip_session, skill=self.basket_weaving, score=1)
        self.flower_score = SkillScore.objects.create(session=self.hip_session, skill=self.flower_arranging, score=3)
        self.sewing_score = SkillScore.objects.create(session=self.hip_session, skill=self.embroidery, score=5)
        
        

    def test_get_course_no_sessions(self):
        # Create a course that has NO sessions
        self.course_no_session = Course.objects.create(
            client = self.hip_client
        )
        
        course = get_course_with_no_sessions(self.hip_client.id)
        
        self.assertEqual(course, self.course_no_session, "Should return a course that has no sessions")

    def test_get_course_no_sessions_has_sessions(self):
        course = get_course_with_no_sessions(self.hip_client.id)
    
        self.assertEqual(course, None, "Should return NONE when no courses have no sessions")

    def test_get_course_for_client(self):
        course = get_course_for_client(self.hip_client.id)
    
        self.assertEqual(course, self.course, "Should return a course for Mister Blobby")

    def test_get_course_for_client_2_courses(self):
        second_course = Course.objects.create(client=self.hip_client)
        # Create sessions for the second course
        Session.objects.create(
            course = second_course,
            week_number = 1,
            horse = self.horse
        )
        Session.objects.create(
            course = second_course,
            week_number = 2,
            horse = self.horse
        )

        course = get_course_for_client(self.hip_client.id)
    
        self.assertEqual(course, second_course, "Should return the latest course for Mister Blobby")

    def test_get_course_for_client_3_courses(self):
        second_course = Course.objects.create(client=self.hip_client)
        # Create sessions for the second course
        Session.objects.create(
            course = second_course,
            week_number = 1,
            horse = self.horse
        )
        Session.objects.create(
            course = second_course,
            week_number = 2,
            horse = self.horse
        )

        third_course = Course.objects.create(client=self.hip_client)
        # Create sessions for the second course
        Session.objects.create(
            course = third_course,
            week_number = 1,
            horse = self.horse
        )
        Session.objects.create(
            course = third_course,
            week_number = 2,
            horse = self.horse
        )

        course = get_course_for_client(self.hip_client.id)
    
        self.assertEqual(course, third_course, "Should return the latest course for Mister Blobby")

    def test_get_course_for_client_no_courses(self):
        donald_duck = Client.objects.create(
            first_name = 'Donald',
            last_name = 'Duck',
            gender = 'M',
            date_of_birth = datetime.today(),
            hat_size = self.hat,
        )
        
        course = get_course_for_client(donald_duck.id)
        
        self.assertNotEqual(course, None, "Courseless client should be given a new course")
        self.assertNotEqual(course.id, self.course.id, "Course returned should have a different ID to existing course")

    def test_get_course_for_client_new_courses(self):
        course = get_course_for_client(self.hip_client.id, True)
        
        self.assertNotEqual(course, None, "Client should be given a new course")
        self.assertNotEqual(course.id, self.course.id, "Course returned should have a different ID to existing course")

    def test_get_course_for_client_create_new(self):
        brand_new = Course.objects.create(client=self.hip_client)
        
        course = get_course_for_client(self.hip_client.id)
        
        self.assertEqual(course, brand_new, "Should return the new course")

    def test_next_session_week(self):
        week = get_next_session_week(self.course)
        
        self.assertEqual(week, 3, "Should return week number 3")

    def test_next_session_week_no_sessions(self):
        new_course = Course.objects.create(client=self.hip_client)
        
        week = get_next_session_week(new_course)
        
        self.assertEqual(week, 1, "Should return week number 1")

    def test_save_tasks(self):
        pre_task_client = Session.objects.filter(id=self.hip_session.id).prefetch_related('tasks')[0]
        pre_task = list(pre_task_client.tasks.all())
        self.assertEqual(len(pre_task), 0, 'Session should have NO tasks before saving tasks')
        post_data = {
            f'task_{self.task1.id}': 'on',
            f'task_{self.task2.id}': 'on'
        }
        
        save_tasks(self.hip_session.id, post_data)
        
        task_session = Session.objects.filter(id=self.hip_session.id).prefetch_related('tasks')[0]
        
        tasks = list(task_session.tasks.all())
        
        self.assertEqual(len(tasks), 2, 'Should be 2 tasks for this session')
        for task in tasks:
            self.assertIn(task.id, [self.task1.id, self.task2.id], 'Task for the session should be one of the defined tasks')
            
    def test_save_tasks_no_tasks(self):
        post_data = {
        }
        
        save_tasks(self.hip_session.id, post_data)
        
        task_session = Session.objects.filter(id=self.hip_session.id).prefetch_related('tasks')[0]
        
        tasks = list(task_session.tasks.all())
        
        self.assertEqual(len(tasks), 0, 'Should be 0 tasks for this session')
            
    def test_save_diagnosis(self):
        pre_diagnoses_client = Client.objects.filter(id=self.hip_client.id).prefetch_related('diagnosis')[0]
        pre_diagnoses = list(pre_diagnoses_client.diagnosis.all())
        self.assertEqual(len(pre_diagnoses), 0, 'Client should have NO diagnoses before saving a diagnosis')

        post_data = {
            f'diagnosis_{self.diagnosis1.id}': 'on',
            f'diagnosis_{self.diagnosis2.id}': 'on'
        }
        save_diagnoses(self.hip_client.id, post_data)
        
        diagnoses_client = Client.objects.filter(id=self.hip_client.id).prefetch_related('diagnosis')[0]
        diagnoses = list(diagnoses_client.diagnosis.all())
        self.assertEqual(len(diagnoses), 2, 'Client should have 2 diagnoses after saving the diagnosis')
        for diagnosis in diagnoses:
            self.assertIn(diagnosis.id, [self.diagnosis1.id, self.diagnosis2.id], 'Task for the session should be one of the defined tasks')

    def test_save_diagnosis_no_data(self):
        pre_diagnoses_client = Client.objects.filter(id=self.hip_client.id).prefetch_related('diagnosis')[0]
        pre_diagnoses = list(pre_diagnoses_client.diagnosis.all())
        self.assertEqual(len(pre_diagnoses), 0, 'Client should have NO diagnoses before saving a diagnosis')

        post_data = {
        }
        save_diagnoses(self.hip_client.id, post_data)
        
        diagnoses_client = Client.objects.filter(id=self.hip_client.id).prefetch_related('diagnosis')[0]
        diagnoses = list(diagnoses_client.diagnosis.all())
        self.assertEqual(len(diagnoses), 0, 'Client should have NO diagnoses after saving the diagnosis')

    def test_convert_observations(self):
        old_observations = {
            f'score{self.basket_weaving.id}': 1,
            f'score{self.embroidery.id}': 3,
            f'score{self.flower_arranging.id}': 5,
        }
        
        expected_observations = [
            { 'skill': self.basket_weaving.id, 'score': 1},
            { 'skill': self.embroidery.id, 'score': 3},
            { 'skill': self.flower_arranging.id, 'score': 5},
        ]
        
        actual_observations = convert_observations(old_observations)
        
        self.assertEqual(actual_observations, expected_observations, 'Should have converted old observations correctly')
        
        # NO data
    def test_convert_observations_no_data(self):
        old_observations = {
        }
        
        expected_observations = [
        ]
        
        actual_observations = convert_observations(old_observations)
        
        self.assertEqual(actual_observations, expected_observations, 'Data Should be empty')
        
    def test_create_course_for_client(self):
        last_course = Course.objects.filter(client=self.hip_client).last()
        old_course_count = Course.objects.filter(client=self.hip_client).count()
        
        create_course_for_client(self.hip_client.id)
        
        new_course = Course.objects.filter(client=self.hip_client).last()
        new_course_count = Course.objects.filter(client=self.hip_client).count()
        
        self.assertGreater(new_course.id, last_course.id, 'New course should have increased the course id')
        self.assertEqual(new_course_count, old_course_count + 1, 'Should now be one more course for this client')
        
    def test_get_scored_courses_for_client(self):
        # First session of 1st course is scored
        # Second session of 1st course is not scored
        # First course should be scored
        
        scored = get_scored_courses_for_client(self.hip_client.id)[0]
        
        self.assertEqual(scored['course'], self.course.id, 'Should return the first course id')
        self.assertEqual(scored['first_week'], 1, 'First scored week should be week 1')
        self.assertEqual(scored['last_week'], 1, 'Last scored week should be week 1 as well')
        self.assertEqual(datetime.strptime(scored['last_date'], '%a, %d %b %Y').date(), self.hip_session.session_date, 'Dates should be the same')
        self.assertEqual(datetime.strptime(scored['first_date'], '%a, %d %b %Y').date(), self.hip_session.session_date, 'Dates should be the same')
        
    # Multiple scored courses
    def test_get_scored_courses_for_client_multiple_scored_courses(self):
        # First session of 1st course is scored
        # Second session of 1st course is not scored
        # Add more scored courses
        next_scored_course = Course.objects.create(
            client = self.hip_client
        )
        
        next_scored_session = Session.objects.create(
            course = next_scored_course,
            week_number = 1,
            horse = self.horse
        )
        
        next_scored_session2 = Session.objects.create(
            course = next_scored_course,
            week_number = 2,
            horse = self.horse
        )
        
        # Score some skills
        SkillScore.objects.create(session=next_scored_session, skill=self.basket_weaving, score=2)
        SkillScore.objects.create(session=next_scored_session, skill=self.flower_arranging, score=4)
        SkillScore.objects.create(session=next_scored_session, skill=self.embroidery, score=1)
        SkillScore.objects.create(session=next_scored_session2, skill=self.basket_weaving, score=3)
        SkillScore.objects.create(session=next_scored_session2, skill=self.flower_arranging, score=4)
        SkillScore.objects.create(session=next_scored_session2, skill=self.embroidery, score=5)

        scored = get_scored_courses_for_client(self.hip_client.id)[0]
        
        self.assertEqual(scored['course'], self.course.id, 'Should return the first course id')
        self.assertEqual(scored['first_week'], 1, 'First scored week should be week 1')
        self.assertEqual(scored['last_week'], 1, 'Last scored week should be week 1 as well')
        self.assertEqual(datetime.strptime(scored['last_date'], '%a, %d %b %Y').date(), self.hip_session.session_date, 'Dates should be the same')
        self.assertEqual(datetime.strptime(scored['first_date'], '%a, %d %b %Y').date(), self.hip_session.session_date, 'Dates should be the same')

        scored = get_scored_courses_for_client(self.hip_client.id)[1]
        
        self.assertEqual(scored['course'], next_scored_course.id, 'Should return the next course id')
        self.assertEqual(scored['first_week'], 1, 'First scored week should be week 1')
        self.assertEqual(scored['last_week'], 2, 'Last scored week should be week 2')
        self.assertEqual(datetime.strptime(scored['last_date'], '%a, %d %b %Y').date(), next_scored_session2.session_date, 'Dates should be the same')
        self.assertEqual(datetime.strptime(scored['first_date'], '%a, %d %b %Y').date(), next_scored_session.session_date, 'Dates should be the same')


        
    
    