from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.db import transaction

class ExpenseUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=User
        # fields='__all__'
        fields=["username","email","contact","password1","password2"]


    @transaction.atomic
    def save(self, commit=True):
        user=super().save(commit=False)
        user.is_user=True
        if commit:
            user.save()
        return user

    
    
