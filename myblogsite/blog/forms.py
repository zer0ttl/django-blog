from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from . import models


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = models.User
        fields = ('username','email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = models.User
        fields = UserChangeForm.Meta.fields