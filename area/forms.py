from django import forms
from django.contrib.auth.models import User
from .models import *
from django.forms import ModelForm

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

class AddhoodForm(ModelForm):
    # name = forms.CharField(max_length=200, label='',widget=forms.TextInput(attrs={'class': 'form-control mb-4', 'placeholder': 'name'}))
    # location =forms.CharField(max_length=200, label='',widget=forms.TextInput(attrs={'class': 'form-control mb-4','placeholder': 'location'}))
    # image = forms.FileField(max_length=200,label='',widget=forms.FileInput(attrs={'class': 'form-control mb-4', 'placeholder': 'hood image'}))
    class Meta:
        model = Neighborhood
        fields = '__all__'