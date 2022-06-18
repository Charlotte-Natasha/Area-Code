from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_picture = models.ImageField(null=True, blank=True, upload_to='profilepics')
    bio = models.TextField()
    location = models.CharField(max_length=30, default="", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()    


class Neighborhood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='hood', default=None, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='profilepics')
    description = models.TextField()

    def __str__(self):
        return self.name

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()


class Post(models.Model):
    title = models.CharField(max_length=100, null=True)
    post = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='post_owner')

    def __str__(self):
        return self.title

    def save_post(self):
        self.save()


class Business(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, related_name='business', null=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='owner')
    business_logo = models.ImageField(null=True, blank=True, upload_to='images')

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()


    def __str__(self):
        return f'{self.name} Business'