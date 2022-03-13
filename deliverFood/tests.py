from email import message
from django.urls import reverse

from deliverFood.views import contact_us
from .models import Contact_Us,Author,Book
from django.contrib.auth.models import User
from django.test import TestCase
from django.contrib.auth import authenticate

class TEstContact(TestCase):
    def test_contact(self):
        book = Book.objects.create(title="Niceone")
        philip = Author.objects.create(first_name="Aashishi", last_name="rajput")
        juliana = Author.objects.create(first_name="Rajes", last_name="rai")
        book.authors.set([philip.pk, juliana.pk])
        self.assertEqual(book.authors.count(), 2)

    def test_model_str(self):
        book = Book.objects.create(title="The papa")
        philip = Author.objects.create(first_name="Philip", last_name="K. Dick")
        self.assertEqual(str(book), "The papa")
        self.assertEqual(str(philip), "Philip")

    
    

class SigninTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test', password='12test12', email='test@example.com')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(username='test',password='12test12')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='12test12')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_pssword(self):
        user = authenticate(username='test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)


class Text(TestCase):
        def test_can_send_message(self):
            data = {
                "user_name": "Juliana",
                "user_email": " Crain",
                "subject": "Would love to talk about Philip K. Dick",
                "message":"asdasdasdsad"
            }
            response = self.client.get(reverse("contact_us"))
            self.assertTemplateUsed(response, "contact_us.html")
           
            response = self.client.post(reverse("contact_us"), data=data)
            self.assertEqual(contact_us.objects.count(), 1)
