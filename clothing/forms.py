from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from clothing.models import Cloth



class ClothForm(forms.ModelForm):
    """
    form for handling cloth creation and update
    """
    class Meta:
        model = Cloth
        fields = [
                    'name', 
                    'size', 
                    'price', 
                    'material_type', 
                    'image', 
                    'available_stock', 
                    'description'
        ]

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
                    max_length=40, 
                    required=False, 
                    help_text="Enter First Name"
    )

    last_name = forms.CharField(
                    max_length=40, 
                    required=False, 
                    help_text="Enter Last Name"
    )

    email = forms.EmailField(
                    max_length=225, 
                    required=True, 
                    help_text="Enter your Email"
    )

    class Meta:
        model = User
        fields = (
                    'username', 
                    'first_name', 
                    'last_name', 
                    'email', 
                    'password1', 
                    'password2'
        )
    