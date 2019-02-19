from django import forms
from django.contrib.auth.models import User


class Formname(forms.Form):
    user = forms.CharField(max_length = 100,label="Season")
    password = forms.CharField(max_length=100,label="District")
    text=forms.CharField(max_length=100,label="Soil Type",)
