from django import forms
from django.contrib.auth.models import User
from .models import Member

class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label="Conferma Password",
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Le password non corrispondono.")
        return password2

class MemberRegistrationForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['altezza', 'peso']
