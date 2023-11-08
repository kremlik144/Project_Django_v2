from django import forms


class ProductForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput())
    name = forms.CharField(max_length=50,
                           label='Наименование товара',
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Введите наименование товара',
                                                         }))
    description = forms.CharField(max_length=250,
                                  label='Описание товара',
                                  widget=forms.Textarea(attrs={'class': 'form-control',
                                                               'placeholder': 'Описание товара',
                                                               }))
    price = forms.FloatField(min_value=0,
                             label='Стоимость товара',
                             widget=forms.NumberInput(attrs={'class': 'form-control'}))
    amount = forms.IntegerField(min_value=0,
                                label='Количество товара',
                                widget=forms.NumberInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(label='Изображение')
