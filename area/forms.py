from django import forms
from django.contrib.auth.models import User
from .models import *

class ProfileForm(forms.ModelForm):
    class Meta:  
        model = Profile
        fields = '__all__'