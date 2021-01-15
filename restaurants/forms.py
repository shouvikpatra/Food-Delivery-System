from django.forms import ModelForm
from .models import Menu


class DishForm(ModelForm):
    class Meta:
        model = Menu
        fields = ['dish_name', 'price', 'cuisine', 'availability']
