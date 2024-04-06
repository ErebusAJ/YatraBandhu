from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, TravelPlan, Category

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
        ('0-5k', 5000.00),
        ('5-10k', 10000.00),
        ('10-20k', 20000.00),
        ('20k & above', 30000.00),
    ]

    Location = [
        ('Gujrat', 'Gujrat'),
        ('West Bengal','West Bengal'),
        ('Jammu','Jammu'),
        ('Karnatka','Karnatka'),
    ]

    categories = forms.MultipleChoiceField(choices=CATEGORIES_CHOICES, widget=forms.CheckboxSelectMultiple)
    price = forms.ChoiceField(choices=Prices)
    location = forms.ChoiceField(choices=Location)
    class Meta:
        model = TravelPlan
        fields = ['location', 'price', 'date_from', 'date_to', 'additional_info', 'categories']
        widgets = {
            'date_from': forms.DateInput(attrs={'type': 'date'}),
            'date_to': forms.DateInput(attrs={'type': 'date'}),
        }

        def __init__(self, *args, **kwargs):
            super(TravelPlanForm, self).__init__(*args, **kwargs)
            self.fields['categories'].queryset = Category.objects.all()