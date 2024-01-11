import requests
from django import forms
from .models import Fornecedor
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, URLValidator, EmailValidator
from requests.exceptions import RequestException

def validar_cnpj_api(cnpj):
    try:
        cnpj_limpo = cnpj.replace('.', '').replace('/', '').replace('-', '')
        response = requests.get(f"https://www.receitaws.com.br/v1/cnpj/{cnpj_limpo}")
        if response.status_code == 200:
            data = response.json()
            if not data['status'] == 'OK':
                raise ValidationError('CNPJ inválido ou não existe.')
        else:
            raise ValidationError('Erro ao validar CNPJ.')
    except RequestException:
        raise ValidationError('Erro ao conectar com o serviço de validação de CNPJ.')


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
            'email': forms.TextInput(attrs={'class': 'css-input', 'id': 'email', 'placeholder': 'email@exemplo.com.br'}),
            'site': forms.TextInput(attrs={'class': 'css-input', 'id': 'site'}),
            'contato': forms.TextInput(attrs={'class': 'css-input', 'id': 'contato'}),
            'data_pesquisa': forms.DateInput(attrs={'class': 'css-input', 'type': 'date', 'id': 'data_pesquisa'}),
            'cliente1': forms.TextInput(attrs={'class': 'css-input', 'id': 'cliente1'}),
            'cliente2': forms.TextInput(attrs={'class': 'css-input', 'id': 'cliente2'}),
            'cliente3': forms.TextInput(attrs={'class': 'css-input', 'id': 'cliente3'}),
            'tempo_atividade': forms.Select(attrs={'class': 'css-select' }),
        }


    

    def clean_cnpj(self):
        cnpj = self.cleaned_data.get('cnpj')
        validar_cnpj_api(cnpj)
        if Fornecedor.objects.filter(cnpj=cnpj).exists():
            raise ValidationError('Ja existe um fornecedor com este CNPJ')
        return cnpj
    
    def clean_site(self):
        site = self.cleaned_data.get('site')
        if site:  # Verifica se o campo não está vazio
            validate = URLValidator()
            try:
                validate(site)
            except ValidationError:
                raise ValidationError('Por favor, insira um URL válido. Exemplo: http://www.exemplo.com.br')
        return site
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:  # Verifica se o campo não está vazio
            validate = EmailValidator()
            try:
                validate(email)
            except ValidationError:
                raise ValidationError('Por favor, insira um EMAIL válido. Exemplo: email@exemplo.com.br')
        return email