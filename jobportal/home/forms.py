from django import forms
from .models import Userreg

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Userreg
        fields = '__all__'
        exclude = ['user']  # important if using OneToOneField(User)