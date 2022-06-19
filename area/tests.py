from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import *


# Create your tests here.

def test_home_page_status_code(self):
    url = reverse('home')
    response = self.client.get(url)
    self.assertEquals(response.status_code, 200)

class NeighborhoodTestCase(TestCase):
    def setUp(self):
        self.user = User(username='hood', password='tashapassword')
        self.user.save()
        self.profile = Profile(id=15, user=self.user, )
        # self.profile.create_profile()
        self.neighborhood = Neighborhood(name='Test Neighborhood', location='Test Location', population=0,
                                        description='Test Description', hood_logo='Test Image', admin=self.profile )
        # self.neighborhood.save()

    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()
        Neighborhood.objects.all().delete()
        self.user.delete()    