from django.db import models

class Fornecedor(models.Model):
    cnpj = models.CharField(max_length=18, unique=True)
    categoria = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    cep = models.CharField(max_length=9)
    email = models.EmailField()
    contato = models.CharField(max_length=20)
    data_pesquisa = models.DateField()
    cliente1 = models.CharField(max_length=100)
    cliente2 = models.CharField(max_length=100)
    cliente3 = models.CharField(max_length=100)
    TEMPO_ATIVIDADE_CHOICES = [
        ('Selecione', 'Selecione'),
        ('até 2 anos', 'até 2 anos'),
        ('02 à 05 anos', '02 à 05 anos'),
        ('05 à 10 anos', '05 à 10 anos'),
        ('+10 anos', '+10 anos'),
    ]

    tempo_atividade = models.CharField(
        max_length=100,
        choices=TEMPO_ATIVIDADE_CHOICES,
        default='Selecione'
    )

    def __str__(self):
        return self.empresa
    
