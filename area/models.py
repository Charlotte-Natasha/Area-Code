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

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()

class Post(models.Model):
    title = models.CharField(max_length=100, null=True)
    post = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='post_owner')

    def __str__(self):
        return self.title

    def save_post(self):
        self.save()

    @classmethod
    def get_post_by_id(cls, id):
        return cls.objects.filter(id=id)

    @classmethod
    def get_post_by_user(cls, user):
        return cls.objects.filter(user=user)

    @classmethod
    def get_post_by_hood(cls, hood):
        return cls.objects.filter(hood=hood)

    @classmethod
    def get_post_by_title(cls, title):
        return cls.objects.filter(title=title)

    @classmethod
    def get_post_by_post(cls, post):
        return cls.objects.filter(post=post)

    @classmethod
    def get_post_by_date(cls, date):
        return cls.objects.filter(date=date)

    def delete_post(self):
        self.delete()

    @classmethod
    def get_posts_by_neighborhood(cls, hood):
        hood_posts = cls.objects.filter(hood=hood)
        return hood_posts[::-1]        