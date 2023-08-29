from django import forms
from django.forms import ModelForm, TextInput, EmailInput

from .models import Round


class RoundForm(ModelForm):
    class Meta:
        model = Round
        # fields = '__all__'
        fields = ['num_players', 'non_exclusions']

# class RoundForm(ModelForm):
#     class Meta:
#         model = Round
#         fields = ['num_players', 'non_exclusions']
#         widgets = {
#             'Number of Players': TextInput(attrs={
#                 'class': "form-control",
#                 'style': 'max-width: 300px;',
#                 'placeholder': 'Number of Players'
#                 }),
#             'Non-exclusions': TextInput(attrs={
#                 'class': "form-control",
#                 'style': 'max-width: 300px;',
#                 'placeholder': 'Non-exclusions'
#                 })
#         }