from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'running_time', 'actors', 'director', 'release_date']
        widgets = {
            'running_time': forms.TimeInput(),
            'release_date': forms.DateInput()
        }