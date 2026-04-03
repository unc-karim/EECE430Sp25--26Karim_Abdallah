from django import forms
from .models import Player

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'dateJoined', 'position', 'salary_payment', 'contactPerson']
        labels = {
            'name': 'Name',
            'dateJoined': 'Date Joined',
            'position': 'Position',
            'salary_payment': 'Salary / Payment',
            'contactPerson': 'Contact Person',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'e.g. Maria Haddad'}),
            'dateJoined': forms.DateInput(attrs={'type': 'date'}),
            'position': forms.TextInput(attrs={'placeholder': 'e.g. Setter'}),
            'salary_payment': forms.NumberInput(attrs={'step': '0.01', 'placeholder': 'e.g. 3200.00'}),
            'contactPerson': forms.TextInput(attrs={'placeholder': 'e.g. Mother'}),
        }
