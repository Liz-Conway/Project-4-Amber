'''
Created on 14 May 2022

@author: liz
'''
from django.test import TestCase, Client as TestClient
from hippotherapy.models import Session, Skill, SkillScore, Course, Hat,\
    Function
from hippotherapy.models import Client
from administration.models import Diagnosis, Horse
from django.urls.base import reverse
from datetime import datetime

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
        self.diagnoses = [Diagnosis.objects.create(diagnosis='ASD'), Diagnosis.objects.create(diagnosis='ADD'), Diagnosis.objects.create(diagnosis='ADHD')]
        
        # Create some skills
        self.function = Function.objects.create(function_name='Test Function')
        self.basket_weaving = Skill.objects.create(skill_name="Basket Weaving", function=self.function)
        self.flower_arranging = Skill.objects.create(skill_name="Flower Arranging", function=self.function)
        self.embroidery = Skill.objects.create(skill_name="Embroidery", function=self.function)
        
        # Score some skills
        self.basket_score = SkillScore.objects.create(session=self.hip_session, skill=self.basket_weaving, score=1)
        self.flower_score = SkillScore.objects.create(session=self.hip_session, skill=self.flower_arranging, score=3)
        self.sewing_score = SkillScore.objects.create(session=self.hip_session, skill=self.embroidery, score=5)

        self.test_client = TestClient()
        self.home_url = reverse('home')
        self.add_client_url = reverse('addClient')
        self.record_session_url = reverse('recordSession', args=[self.hip_client.id])
        self.select_client_url = reverse('selectClient', args=['recordSession'])
        self.observe_session_url = reverse('observeSession', args=[self.hip_session.id])
        self.generate_chart_url = reverse('generateChart', args=[self.course.id])
        self.choose_course_client = reverse('chooseCourse', args=[self.hip_client.id])
        self.new_course = reverse('newCourse', args=[self.hip_client.id, self.hip_session.id])
        self.add_diagnosis_url = reverse('addDiagnosis')
        
    def test_show_home_page(self):
        response = self.test_client.get(self.home_url)
        
        self.assertEqual(response.status_code, 200, "Going to home page should return a Status Code of 200 (OK)")
        self.assertTemplateUsed(response, "hippo/index.html", "Home page should use the index.html template")

    def test_show_home_page_blank_url(self):
        response = self.test_client.get('')
        
        self.assertEqual(response.status_code, 200, "Going to home page should return a Status Code of 200 (OK)")
        self.assertTemplateUsed(response, "hippo/index.html", "Home page should use the index.html template")

    def test_get_add_client(self):
        response = self.test_client.get(self.add_client_url)
        
        self.assertEqual(response.status_code, 200, "Going to Add Client page should return a Status Code of 200 (OK)")
        self.assertTemplateUsed(response, "hippo/addClient.html", "Add Client page should use the addClient.html template")

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
        messages = list(response.context['messages'])
        
        # self.assertEqual(response.status_code, 302, 'Posting the Add Client form should cause a redirect (302)')
        # Since we redisplay the Add Client page again after successfully adding a client
        # the Status Code is 200 because we used a GET instead of a redirect
        self.assertEqual(response.status_code, 200, 'Posting the Add Client form should return a Status Code of 200 (OK)')
        
        self.assertEqual(Client.objects.last().first_name, 'Donald', 'First name should be Donald')
        self.assertEqual(Client.objects.last().last_name, 'Duck', 'Last name should be Duck')
        self.assertEqual(Client.objects.last().gender, 'M', 'Gender should be Male')
        self.assertEqual(Client.objects.last().date_of_birth, datetime.strptime('09/06/1931', '%d/%m/%Y').date(), 'Donald Duck was born on 9th June 1931')
        self.assertEqual(Client.objects.last().hat_size, self.hat, 'Donald Duck has a hat size of 5')
        # For many-to-many relationships - Need to use 'get' to retrieve the associated object
        self.assertEqual(Client.objects.last().diagnosis.get(), self.diagnoses[0], 'Donald Duck has the first diagnosis on the list')
        self.assertEqual(Client.objects.last().degree_of_difficulty, 'Gets annoyed very quickly', 'Donald certainly Gets annoyed very quickly')
        self.assertEqual(Client.objects.last().additional_notes, 'Speaks quackily', 'Additional notes should say :  Speaks quackily')
        
        self.assertTemplateUsed(response, "addClient.html", "Add Client page should use the addClient.html template")
        
    def test_get_add_diagnosis(self):
        response = self.test_client.get(self.add_diagnosis_url)
        
        self.assertEqual(response.status_code, 200, "Going to Add Diagnosis page should return a Status Code of 200 (OK)")
        self.assertTemplateUsed(response, "admins/addDiagnosis.html", "Add Diagnosis page should use the addDiagnosis.html template")

    def test_post_add_diagnosis(self):
        post_data = {
            'diagnosis': 'New Diagnosis',
        }
        
        response = self.test_client.post(self.add_diagnosis_url, post_data)
        # messages = list(response.context['messages'])
        
        # self.assertEqual(response.status_code, 302, 'Posting the Add Diagnosis form should cause a redirect (302)')
        # Since we redisplay the Add Diagnosis page again after successfully adding a diagnosis
        # the Status Code is 200 because we used a GET instead of a redirect
        self.assertEqual(response.status_code, 200, 'Posting the Add Diagnosis form should return a Status Code of 200 (OK)')
        
        self.assertEqual(Diagnosis.objects.last().diagnosis, 'New Diagnosis', 'Diagnosis should be "New Diagnosis"')
        
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
        
        # Since we redisplay the Add Client page again after successfully adding a client
        # the Status Code is 200 because we used a GET instead of a redirect
        self.assertEqual(response.status_code, 200, 'Posting the Add Client form should return a Status Code of 200 (OK)')
        
        last_client = Client.objects.last()
        
        self.assertEqual(last_client.first_name, 'Donald', 'First name should be Donald')
        self.assertEqual(last_client.last_name, 'Duck', 'Last name should be Duck')
        self.assertEqual(last_client.gender, 'M', 'Gender should be Male')
        self.assertEqual(last_client.date_of_birth, datetime.strptime('09/06/1931', '%d/%m/%Y').date(), 'Donald Duck was born on 9th June 1931')
        self.assertEqual(last_client.hat_size, self.hat, 'Donald Duck has a hat size of 5')
        # For many-to-many relationships - Need to use 'all()' to retrieve the associated objects
        all_diagnoses = last_client.diagnosis.all()
        for i in range(all_diagnoses.count()):
            self.assertEquals(all_diagnoses[i], self.diagnoses[i], 'Should have the same diagnosis')
        self.assertEqual(last_client.degree_of_difficulty, 'Gets annoyed very quickly', 'Donald certainly Gets annoyed very quickly')
        self.assertEqual(last_client.additional_notes, 'Speaks quackily', 'Additional notes should say :  Speaks quackily')
        
        self.assertTemplateUsed(response, "addClient.html", "Add Client page should use the addClient.html template")
        
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
        for diagnosis in self.diagnoses:
            post_data.update({f'diagnosis_{diagnosis.id}': 'on'})
        
        response = self.test_client.post(self.add_client_url, post_data)
        messages = list(response.context['messages'])
        message = messages[0].message
        
        # Since we redisplay the Add Client page again after successfully adding a client
        # the Status Code is 200 because we used a GET instead of a redirect
        self.assertEqual(response.status_code, 200, 'Posting the Add Client form should return a Status Code of 200 (OK)')
        self.assertTemplateUsed(response, "addClient.html", "Add Client page should use the addClient.html template")
        self.assertEqual(message, 'New client <span class="name">Donald Duck</span> added successfully.', 'Should have a success message when a client is added.')
        
        
        
    def test_get_record_session(self):
        response = self.test_client.get(self.record_session_url)
        
        self.assertEqual(response.status_code, 200, "Going to Record Session page should return a Status Code of 200 (OK)")
        self.assertTemplateUsed(response, "hippo/recordSession.html", "Record Session page should use the recordSession.html template")

    def test_get_record_session_no_client(self):
        response = self.test_client.get(reverse('recordSession', args=[666]))
        
        self.assertEqual(response.status_code, 404, "Going to Record Session page with a non-existant client should return a Status Code of 404")

    def test_get_select_client(self):
        response = self.test_client.get(self.select_client_url)
        
        self.assertEqual(response.status_code, 200, "Going to Select Client page should return a Status Code of 200 (OK)")
        self.assertTemplateUsed(response, "hippo/selectClient.html", "Select Client page should use the selectClient.html template")

    def test_get_select_client_any_target(self):
        response = self.test_client.get(reverse('selectClient', args=['any target']))
        
        self.assertEqual(response.status_code, 200, "Going to Select Client page should return a Status Code of 200 (OK) regardless of the target passed in")
        self.assertTemplateUsed(response, "hippo/selectClient.html", "Select Client page should use the selectClient.html template")

    def test_get_observe_session(self):
        response = self.test_client.get(self.observe_session_url)
    
        self.assertEqual(response.status_code, 200, "Going to Observe Session page should return a Status Code of 200 (OK)")
        self.assertTemplateUsed(response, "hippo/observeSession.html", "Observe Session page should use the observeSession.html template")

    def test_get_observe_session_no_session(self):
        response = self.test_client.get(reverse('observeSession', args=[666]))
    
        self.assertEqual(response.status_code, 404, "Going to Observe Session page with a non-existant session should return a Status Code of 404")

    def test_get_generate_chart(self):
        # Needed to add some skill scores for this to work
        response = self.test_client.get(self.generate_chart_url)
    
        self.assertEqual(response.status_code, 200, "Going to Generate Chart page should return a Status Code of 200 (OK)")
        self.assertTemplateUsed(response, "hippo/generateChart.html", "Generate Chart page should use the generateChart.html template")

    def test_get_generate_chart_no_course(self):
        # Needed to add some skill scores for this to work
        response = self.test_client.get(reverse('generateChart', args=[666]))
    
        self.assertEqual(response.status_code, 404, "Going to Generate Chart page with a non-existant course should return a Status Code of 404")

    def test_get_choose_course_client_only(self):
        response = self.test_client.get(self.choose_course_client)
    
        self.assertEqual(response.status_code, 200, "Going to Choose Course page should return a Status Code of 200 (OK)")
        self.assertTemplateUsed(response, "hippo/chooseCourse.html", "Choose Course page should use the chooseCourse.html template")

    def test_get_choose_course_no_client(self):
        response = self.test_client.get(reverse('chooseCourse', args=[666]))
    
        self.assertEqual(response.status_code, 404, "Going to Choose Course page with a non-existant client should return a Status Code of 404")

    def test_get_new_course(self):
        response = self.test_client.get(self.new_course)
    
        self.assertEqual(response.status_code, 200, "Going to New Course page should return a Status Code of 200 (OK)")
        self.assertTemplateUsed(response, "hippo/newCourse.html", "New Course page should use the newCourse.html template")


# class ObservationsTest(TestCase):
#     # databases = {'test', 'default'}
#
#     def setUp(self):
#         #Create a session
#         test_date = date.today()
#         hat = Hat.objects.create(size='10')
#         diagnosis = Diagnosis.objects.create(diagnosis='Messed up')
#         client = Client.objects.create(first_name='Sir', last_name='Test', gender='M', date_of_birth=test_date, hat_size=hat)
#         course = Course.objects.create(client=client)
#         horse = Horse.objects.create(horse_name='Red Rum')
#         self.session = Session.objects.create(course=course, week_number=1, session_date=test_date, horse=horse)
#
#         # Create some skills
#         self.function = Function.objects.create(function_name='Test Function')
#         self.basket_weaving = Skill.objects.create(skill_name="Basket Weaving", function=self.function)
#         self.flower_arranging = Skill.objects.create(skill_name="Flower Arranging", function=self.function)
#         self.embroidery = Skill.objects.create(skill_name="Embroidery", function=self.function)

    # @classmethod
    # def setUpTestData(cls):
    #     """
    #     https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing#views
    #     """
    #     # Create some skills
    #     function = Function.objects.create(function_name='Test Function2')
    #     # basket_weaving = Skill.objects.create(skill_name="Basket Weaving", function=function)
    #     # flower_arranging = Skill.objects.create(skill_name="Flower Arranging", function=function)
    #     # embroidery = Skill.objects.create(skill_name="Embroidery", function=function)
    #     Skill.objects.create(skill_name="Basket Weaving2", function=function)
    #     Skill.objects.create(skill_name="Flower Arranging2", function=function)
    #     Skill.objects.create(skill_name="Embroidery2", function=function)
        
    # def test_score_observations(self):
    #     # Post a new Observation via the form on the '/observeSession/<session>' route
    #     """
    #     To test the HTTP responses of the views
    #     we can use a built-in HTTP client that comes with the Django testing framework.
    #     """
    #     response = self.client.post(f"/observeSession/{self.session.id}/", {"score1": "1", "score2": "3", "score3": "5"})
    #
    #     basket_weaving = Skill.objects.create(skill_name="Basket Weaving3", function=self.function)
    #     flower_arranging = Skill.objects.create(skill_name="Flower Arranging3", function=self.function)
    #     embroidery = Skill.objects.create(skill_name="Embroidery3", function=self.function)
    #
    #     """
    #     If the observation scores have been saved successfully:
    #     The view should redirect back to 'VIEW CHARTS' but for now the home page.
    #     Use assertRedirects() to confirm that it redirects back to slash.
    #     """
    #     '''
    #     Does not work because the form posts back to /observeSession/<session_id>/
    #     And it is this redirection that 'assertRedirects' detects instead of
    #     the final destination of the page
    #     '''
    #     # 302 status means redirect
    #     self.assertRedirects(response, f'/observeSession/{self.session.id}/', status_code=302)
    #     """
    #     Just to prove that the observation scores have been saved.
    #     Try to get them from the database using .filter() and passing it the session ID
    #     Since these scores are the only ones on the database for that session
    #     We can be certain the view works by asserting that the length of existing scores
    #     equals the number of scores we added in the test.
    #     """
    #     observation_scores = SkillScore.objects.filter(session=self.session.id).order_by("score")
    #
    #     self.assertEqual(observation_scores.count(), 3, f"There should be 3 observation scores for session : {self.session.id}")
    #     # self.assertEqual(len(observation_scores), 3, f"There should be 3 observation scores for session : {self.session.id}")
    #     first_score = observation_scores[0]
    #     second_score = observation_scores[1]
    #     third_score = observation_scores[2]
    #
    #     self.assertEqual(1, first_score.score, "First score should be 1")
    #     self.assertEqual(3, second_score.score, "First score should be 3")
    #     self.assertEqual(5, third_score.score, "First score should be 5")
