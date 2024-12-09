from django import forms
from django.contrib.auth.models import User
from .models import Member,CaratteristicheFisiche,ObiettivoFitness,Workout,Plan

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


from django import forms
from .models import Workout, Plan, ObiettivoFitness, CaratteristicheFisiche

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = '__all__'

class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['title', 'workouts']  # `member` può essere impostato automaticamente dalla vista

class ObiettivoFitnessForm(forms.ModelForm):
    class Meta:
        model = ObiettivoFitness
        fields = ['obiettivo','data_inizio','data_fine','note']
    def __init__(self, *args, **kwargs):
        # Riceviamo l'utente come argomento e lo rimuoviamo dai kwargs
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        # Assicuriamoci che il Member corrisponda all'utente loggato
        if not self.user:
            raise ValueError("User is required to save this form.")

        # Recuperiamo il Member associato all'utente loggato
        try:
            member = Member.objects.get(user=self.user)
        except Member.DoesNotExist:
            raise ValueError("No Member instance found for the logged-in user.")

        # Colleghiamo il Member al modello CaratteristicheFisiche
        instance = super().save(commit=False)
        instance.member = member

        if commit:
            instance.save()

        return instance

class CaratteristicheFisicheForm(forms.ModelForm):
    class Meta:
        model = CaratteristicheFisiche
        fields = ['tipo_peso']  # Mostriamo solo il campo che l'utente deve compilare

    def __init__(self, *args, **kwargs):
        # Riceviamo l'utente come argomento e lo rimuoviamo dai kwargs
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        # Assicuriamoci che il Member corrisponda all'utente loggato
        if not self.user:
            raise ValueError("User is required to save this form.")

        # Recuperiamo il Member associato all'utente loggato
        try:
            member = Member.objects.get(user=self.user)
        except Member.DoesNotExist:
            raise ValueError("No Member instance found for the logged-in user.")

        # Colleghiamo il Member al modello CaratteristicheFisiche
        instance = super().save(commit=False)
        instance.member = member

        if commit:
            instance.save()

        return instance

