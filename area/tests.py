from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import *


# Create your tests here.

def test_home_page_status_code(self):
    url = reverse('home')
    response = self.client.get(url)
    self.assertEquals(response.status_code, 200)