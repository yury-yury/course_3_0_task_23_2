from django import forms

from catalog.models import Product, Version


class StyleMixinForm:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name not in ['active', ]:
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-check-input'


class ProductForm(StyleMixinForm, forms.ModelForm):
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


class VersionForm(StyleMixinForm, forms.ModelForm):

    class Meta:
        model = Version
        fields = ('num_version', 'title_version', 'active')


    # def clean_active(self):
    #     cleaned_data = self.cleaned_data.get('active')
    #     print(cleaned_data)
    #
    #     if cleaned_data == True:
    #         inst_list = Version.objects.filter(product=) #.filter(active=True)
    #         print(self.cleaned_data.get('product'))
    #         print(len(inst_list))
    #         if len(inst_list) > 0:
    #             raise forms.ValidationError('Только одна версия товара может быть отмечена как текущая')
    #
    #     return cleaned_data
