from django import forms
from clothing.models import Cloth

class ClothCreationForm(forms.ModelForm):
    
    class Meta:
        model = Cloth
        fields = ['name', 'size', 'price', 'material_type', 'image', 'colour', 'amount']