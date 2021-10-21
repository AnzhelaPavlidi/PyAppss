from django import forms
from main.models import Advert


class AdvertForm(forms.ModelForm):
    class Meta:
        model = Advert
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form_control'}),
            'text': forms.Textarea(attrs={'class': 'form_control'}),
            'phone': forms.TextInput(attrs={'class': 'form_control'}),
            'email': forms.EmailInput(attrs={'class': 'form_control'}),
        }
