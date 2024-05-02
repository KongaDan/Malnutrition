from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class ProvinceForm(forms.ModelForm):
    class Meta:
        model = Province
        fields = ['nom_province']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nom_province'].widget.attrs.update({'class':'form-control',})

class ZoneSanitaireForm(forms.ModelForm):
    class Meta:
        model = ZoneSanitaire
        fields = ['nom_zone', 'address','code_province']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nom_zone'].widget.attrs.update({'class':'form-control',})
        self.fields['address'].widget.attrs.update({'class':'form-control',})
        self.fields['code_province'].widget.attrs.update({'class':'form-control',})

class AireSanitaireForm(forms.ModelForm):
    class Meta:
        model = AireSanitaire
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nom_aire'].widget.attrs.update({'class':'form-control',})
        self.fields['address'].widget.attrs.update({'class':'form-control',})
        self.fields['code_zone'].widget.attrs.update({'class':'form-control',})

