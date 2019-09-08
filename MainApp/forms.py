from django import forms
from .models import *
from django.core.exceptions import ValidationError


class PostScore(forms.ModelForm):
    class Meta:
        model = Throw
        fields = ['player', 'throw_code', 'throw_k', 'throw_v', 'game', 'set', 'leg']
        widgets = {
            'player': forms.TextInput(attrs={'class': 'form-control'}),
            'throw_code': forms.TextInput(attrs={'class': 'form-control'}),
            'throw_k': forms.TextInput(attrs={'class': 'form-control'}),
            'throw_v': forms.TextInput(attrs={'class': 'form-control'}),
            'game': forms.TextInput(attrs={'class': 'form-control'}),
            'set': forms.TextInput(attrs={'class': 'form-control'}),
            'leg': forms.TextInput(attrs={'class': 'form-control'}),
        }
