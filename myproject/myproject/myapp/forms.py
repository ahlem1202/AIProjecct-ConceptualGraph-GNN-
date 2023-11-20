# forms.py
from django import forms

class WordSearchForm(forms.Form):
    search_word = forms.CharField(label='Enter a word', max_length=255)
