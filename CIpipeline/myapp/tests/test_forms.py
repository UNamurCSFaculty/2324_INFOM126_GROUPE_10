from django.test import TestCase
from myapp.forms import MessageForm

class TestForms(TestCase):
    def test_forms(self):
        form = MessageForm(data={
            'model' : 'test1',
            'fields' : 'test2'
        })

       
    
    def test_form_assert(self):
        form = MessageForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)