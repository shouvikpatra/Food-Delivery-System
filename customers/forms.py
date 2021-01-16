from django.forms import ModelForm, HiddenInput
from .models import *


class ProfileForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {'id': HiddenInput()}
