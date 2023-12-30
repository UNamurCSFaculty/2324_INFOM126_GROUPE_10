from django.test import TestCase
from django.db import models
from myapp.models import Message
import datetime

class TestModels(TestCase):
        def setUp(self):
                self.message1 = Message.objects.create(
                      content = 'hello world' 
                )

        def test_model(self):
                self.assertEquals(self.message1.content, 'hello world')
                