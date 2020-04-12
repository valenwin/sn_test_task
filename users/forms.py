from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from pyhunter import PyHunter

from .models import User
from .utils import clearbit_signup

hunter = PyHunter(settings.EMAIL_HUNTER_API_KEY)


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        response = hunter.email_verifier(email)
        if response['result'] == 'undeliverable':
            raise forms.ValidationError('Email does not exist.')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = True
        user.name = clearbit_signup(user.email)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
