from django import forms
from clothing.models import Cloth

class ClothForm(forms.ModelForm):
    class Meta:
        model = Cloth
        fields = ['name', 'size', 'price', 
                    'material_type', 'image', 'available_stock', 'description']