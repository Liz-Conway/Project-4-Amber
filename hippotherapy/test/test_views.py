'''
Created on 14 May 2022

@author: liz
'''
from django.test import TestCase, Client as TestClient
from hippotherapy.models import Session, Skill, SkillScore, Course, Hat,\
    Function
from hippotherapy.models import Client
from administration.models import Diagnosis, Horse, Task
from django.urls.base import reverse
from datetime import datetime
from django.contrib.messages.api import get_messages
from profiles.models import HippotherapyUser

class ViewsTest(TestCase):
    def setUp(self):
        self.hat = Hat.objects.create(size='5')
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
        
        self.hat_sizes = ['1']  # Refers to the ID of the hat in the hat table
        self.genders = ['M', 'F']
        self.diagnoses = [Diagnosis.objects.create(
            diagnosis='ASD'), 
            Diagnosis.objects.create(diagnosis='ADD'), 
            Diagnosis.objects.create(diagnosis='ADHD')]
        
        # Create some skills
        self.function = Function.objects.create(function_name='Test Function')
        self.basket_weaving = Skill.objects.create(
            skill_name="Basket Weaving", function=self.function)
        self.flower_arranging = Skill.objects.create(
            skill_name="Flower Arranging", function=self.function)
        self.embroidery = Skill.objects.create(
            skill_name="Embroidery", function=self.function)
        
        # Score some skills
        self.basket_score = SkillScore.objects.create(
            session=self.hip_session, skill=self.basket_weaving, score=1)
        self.flower_score = SkillScore.objects.create(
            session=self.hip_session, skill=self.flower_arranging, score=3)
        self.sewing_score = SkillScore.objects.create(
            session=self.hip_session, skill=self.embroidery, score=5)
        
        # Add some tasks
        self.task1 = Task.objects.create(task_name="First Task")
        self.task2 = Task.objects.create(task_name="Second Task")
        self.task3 = Task.objects.create(
            task_name="Third Task", mounted=True)
        self.task4 = Task.objects.create(
            task_name="Fourth Task", mounted=True)

        self.test_client = TestClient()
        self.home_url = reverse('home')
        self.add_client_url = reverse('addClient')
        self.record_session_url = reverse(
            'recordSession', args=[self.hip_client.id, self.hip_session.id])
        self.select_client_url = reverse(
            'selectClient', args=['recordSession'])
        self.observe_session_url = reverse(
            'observeSession', args=[self.hip_session.id, self.hip_session.id])
        self.generate_chart_url = reverse(
            'generateChart', args=[self.course.id])
        self.choose_course_client = reverse(
            'chooseCourse', args=[self.hip_client.id])
        self.new_course_url = reverse(
            'newCourse', args=[self.hip_client.id, self.hip_session.id])
        self.add_diagnosis_url = reverse(
            'addDiagnosis')
        self.choose_session_url = reverse(
            'chooseSession', args=[self.hip_client.id])
        
        self.ot_login =  {
            'username': 'testotuser',
            'password': 'secret', 
            'role': 2}
        self.ot_user = HippotherapyUser.objects.create_user(**self.ot_login)
        
    def test_show_home_page(self):
        response = self.test_client.get(self.home_url)
        
        self.assertEqual(
            response.status_code, 200, 
            "Going to home page should return a Status Code of 200 (OK)")
        self.assertTemplateUsed(
            response, "index.html", 
            "Home page should use the index.html template")

    def test_show_home_page_blank_url(self):
        response = self.test_client.get('')
        
        self.assertEqual(
            response.status_code, 200, 
            "Going to home page should return a Status Code of 200 (OK)")
        self.assertTemplateUsed(
            response, "index.html", 
            "Home page should use the index.html template")

    def test_get_add_diagnosis(self):
        response = self.test_client.get(self.add_diagnosis_url)
        
        self.assertEqual(
            response.status_code, 200, 
            "Going to Add Diagnosis page should\
             return a Status Code of 200 (OK)")
        self.assertTemplateUsed(
            response, "admins/addDiagnosis.html", 
            "Add Diagnosis page should use the addDiagnosis.html template")

    def test_post_add_diagnosis(self):
        post_data = {
            'diagnosis': 'New Diagnosis',
        }
        
        response = self.test_client.post(self.add_diagnosis_url, post_data)
        # messages = list(response.context['messages'])
        
        # Since we redisplay the Add Diagnosis page again 
        # after successfully adding a diagnosis
        # the Status Code is 200 because we used a GET instead of a redirect
        self.assertEqual(
            response.status_code, 200, 
            'Posting the Add Diagnosis form should\
             return a Status Code of 200 (OK)')
        
        self.assertEqual(
            Diagnosis.objects.last().diagnosis, 
            'New Diagnosis', 'Diagnosis should be "New Diagnosis"')
        
    def test_get_add_client(self):
        response = self.test_client.get(self.add_client_url)
        print(response['location'])
        self.loginAsOT()
        self.assertEqual(
            response.status_code, 200, 
            "Going to Add Client page should return a Status Code of 200 (OK)")
        self.assertTemplateUsed(
            response, "hippo/addClient.html", 
            "Add Client page should use the addClient.html template")

    def loginAsOT(self):
        response = self.client.post(
            '/accounts/login/', self.ot_login, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_authenticated())

    def test_post_add_client(self):
        post_data = {
            'first_name': 'Donald',
            'last_name': 'Duck',
            'gender': self.genders[0],
            'date_of_birth': '09/06/1931',
            'hat_size': self.hat.id,
            'degree_of_difficulty': 'Gets annoyed very quickly',
            'additional_notes': 'Speaks quackily'
        }
        
        post_data.update({f'diagnosis_{self.diagnoses[0].id}': 'on'})

        
        response = self.test_client.post(self.add_client_url, post_data)
        
        # Since we redisplay the Add Client page 
        # again after successfully adding a client
        # the Status Code is 200 because we used a GET instead of a redirect
        self.assertEqual(
            response.status_code, 200, 
            'Posting the Add Client form should\
             return a Status Code of 200 (OK)')
        
        self.assertEqual(
            Client.objects.last().first_name, 
            'Donald', 'First name should be Donald')
        self.assertEqual(
            Client.objects.last().last_name, 
            'Duck', 'Last name should be Duck')
        self.assertEqual(
            Client.objects.last().gender, 'M', 'Gender should be Male')
        self.assertEqual(
            Client.objects.last().date_of_birth, 
            datetime.strptime('09/06/1931', '%d/%m/%Y').date(),
             'Donald Duck was born on 9th June 1931')
        self.assertEqual(
            Client.objects.last().hat_size, self.hat,
             'Donald Duck has a hat size of 5')
        # For many-to-many relationships - 
        # Need to use 'get' to retrieve the associated object
        self.assertEqual(
            Client.objects.last().diagnosis.get(), 
            self.diagnoses[0], 
            'Donald Duck has the first diagnosis on the list')
        self.assertEqual(
            Client.objects.last().degree_of_difficulty, 
            'Gets annoyed very quickly', 
            'Donald certainly Gets annoyed very quickly')
        self.assertEqual(
            Client.objects.last().additional_notes, 
            'Speaks quackily', 
            'Additional notes should say :  Speaks quackily')
        
        self.assertTemplateUsed(
            response, 'hippo/addClient.html', 
            'Add Client page should use the addClient.html template')
        
    def test_post_add_client_multiple_diagnoses(self):
        post_data = {
            'first_name': 'Donald',
            'last_name': 'Duck',
            'gender': self.genders[0],
            'date_of_birth': '09/06/1931',
            'hat_size': self.hat.id,
            'degree_of_difficulty': 'Gets annoyed very quickly',
            'additional_notes': 'Speaks quackily'
        }
        for diagnosis in self.diagnoses:
            post_data.update({f'diagnosis_{diagnosis.id}': 'on'})
        
        response = self.test_client.post(self.add_client_url, post_data)
        
        # Since we redisplay the Add Client page
         # again after successfully adding a client
        # the Status Code is 200 because we used a GET instead of a redirect
        self.assertEqual(
            response.status_code, 200, 
            'Posting the Add Client form should\
             return a Status Code of 200 (OK)')
        
        last_client = Client.objects.last()
        
        self.assertEqual(
            last_client.first_name, 
            'Donald', 'First name should be Donald')
        self.assertEqual(
            last_client.last_name, 'Duck', 'Last name should be Duck')
        self.assertEqual(last_client.gender, 'M', 'Gender should be Male')
        self.assertEqual(
            last_client.date_of_birth, 
            datetime.strptime('09/06/1931', '%d/%m/%Y').date(), 
            'Donald Duck was born on 9th June 1931')
        self.assertEqual
        (last_client.hat_size, self.hat, 
         'Donald Duck has a hat size of 5')
        # For many-to-many relationships - 
        # Need to use 'all()' to retrieve the associated objects
        all_diagnoses = last_client.diagnosis.all()
        for i in range(all_diagnoses.count()):
            self.assertEquals(
                all_diagnoses[i], self.diagnoses[i], 
                'Should have the same diagnosis')
        self.assertEqual(
            last_client.degree_of_difficulty, 
            'Gets annoyed very quickly', 
            'Donald certainly Gets annoyed very quickly')
        self.assertEqual(
            last_client.additional_notes, 
            'Speaks quackily', 
            'Additional notes should say :  Speaks quackily')
        
        self.assertTemplateUsed(
            response, 'hippo/addClient.html', 
            'Add Client page should use the addClient.html template')
        
    def test_post_add_client_success_message(self):
        post_data = {
            'first_name': 'Donald',
            'last_name': 'Duck',
            'gender': self.genders[0],
            'date_of_birth': '09/06/1931',
            'hat_size': self.hat.id,
            'degree_of_difficulty': 'Gets annoyed very quickly',
            'additional_notes': 'Speaks quackily'
        }
        
        response = self.test_client.post(self.add_client_url, post_data)
        
        # https://stackoverflow.com/questions/2897609/
        # how-can-i-unit-test-django-messages
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        message = str(messages[0])
        
        # Since we redisplay the Add Client page
         # again after successfully adding a client
        # the Status Code is 200 because we used a GET instead of a redirect
        self.assertEqual(
            response.status_code, 200, 
            'Posting the Add Client form should\
             return a Status Code of 200 (OK)')
        self.assertTemplateUsed(
            response, 'hippo/addClient.html', 
            'Add Client page should use the addClient.html template')
        self.assertEqual(
            message, 
            'New client <span class="name">\
            Donald Duck</span> added successfully.', 
            'Should have a success message when a client is added.')
        

    def test_get_record_session(self):
        response = self.test_client.get(self.record_session_url)
        
        self.assertEqual(
            response.status_code, 200, 
            "Going to Record Session page should\
             return a Status Code of 200 (OK)")
        self.assertTemplateUsed(
            response, "hippo/recordSession.html", 
            "Record Session page should use the recordSession.html template")

    def test_get_record_session_no_client(self):
        response = self.test_client.get(
            reverse('recordSession', args=[666, self.hip_session.id]))
        
        self.assertEqual(
            response.status_code, 404, 
            "Going to Record Session page with a non-existant\
             client should return a Status Code of 404")

    def test_post_record_session_new_course(self):
        course = Course.objects.create(client = self.hip_client)
        post_data = {
            'course': course.id,
            'week_number': 1,
            'horse': self.horse.id,
            'task_4': 'on',
            'task_14': 'on',
        }
        
        response = self.test_client.post(self.record_session_url, post_data)
        
        self.assertEqual(
            response.status_code, 302, 
            'Posting the Record Session form should cause a redirect (302)')
        self.assertEqual(
            Session.objects.last().course_id, course.id, 
            "Should have created a Session with course id = 19")
        self.assertEqual(
            Session.objects.last().week_number, 1, 
            "Should have created a Session with week_number = 1")
        self.assertEqual(
            Session.objects.last().horse_id, self.horse.id, 
            "Should have created a Session with horse id = 2")
    
    def test_post_record_session_new_course_tasks(self):
        course = Course.objects.create(client = self.hip_client)
        post_data = {
            'course': course.id,
            'week_number': 1,
            'horse': self.horse.id,
            f'task_{self.task1.id}': 'on',
            f'task_{self.task3.id}': 'on',
        }
        
        response = self.test_client.post(self.record_session_url, post_data)
        
        self.assertEqual(
            response.status_code, 302, 
            'Posting the Record Session form should cause a redirect (302)')
        last_session = Session.objects.last()
        # Get the Tasks for the chosen session
        tasks = Task.objects.filter(performed__id=last_session.id)
        task_count = tasks.count()
        self.assertEqual(task_count, 2, 
                         'Posted session should have 2 tasks associated')
        for task in tasks:
            self.assertIn(
                task.id, [self.task1.id, self.task3.id], 
                'Tasks should be task with ID = 4 or 14')
    
    def test_post_record_session_success_message(self):
        course = Course.objects.create(client = self.hip_client)
        post_data = {
            'course': course.id,
            'week_number': 1,
            'horse': self.horse.id,
            f'task_{self.task1.id}': 'on',
            f'task_{self.task3.id}': 'on',
        }
        
        response = self.test_client.post(self.record_session_url, post_data)
        
        # Redirect does not have a context
        # so need to use this instead
        messages = list(response.wsgi_request._messages)
        self.assertEqual(
            len(messages), 1, 
            'Should have 1 message on successful creation of a session')
        message = messages[0].message
        
        self.assertEqual(
            response.status_code, 302, 
            'Posting the Record Session form should cause a redirect (302)')
        self.assertEqual(
            message, 
            f'New session for <span class="boldEntry"\
            Mister Blobby</span> ({course.id}/1) added successfully.', 
            'Should have a success message when a new session is created.')

    def test_post_record_session_fail_message(self):
        course = Course.objects.create(client = self.hip_client)
        post_data = {
            'course': course.id,
            'week_number': 1,
            f'task_{self.task1.id}': 'on',
            f'task_{self.task3.id}': 'on',
        }
        
        response = self.test_client.post(self.record_session_url, post_data)
        
        # Redirect does not have a context
        # so need to use this instead
        messages = list(response.wsgi_request._messages)
        self.assertEqual(
            len(messages), 2, 
            'Should have 1 message on submitting\
             a session without filling all details')
        message1 = messages[0].message
        message2 = messages[1].message
        
        self.assertEqual(
            response.status_code, 302, 
            'Posting the Record Session form should cause a redirect (302)')
        self.assertEqual(
            message1, 'Invalid form submission.',
'Should have a message indicating that there\
 was an error with the form submission')
        self.assertEqual(
            message2, 
            '<ul class="errorlist"><li>horse<ul class="errorlist">\
            <li>This field is required.</li></ul></li></ul>', 
            'Should have a message showing that the horse was not chosen')

    def test_get_observe_session(self):
        response = self.test_client.get(self.observe_session_url)
    
        self.assertEqual(
            response.status_code, 200, 
            "Going to Observe Session page should\
             return a Status Code of 200 (OK)")
        self.assertTemplateUsed(
            response, "hippo/observeSession.html", 
            "Observe Session page should \
            use the observeSession.html template")

    def test_get_observe_session_no_session(self):
        response = self.test_client.get(
            reverse('observeSession', args=[666, self.hip_session.id]))
    
        self.assertEqual(
            response.status_code, 404, 
            "Going to Observe Session page with a non-existant\
             session should return a Status Code of 404")

    def test_post_observe_session(self):
        post_data = {
            f'score{self.basket_weaving.id}': 1,
            f'score{self.flower_arranging.id}': 3,
            f'score{self.embroidery.id}': 5,
        }
        
        response = self.test_client.post(self.observe_session_url, post_data)
        
        self.assertEqual(
            response.status_code, 302, 
            'Posting the Session Observations\
             form should cause a redirect (302)')
        self.assertEqual(
            SkillScore.objects.filter(
                skill=self.basket_weaving).last().score, 1, 
            "Should have created a SkillScore with score = 1")
        self.assertEqual(
            SkillScore.objects.filter(
                skill=self.flower_arranging).last().score, 3, 
            "Should have created a SkillScore with score = 3")
        self.assertEqual(
            SkillScore.objects.filter(
                skill=self.embroidery).last().score, 5, 
            "Should have created a SkillScore with score = 5")

        
    def test_post_observe_session_only_some_skills_scored(self):
        post_data = {
            f'score{self.basket_weaving.id}': 1,
            f'score{self.flower_arranging.id}': 3,
        }
        
        response = self.test_client.post(self.observe_session_url, post_data)
        
        self.assertEqual(
            response.status_code, 302, 
            'Posting the Session Observations\
             form should cause a redirect (302)')
        self.assertEqual(
            SkillScore.objects.filter(
                skill=self.basket_weaving).last().score, 1, 
            "Should have created a SkillScore with score = 1")
        self.assertEqual(
            SkillScore.objects.filter(
                skill=self.flower_arranging).last().score, 3, 
            "Should have created a SkillScore with score = 3")

    def test_get_select_client(self):
        response = self.test_client.get(self.select_client_url)
        
        self.assertEqual(
            response.status_code, 200, 
            "Going to Select Client page\
             should return a Status Code of 200 (OK)")
        self.assertTemplateUsed(
            response, "hippo/selectClient.html", 
            "Select Client page should use the selectClient.html template")

    def test_get_select_client_any_target(self):
        response = self.test_client.get(
            reverse('selectClient', args=['any target']))
        
        self.assertEqual(
            response.status_code, 200,
             "Going to Select Client page should return a Status Code\
              of 200 (OK) regardless of the target passed in")
        self.assertTemplateUsed(
            response, "hippo/selectClient.html", 
            "Select Client page should use the selectClient.html template")

    def test_post_select_client_generate_chart(self):
        post_data = {
            'targetPage': 'generateChart',
            'client': self.hip_client.id,
        }
        
        response = self.test_client.post(self.select_client_url, post_data)
        
        self.assertEqual(
            response.status_code, 302, 
            'Posting the Select Client form should cause a redirect (302)')
        self.assertRedirects(
            response, self.choose_course_client, 302, 200, msg_prefix='', 
            fetch_redirect_response=True)

    def test_post_select_client_view_session(self):
        post_data = {
            'targetPage': 'chooseSession',
            'client': self.hip_client.id,
        }
        
        response = self.test_client.post(self.select_client_url, post_data)
        
        self.assertEqual(
            response.status_code, 302, 
            'Posting the Select Client form should cause a redirect (302)')
        self.assertRedirects(
            response, self.choose_session_url, 302, 200, msg_prefix='', 
            fetch_redirect_response=True)

    def test_post_select_client_record_session(self):
        post_data = {
            'targetPage': 'recordSession',
            'client': self.hip_client.id,
        }
        
        response = self.test_client.post(self.select_client_url, post_data)
        
        self.assertEqual(
            response.status_code, 302, 
            'Posting the Select Client form should cause a redirect (302)')
        self.assertRedirects(
            response, self.new_course_url, 302, 200, msg_prefix='', 
            fetch_redirect_response=True)

    def test_get_generate_chart(self):
        # Needed to add some skill scores for this to work
        response = self.test_client.get(self.generate_chart_url)
    
        self.assertEqual(
            response.status_code, 200, 
            "Going to Generate Chart page should\
             return a Status Code of 200 (OK)")
        self.assertTemplateUsed(
            response, "hippo/generateChart.html",
             "Generate Chart page should use the generateChart.html template")

    def test_get_generate_chart_no_course(self):
        # Needed to add some skill scores for this to work
        response = self.test_client.get(reverse('generateChart', args=[666]))
    
        self.assertEqual(
            response.status_code, 404, 
            "Going to Generate Chart page with a non-existant course should\
             return a Status Code of 404")

    def test_get_choose_course_client_only(self):
        response = self.test_client.get(self.choose_course_client)
    
        self.assertEqual(
            response.status_code, 200, 
            "Going to Choose Course page should return \
            a Status Code of 200 (OK)")
        self.assertTemplateUsed(
            response, "hippo/chooseCourse.html", 
            "Choose Course page should use the chooseCourse.html template")

    def test_get_choose_course_no_client(self):
        response = self.test_client.get(reverse('chooseCourse', args=[666]))
    
        self.assertEqual(
            response.status_code, 404, 
            "Going to Choose Course page with a non-existant client should \
            return a Status Code of 404")

    def test_post_choose_course(self):
        post_data = {
            'client': self.hip_client.id,
            'chosenCourse': self.course.id,
        }
        
        response = self.test_client.post(self.choose_course_client, post_data)
        
        self.assertEqual(
            response.status_code, 302, 
            'Posting the Choose Course form should cause a redirect (302)')
        self.assertRedirects(
            response, self.generate_chart_url, 302, 200, msg_prefix='', 
            fetch_redirect_response=True)

    def test_post_choose_course_none_chosen(self):
        post_data = {
            'client': self.hip_client.id,
        }
        
        response = self.test_client.post(self.choose_course_client, post_data)
        # Redirect does not have a context
        # so need to use this instead
        messages = list(response.wsgi_request._messages)
        self.assertEqual(
            len(messages), 1, 
            'Should have 1 message on submitting without choosing a course')
        message1 = messages[0].message
        
        self.assertEqual(
            response.status_code, 302, 
            'Posting the Choose Course form without selecting a course should \
            cause a redirect (302) back to the Choose Course page')
        self.assertRedirects(
            response, self.choose_course_client, 302, 200, msg_prefix='', 
            fetch_redirect_response=True)
        self.assertEqual(
            message1, 'You must select one of the courses below', 
            'Should have a message indicating that there was an\
             error with the form submission')

    def test_get_new_course(self):
        response = self.test_client.get(self.new_course_url)
    
        self.assertEqual(
            response.status_code, 200, 
            "Going to New Course page should\
             return a Status Code of 200 (OK)")
        self.assertTemplateUsed(
            response, "hippo/newCourse.html", 
            "New Course page should use the newCourse.html template")

    def test_post_new_course_use_existing_course(self):
        post_data = {  }
        
        pre_course_count = Course.objects.count()
        response = self.test_client.post(
            self.new_course_url, post_data)
        post_course_count = Course.objects.count()
        
        self.assertEqual(
            response.status_code, 302, 
            'Posting the Choose Course form should\
             cause a redirect (302) to the Record Session page')
        self.assertRedirects(
            response, self.record_session_url, 302, 200, msg_prefix='', 
            fetch_redirect_response=True)
        self.assertEqual(
            Course.objects.last(), self.course, 
            'Should have the same courses as before')
        self.assertEqual(
            pre_course_count, post_course_count, 
            'Should have the same number of courses as before')

    def test_post_new_course_make_new_course(self):
        post_data = { 'newCourse': 'on' }
        
        pre_course_count = Course.objects.count()
        response = self.test_client.post(self.new_course_url, post_data)
        post_course_count = Course.objects.count()
        
        self.assertEqual(
            response.status_code, 302, 
            'Posting the Choose Course form should cause \
            a redirect (302) to the Record Session page')
        self.assertRedirects(
            response, self.record_session_url, 302, 200, msg_prefix='', 
            fetch_redirect_response=True)
        self.assertEqual(
            pre_course_count + 1, post_course_count, 
            'Should have one more course than before the form was submitted')
