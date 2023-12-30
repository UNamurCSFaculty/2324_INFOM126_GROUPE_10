from django.test import TestCase, Client
from django.urls import reverse
from myapp.models import Message

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.add_message = reverse("add_message")
        self.update_message = reverse("modifier_message", args=[2])
        self.remove_message = reverse("supprimer_message", args=[2])
        
        self.message = Message.objects.create(
            content="hello world"
        )
        self.message = Message.objects.create(
            content="hello universe"
        )
        self.message = Message.objects.create(
            content="hello tutur"
        )

    def test_add_message_POST(self):
        response = self.client.post(self.add_message, {
            "content": "hello test"
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Message.objects.first().content, "hello world")
        self.assertEquals(Message.objects.last().content, "hello test")
    
    def test_update_message_POST(self):
        response = self.client.post(self.update_message, {
            "content": "hello planet"
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Message.objects.first().content, "hello world")
        self.assertEquals(Message.objects.all()[1].content, "hello planet")

    def test_delete_message_POST(self):
        response = self.client.post(self.remove_message)

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Message.objects.first().content, "hello world")
        self.assertEquals(Message.objects.last().content, "hello tutur")
