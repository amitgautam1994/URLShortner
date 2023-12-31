from .models import ShortURL
from django import forms


class CreateNewShortURL(forms.ModelForm):
    class Meta:
        model = ShortURL
        fields = {'original_url'}

        widget = {
            'original_url': forms.TimeInput(attrs={'class': 'form-control'})
        }
