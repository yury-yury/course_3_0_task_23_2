from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):
    forbidden_words: list = ['казино', 'криптовалюта', 'крипта', 'биржа',
                             'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price']

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')

        for f_word in self.forbidden_words:
            if f_word in cleaned_data:
                raise forms.ValidationError('Поле название содержит запрещенные слова.')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')

        for f_word in self.forbidden_words:
            if f_word in cleaned_data:
                raise forms.ValidationError('Поле описание содержит запрещенные слова.')

        return cleaned_data
