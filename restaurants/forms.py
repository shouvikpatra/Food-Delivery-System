from django.forms import ModelForm, HiddenInput
from .models import Menu, Restaurant


class DishForm(ModelForm):
    class Meta:
        model = Menu
        fields = ['res_id', 'dish_name', 'price', 'cuisine', 'availability']
        widgets = {'res_id': HiddenInput()}


class ProfileForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'
        widgets = {'id': HiddenInput()}
