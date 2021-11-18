from django.db import models
from django.urls import reverse
from django.db.models import Q
import numpy as np

class Corretor(models.Model):
    nome = models.CharField(max_length=200)
    celular = models.CharField(max_length=200)
    creci = models.CharField(max_length=200)
    dtanasc = models.DateField(blank=True, null=True)
    cidade = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Estadoconser(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    codigo = models.CharField(max_length=1, blank=True, null=True)

    def __str__(self):
        return self.nome, self.codigo


class Nomecondominio(models.Model):
    nome = models.CharField(max_length=300)
    endereco = models.CharField(max_length=300, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    uf = models.CharField(db_column='UF', max_length=2, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("cond_edit", kwargs={"cond_pk": self.id})

    class Meta:
       ordering = ['nome']


class Padrao(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome


class Tabelarossheideck(models.Model):
    idade_em_vida = models.TextField(db_column='idade_em_vida', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    A = models.TextField(blank=True, null=True)  # Field name made lowercase.
    B = models.TextField(blank=True, null=True)  # Field name made lowercase.
    C = models.TextField(blank=True, null=True)  # Field name made lowercase.
    D = models.TextField(blank=True, null=True)  # Field name made lowercase.
    E = models.TextField(blank=True, null=True)  # Field name made lowercase.
    F = models.TextField(blank=True, null=True)  # Field name made lowercase.
    G = models.TextField(blank=True, null=True)  # Field name made lowercase.
    H = models.TextField(blank=True, null=True)  # Field name made lowercase.

    def retorna_id(vidautil):
        retorna = Tabelarossheideck.objects.get(idade_em_vida=vidautil)
        return retorna.id

class Tipo(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
       ordering = ['nome']

class Vidautil(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    idadevidautil = models.IntegerField(db_column='idadeVidaUtil', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.nome


status_choices = (
        ('1', 'Oferta'),
        ('2', 'Vendido')
    )

class Imovel(models.Model):
    valordevenda = models.DecimalField(db_column='valorDeVenda', max_digits=10, decimal_places=2, blank=False, null=False, default=0, verbose_name='Valor de venda')  # Field name made lowercase.
    nomecondominio = models.ForeignKey(Nomecondominio, on_delete=models.CASCADE,  blank=True, null=True, verbose_name='Condominio')
    idade = models.IntegerField(blank=True)
    bairro = models.CharField(max_length=100, blank=True)
    cidade = models.CharField(max_length=200, blank=True)
    aconstruida = models.DecimalField(blank=False, null=False, default=0, max_digits=10, decimal_places=2,  verbose_name='Área Construída/Útil')
    atotal = models.DecimalField(blank=False, null=False, default=0, max_digits=10, decimal_places=2, verbose_name='Área Total')
    dtacadastro = models.DateField(db_column='dtaCadastro', blank=True, null=True, verbose_name='Data de cadastro')  # Field name made lowercase.
    status = models.CharField(max_length=1, choices=status_choices)
    padrao = models.ForeignKey(Padrao, on_delete=models.CASCADE, blank=True)
    estadoconser = models.ForeignKey(Estadoconser, on_delete=models.CASCADE, blank=True, verbose_name='Estado de Conservação')  # Field name made lowercase.
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, blank=True)
    corretor = models.ForeignKey(Corretor, on_delete=models.CASCADE, blank=True)
    vidautil = models.ForeignKey(Vidautil, on_delete=models.CASCADE, blank=True,  verbose_name='Vida Útil')  # Field name made lowercase.

    class Meta:
        unique_together = ['padrao', 'tipo', 'nomecondominio', 'estadoconser', 'corretor', 'vidautil']

    def __str__(self):
        return "{} - {} - {} - {} - {} - {} ".format(self.padrao.nome, self.tipo.nome, self.nomecondominio.nome, self.estadoconser.nome, self.corretor.nome, self.vidautil.nome)

    def __float__(self):
        return "{} - {} - {}".format(self.valordevenda, self.aconstruida, self.atotal)

    def metroquadrado(self):
        metro_quadrado=((self.valordevenda)/(self.aconstruida))
        return metro_quadrado

    def get_absolute_url(self):
        return reverse("editar", kwargs={"imovel_pk": self.id})

