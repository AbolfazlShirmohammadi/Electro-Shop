from django import forms
from .models import Product  
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category','brand', 'price','wattage','inputV','outV', 'description', 'image']  # فیلدهای مدل محصولت
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام محصول'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'قیمت به تومان'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'توضیحات محصول'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }


        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
               
                field.widget.attrs['class'] = 'form-control'