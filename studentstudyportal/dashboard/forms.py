from dataclasses import field
from datetime import date, datetime
from xmlrpc.client import DateTime
from django.forms import  DateTimeInput, Widget
from django import forms
from . models import *

class NotesForm(forms.ModelForm):
    class Meta:
        model=Notes
        fields=["title","description"]

class DateInput(forms.DateInput):
    input_type='date'

class HomeworkForm(forms.ModelForm):
    class Meta:
        model=Homework
        Widgets={'due':date}
        fields=["subject","title","description","due","is_finished"]