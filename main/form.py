from cProfile import label
from django.utils import timezone
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class AddData(forms.Form):
    value = forms.IntegerField(label="Indicateur", required=True)
    date = forms.DateField(widget=DateInput)
