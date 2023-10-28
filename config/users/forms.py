from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class NewUserForm(UserCreationForm):
    email = forms.EmailField(
                             widget=forms.EmailInput(
                                 attrs={"class": "focus:outline-none", "placeholder": "mail@mail.com"})
                             )
    username = forms.CharField(
                               widget=forms.TextInput(
                                   attrs={"class": "focus:outline-none", "placeholder": "Enter username"})
                               )
    password1 = forms.CharField(
                                widget=forms.NumberInput(
                                    attrs={"class": "focus:outline-none", "placeholder": "Enter password 1"})
                                )
    password2 = forms.CharField(
                                widget=forms.NumberInput(
                                    attrs={"class": "focus:outline-none", "placeholder": "Enter password 2"})
                                )


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


    # def save(self, commit=True):#форма для сохранения user
    #     user = super(NewUserForm, self).save(commit=False)
    #     user.email = self.cleaned_data['email']
    #     if commit:
    #         user.save()
    #     return user
    #

