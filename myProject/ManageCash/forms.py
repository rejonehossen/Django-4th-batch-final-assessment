from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name in self.fields:
            self.fields[field_name].help_text = None

class AddCashForm(forms.ModelForm):
    class Meta:
        model = AddCash
        fields = ['source', 'amount', 'description']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name in self.fields:
            self.fields[field_name].help_text = None
            
class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['description', 'amount']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name in self.fields:
            self.fields[field_name].help_text = None