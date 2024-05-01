from django.contrib.auth import forms, get_user_model

from .models import CustomUser


class CustomUserCreationForm(forms.UserCreationForm):
    class Meta:
        model: get_user_model()
        fields = ('username', 'email')


class CustomUserChangeForm(forms.UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email')
