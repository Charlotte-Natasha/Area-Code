from dataclasses import fields
from django import forms
from django.contrib.auth.models import User
from .models import *

class ProfileForm(forms.ModelForm):
    class Meta:  
        model = Profile
        fields = '__all__'

class NeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        fields = '__all__'  

class NewBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = '__all__' 
        # exclude = ['Admin', 'pub_date', 'admin_profile']
        # widgets = {
        # 'address': forms.Textarea(attrs={'rows':1, 'cols':10,}),
        # }              

