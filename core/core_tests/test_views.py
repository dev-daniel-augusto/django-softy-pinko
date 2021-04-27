from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy
from string import ascii_letters
from random import choice, randint

letters = ascii_letters


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.object_1 = {
            "name": f"{(''.join(choice(letters) for n in range(0, randint(1, 199))))}",
            "email": f"{(''.join(choice(letters) for n in range(0, randint(1, 189))))}@gmail.com",
            "message": f"{(''.join(choice(letters) for n in range(0, randint(1, 999))))}"
        }
        self.object_2 = {
            "name": f"{(''.join(choice(letters) for n in range(0, randint(1, 199))))}",
            "email": f"{(''.join(choice(letters) for n in range(0, randint(1, 187))))}@hotmail.com",
            "message": f"{(''.join(choice(letters) for n in range(0, randint(1, 999))))}"
        }
        self.object_3 = {
            "name": f"{(''.join(choice(letters) for n in range(0, randint(1, 199))))}",
            "message": f"{(''.join(choice(letters) for n in range(0, randint(1, 999))))}"
        }
        self.object_4 = {
            "email": f"{(''.join(choice(letters) for n in range(0, randint(1, 187))))}@hotmail.com",
            "message": f"{(''.join(choice(letters) for n in range(0, randint(1, 999))))}"
        }
        self.object_5 = {
            "name": f"{(''.join(choice(letters) for n in range(0, randint(1, 199))))}",
            "email": f"{(''.join(choice(letters) for n in range(0, randint(1, 189))))}@gmail.com",
        }

    def test_form_valid(self):
        request = self.client.post(reverse_lazy('index'), data=self.object_1)
        self.assertEquals(request.status_code, 302)

        request = self.client.post(reverse_lazy('index'), data=self.object_2)
        self.assertEquals(request.status_code, 302)

    def test_form_invalid(self):
        request = self.client.post(reverse_lazy('index'), data=self.object_3)
        self.assertEquals(request.status_code, 200)

        request = self.client.post(reverse_lazy('index'), data=self.object_4)
        self.assertEquals(request.status_code, 200)

        request = self.client.post(reverse_lazy('index'), data=self.object_5)
        self.assertEquals(request.status_code, 200)
