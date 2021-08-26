from django import forms
from . import models


class AddTask(forms.ModelForm):
    """docstring for AddTask."""

    class Meta:
        model = models.Task
        fields = ('title', 'description', 'image')


class UpdateTask(forms.ModelForm):
    """docstring for AddTask."""

    class Meta:
        model = models.Task
        fields = ('title', 'description', 'is_complete', 'image')
