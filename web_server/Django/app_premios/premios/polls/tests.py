import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question


# Create your tests here.
class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_questions(self):
        '''was_published_recently returns False for questions whose pub_date is in the future'''
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text="¿Quien es el mejor super heroe de marvel?", pub_date = time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_pass_questions(self):
        '''was_published_recently returns False for questions whose pub_date is in the future'''
        time = timezone.now() - datetime.timedelta(days=30)
        future_question = Question(question_text="¿Quien es el mejor super heroe de marvel?", pub_date = time)
        self.assertIs(future_question.was_published_recently(), False)


    def test_was_published_recently_with_today_questions(self):
        '''was_published_recently returns False for questions whose pub_date is in the future'''
        time = timezone.now() + datetime.timedelta(days=0)
        future_question = Question(question_text="¿Quien es el mejor super heroe de marvel?", pub_date = time)
        self.assertIs(future_question.was_published_recently(), True)

def create_question(question_text, days):
    '''create a question with the given "question_text" and publish the given number of days offset
    to now (negative for question published in the past, positive for questions that have yet 
    to be published)
    '''
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)
    

class QuestionIndexViewTest(TestCase):

    def test_no_question(self):
        """If no question exist, an appopiate message is displayed"""
        response = self.client.get(reverse("polls:index"))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context['lastest_question_list'],[])

    def test_no_question_when_exist_future_question(self):
        """If no question exist, an appopiate message is displayed"""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text="¿Quien es el mejor super heroe de marvel?", pub_date = time)
        
        response = self.client.get(reverse("polls:index"))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context['lastest_question_list'],[])

    def test_future_question(self):
        '''question with a pub_date in the future aren't displayed on the index page.'''
        create_question("future qeustion", 10)
        response = self.client.get(reverse("polls:index"))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context['lastest_question_list'],[])

    def test_past_question(self):
        '''question with a pub_date in the past are displayed on the index page.'''
        question = create_question("future qeustion", -10)
        response = self.client.get(reverse("polls:index"))
        self.assertEquals(response.status_code, 200)
        self.assertNotContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context['lastest_question_list'],[question])

    def test_future_question_and_past_question(self):
        '''Even if both past and future question exists, only past question are displayed'''
        past_question = create_question("past question", -30)
        future_question = create_question("furute question", 30)
        response = self.client.get(reverse("polls:index"))
        self.assertEquals(response.status_code, 200)
        self.assertNotContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context['lastest_question_list'],[past_question])

    def test_two_past_question(self):
        '''The question index page may display multiple questions.'''
        past_question = create_question("past question", -30)
        past_question2 = create_question("past question2", -40)
        response = self.client.get(reverse("polls:index"))
        self.assertEquals(response.status_code, 200)
        self.assertNotContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context['lastest_question_list'],[past_question,past_question2])

    def test_two_future_question(self):
        '''The question index page may not display multiple questions.'''
        create_question("future question", 30)
        create_question("future question2", 40)
        response = self.client.get(reverse("polls:index"))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context['lastest_question_list'],[])

class QuestionDetailsViewTest(TestCase):

    def test_furute_question(self):
        '''The detail view of a question with a pub_date in the future return a 404 error not found'''
        future_question = create_question("future question", 30)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        '''The detail view of a question with a pub_date in the pass displays the question's test'''
        past_question = create_question("past question", -30)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, past_question.question_text)
