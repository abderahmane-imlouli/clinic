# core/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Patient

class PatientSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'patient'  # تعيين الدور للمريض
        if commit:
            user.save()
        # إنشاء سجل Patient عند التسجيل
        Patient.objects.create(user=user)
        return user
