from django import forms
from .models import Fornecedor
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

class FornecedorForm(forms.ModelForm):

    cnpj = forms.RegexField(
        regex=r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$',
        error_messages={'invalid': 'Digite um CNPJ no formato 00.000.000/0000-00.'},
        widget=forms.TextInput(attrs={'placeholder': '00.000.000/0000-00'})
    )



    class Meta:
        model = Fornecedor
        fields = '__all__'
        widgets = {
            'cnpj': forms.TextInput(attrs={'class': 'css-input', 'id': 'cnpj'}),
            'categoria': forms.TextInput(attrs={'class': 'css-input', 'id': 'categoria'}),
            'empresa': forms.TextInput(attrs={'class': 'css-input', 'id': 'empresa'}),
            'endereco': forms.TextInput(attrs={'class': 'css-input', 'id': 'endereco'}),
            'cep': forms.TextInput(attrs={'class': 'css-input', 'id': 'cep'}),
            'email': forms.TextInput(attrs={'class': 'css-input', 'id': 'email'}),
            'contato': forms.TextInput(attrs={'class': 'css-input', 'id': 'contato'}),
            'data_pesquisa': forms.DateInput(attrs={'class': 'css-input', 'type': 'date', 'id': 'data_pesquisa'}),
            'cliente1': forms.TextInput(attrs={'class': 'css-input', 'id': 'cliente1'}),
            'cliente2': forms.TextInput(attrs={'class': 'css-input', 'id': 'cliente2'}),
            'cliente3': forms.TextInput(attrs={'class': 'css-input', 'id': 'cliente3'}),
            'tempo_atividade': forms.Select(attrs={'class': 'css-select' }),
        }

    def clean_cnpj(self):
        cnpj = self.cleaned_data.get('cnpj')
        if Fornecedor.objects.filter(cnpj=cnpj).exists():
            raise ValidationError('Ja existe um fornecedor com este CNPJ')
        return cnpj