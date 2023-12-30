from django.test import TestCase
from django.urls import reverse, resolve
from myapp.views import add_message, update_message, delete_message

# Create your tests here.
class MessageTestCase(TestCase):
    def test_add_message_url_is_resolved(self):
        url = reverse("add_message")
        self.assertEquals(resolve(url).func, add_message) 

    def test_update_message_url_is_resolved(self):
        url = reverse("modifier_message", args=[1])
        self.assertEquals(resolve(url).func, update_message)

    def test_delete_message_url_is_resolved(self):
        url = reverse("supprimer_message", args=[1])
        self.assertEquals(resolve(url).func, delete_message)

    