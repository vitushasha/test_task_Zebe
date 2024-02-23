from django import forms
from .models import Client
from django.core.validators import RegexValidator

class Order(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Order, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Имя'
        self.fields['phone'].label = 'Телефон'
        self.fields['phone'].validators = [
            RegexValidator(regex='^\+7\(\d{3}\)\d{3}-\d{2}-\d{2}$', message="формат: +7(123)456-78-91",
                       code='invalid_format')]
        self.fields['phone'].initial = '+7(777)777-77-77'
        self.fields['hidden_field'].widget = forms.HiddenInput()
        self.fields['hidden_field'].initial = 'test'
    class Meta:
        model = Client
        fields = ['name', 'phone', 'hidden_field']