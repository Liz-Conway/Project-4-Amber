'''
Created on 14 May 2022

@author: liz
'''
from django.test import TestCase
from hippotherapy.models import Session, Skill, SkillScore, Course, Client, Hat,\
    Function
from datetime import date
from administration.models import Diagnosis, Horse

class ObservationsTest(TestCase):
    
    def setUp(self):
        #Create a session
        test_date = date.today()
        hat = Hat.objects.create(size='10')
        diagnosis = Diagnosis.objects.create(diagnosis='Messed up')
        client = Client.objects.create(first_name='Sir', last_name='Test', gender='M', date_of_birth=test_date, hat_size=hat)
        course = Course.objects.create(client=client)
        horse = Horse.objects.create(horse_name='Red Rum')
        self.session = Session.objects.create(course=course, week_number=1, session_date=test_date, horse=horse)

    @classmethod
    def setUpTestData(cls):
        """
        https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing#views
        """
        # Create some skills
        function = Function.objects.create(function_name='Test Function')
        # basket_weaving = Skill.objects.create(skill_name="Basket Weaving", function=function)
        # flower_arranging = Skill.objects.create(skill_name="Flower Arranging", function=function)
        # embroidery = Skill.objects.create(skill_name="Embroidery", function=function)
        Skill.objects.create(skill_name="Basket Weaving", function=function)
        Skill.objects.create(skill_name="Flower Arranging", function=function)
        Skill.objects.create(skill_name="Embroidery", function=function)
        
    def test_score_observations(self):
        # Post a new Observation via the form on the '/observeSession/<session>' route
        """
        To test the HTTP responses of the views
        we can use a built-in HTTP client that comes with the Django testing framework.
        """
        response = self.client.post(f"/observeSession/{self.session.id}/", {"score1": "1", "score2": "3", "score3": "5"})
        
        """
        If the observation scores have been saved successfully:
        The view should redirect back to 'VIEW CHARTS' but for now the home page.
        Use assertRedirects() to confirm that it redirects back to slash.
        """
        '''
        Does not work because the form posts back to /observeSession/<session_id>/
        And it is this redirection that 'assertRedirects' detects instead of
        the final destination of the page
        '''
        self.assertRedirects(response, f'/observeSession/{self.session.id}/', status_code=301)
        """
        Just to prove that the observation scores have been saved.
        Try to get them from the database using .filter() and passing it the session ID
        Since these scores are the only ones on the database for that session
        We can be certain the view works by asserting that the length of existing scores
        equals the number of scores we added in the test.
        """
        observation_scores = SkillScore.objects.filter(session=self.session.id).order_by("score")
        self.assertEqual(len(observation_scores), 3, f"There should be 3 observation scores for session : {self.session.id}")
        first_score = observation_scores[0]
        second_score = observation_scores[1]
        third_score = observation_scores[2]
        
        self.assertEqual(1, first_score.score, "First score should be 1")
        self.assertEqual(3, second_score.score, "First score should be 3")
        self.assertEqual(5, third_score.score, "First score should be 5")
