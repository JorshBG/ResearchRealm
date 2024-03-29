from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from ScholarStack.models import Thesis


class SignUpForm(UserCreationForm):

    username = forms.CharField(max_length=20, help_text='One word used to identify this user.', required=True)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address', required=True)
    first_name = forms.CharField(max_length=30, help_text='Required. Max: 30 characters.', required=True)
    last_name = forms.CharField(max_length=30, help_text='Required. Max: 30 characters.', required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


class ThesisCreationForm(forms.ModelForm):

    title = forms.CharField(max_length=50, required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)
    content = forms.FileField(help_text='Upload a file for your thesis.', required=True, widget=forms.ClearableFileInput(attrs={'multiple': False}))
    user = forms.ModelChoiceField(queryset=User.objects.all(), required=True, label='Author')

    class Meta:
        model = Thesis
        fields = ('title', 'description', 'user', 'content')
