from django.test import TestCase
from hippotherapy.models import Session, Skill, SkillScore, Course, Client, Hat,\
    Function
from datetime import date
from administration.models import Diagnosis, Horse


class SkillScoreTest(TestCase):
    
    def setUp(self):
        #Create a session
        test_date = date.today()
        hat = Hat.objects.create(size='10')
        diagnosis = Diagnosis.objects.create(diagnosis='Messed up')
        client = Client.objects.create(first_name='Sir', last_name='Test', gender='M', date_of_birth=test_date, hat_size=hat)
        course = Course.objects.create(client=client)
        horse = Horse.objects.create(horse_name='Red Rum')
        self.session = Session.objects.create(course=course, week_number=1, session_date=test_date, horse=horse)
        self.session2 = Session.objects.create(course=course, week_number=2, session_date=test_date, horse=horse)
        
        # Create 3 skills
        function = Function.objects.create(function_name='Test Function')
        self.basket_weaving = Skill.objects.create(skill_name="Basket Weaving", function=function)
        self.flower_arranging = Skill.objects.create(skill_name="Flower Arranging", function=function)
        self.embroidery = Skill.objects.create(skill_name="Embroidery", function=function)
        
        # Give each skill a score
        SkillScore.objects.create(session=self.session, skill=self.basket_weaving, score=1)
        SkillScore.objects.create(session=self.session, skill=self.flower_arranging, score=2)
        SkillScore.objects.create(session=self.session, skill=self.embroidery, score=5)
        # Scores for session 2
        SkillScore.objects.create(session=self.session2, skill=self.basket_weaving, score=3)
        SkillScore.objects.create(session=self.session2, skill=self.flower_arranging, score=4)
        SkillScore.objects.create(session=self.session2, skill=self.embroidery, score=2)
        
    def test_basket_weaving_scores(self):
        basket = SkillScore.objects.filter(skill=self.basket_weaving)[0]
        
        # Check the score for the basket
        self.assertEqual(1, basket.score, "Score for basket should be 1")
        
    def test_flower_arranging_score(self):
        flower = SkillScore.objects.filter(skill=self.flower_arranging)[0]
        
        # Check the score for the flower
        self.assertEqual(2, flower.score, "Score for flower should be 2")
        
    def test_embroidery_score(self):
        sewing = SkillScore.objects.filter(skill=self.embroidery)[0]
        
        # Check the score for the flower
        self.assertEqual(5, sewing.score, "Score for embroidery should be 5")
        
    def test_skill_score_is_1(self):
        score_1 = Skill.objects.filter(score_skill__score=1)
        
        # Check there is only one Skill with a score of 1
        self.assertEqual(1, score_1.count(), 'There should only be one Skill that has a score of 1')
        # Check the name of the Skill with a score of 1
        self.assertEqual('Basket Weaving', score_1[0].skill_name, 'The only Skill with a score of 1 should be Basket Weaving')
        
    def test_skill_score_is_2(self):
        score_2 = Skill.objects.filter(score_skill__score=2)
        
        # Check there is only one Skill with a score of 2
        self.assertEqual(2, score_2.count(), 'There should two Skills that have a score of 2')
        # Check the name of the Skill with a score of 2
        self.assertEqual('Flower Arranging', score_2[0].skill_name, 'The only Skill with a score of 2 should be Flower Arranging')
        
    def test_skill_score_is_5(self):
        score_5 = Skill.objects.filter(score_skill__score=5)
        
        # Check there is only one Skill with a score of 5
        self.assertEqual(1, score_5.count(), 'There should only be one Skill that has a score of 5')
        # Check the name of the Skill with a score of 5
        self.assertEqual('Embroidery', score_5[0].skill_name, 'The only Skill with a score of 5 should be Embroidery')
                
    def test_2_sessions(self):
        baskets = SkillScore.objects.filter(skill=self.basket_weaving).values('score')
        flowers = SkillScore.objects.filter(skill=self.flower_arranging).values('score')
        sewings = SkillScore.objects.filter(skill=self.embroidery).values('score')
        
        self.assertEqual([1, 3], self.make_score_list(baskets), "Basket weaving should have scores of 1 and 3")
        self.assertEqual([2, 4], self.make_score_list(flowers), "Flower Arranging should have scores of 2 and 4")
        self.assertEqual([5, 2], self.make_score_list(sewings), "Embroidery should have scores of 5 and 2")
        
        
    def make_score_list(self, scores):
        score_list = []
        for i in range(scores.count()):
            score_list.append(scores[i]["score"])
            
        return score_list