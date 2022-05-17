from django.test import TestCase
from typing import Dict
from django.urls import resolve, reverse
from .models import IdeaModel
from .forms import IdeaForm
from .views import create, table

# Create your tests here.

#1. test model(s)
#1.1 do setUp so it will run before each test group

class IdeaTestCase(TestCase):
    def setUp(self):
        self.idea = IdeaModel()
        self.idea.idea_title = 'test idea'
        self.idea.idea_description = 'my test description'
        self.idea.save()

#1.2 need to test the constructor, title, and model
    def test_IdeaModel_constructor(self):
        idea_zero = IdeaModel()
        self.assertIsNot(idea_zero)

    def test_IdeaModel_idea_title(self):
        self.assertEquals('test idea', self.idea.idea_title)

    def test_IdeaModel_idea_description(self):
        self.assertEquals('my test description', self.idea.idea_description)


#2. test views
class PresentationLayerTestCase(TestCase):
    def setUp(self):
        self.idea = IdeaModel()
        self.idea.idea_title = 'test idea'
        self.idea.idea_description = 'my test description'
        self.idea.save()

    def test_homepage(self):
        response = self.client.get('/')
        self.assertTemplateNotUsed(response, 'crud/update.html')

    def test_homepage_uses_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'crud/table.html')

    def test_update_uses_correct_template(self):
        response = self.client.get('/update.html')
        self.assertTemplateUsed(response, 'crud/update.html')

    def test_delete_uses_correct_template(self):
        response = self.client.get('/delete')
        self.assertTemplateUsed(response, 'crud/delete.html')

    def test_create_uses_correct_template(self):
        response = self.client.get('/create')
        self.assertTemplateUsed(response, 'crud/create.html')


# 3. test urls
class UrlTestCase(TestCase):
    def setUp(self):
        self.idea = IdeaModel()
        self.idea.idea_title = 'test idea'
        self.idea.idea_description = 'my test description'
        self.idea.save()

    def test_url_exists(self):
        response = self.client.get('/create')
        self.assertEquals(response.status_code, 200)

    def test_url_accessibility_by_name(self):
        response = self.client.get(reverse('create'))
        self.assertEquals(response.status_code, 200)

    def test_correct_url_by_name(self):
        response = self.client.get(reverse('table'))
        self.assertNotEquals(response.status_code, 404)

    def test_CreatePage(self):
        url = reverse('create')
        print("Resolve : ", resolve(url))
        self.assertEquals(resolve(url).func, create)


# 4. test forms
class IdeaFormTestCase(TestCase):
    def setUp(self):
        self.idea = IdeaModel()
        self.idea.idea_title = 'test idea'
        self.idea.idea_description = 'my test description'
        self.idea.save()
        self.invalid_data: dict[str, str] = {
            'idea_title': 'We are on a train, where we are headed we do not care, we are on a train speeding from the station heading away from London and here',
            'idea_description': 'to nowhere'
        }
        self.valid_data = {'idea_title': 'Kitties', 'idea_description': '1234'}

    def test_is_invalid(self):
        form = IdeaForm(data=self.invalid_data)
        self.assertFalse(form.is_valid())

    def test_form_is_valid(self):
        form = IdeaForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_empty_form(self):
        form = IdeaForm()
        self.assertIn('idea_title', form.fields)
        self.assertIn('idea_description', form.fields)

