from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, TravelPlan

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    # bio = forms.Textarea()
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class TravelPlanForm(forms.ModelForm):
    CATEGORIES_CHOICES = [
        ('Must See Attractions', 'Must See Attractions'),
        ('Hidden Gems', 'Hidden Gems'),
        ('Shopping', 'Shopping'),
        ('Great Food', 'Great Food'),
        ('Cultural Heritage', 'Cultural Heritage'),
        ('Art and Theater', 'Art and Theater'),
    ]

    Prices = [
        ('0-5k', '0-5k'),
        ('5-10k', '5-10k'),
        ('10-20k', '10-20k'),
        ('20k & above', '20k & above'),
    ]

    categories = forms.MultipleChoiceField(choices=CATEGORIES_CHOICES, widget=forms.CheckboxSelectMultiple)
    price = forms.ChoiceField(choices=Prices)

    class Meta:
        model = TravelPlan
        fields = ['user', 'location', 'price', 'date_from', 'date_to', 'additional_info', 'categories']
        widgets = {
            'date_from': forms.DateInput(attrs={'type': 'date'}),
            'date_to': forms.DateInput(attrs={'type': 'date'}),
        }