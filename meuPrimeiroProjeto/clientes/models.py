from django.db import models

class CPF(models.Model):
    numero = models.CharField(max_length=11)
    data_exp = models.DateTimeField(auto_now=False)

    def __str__(self):
        return '{0} - {1}'.format(self.numero, self.data_exp)

class Cliente(models.Model):
    nome = models.CharField(max_length=70, null=False)
    cpf = models.OneToOneField(CPF, on_delete=models.CASCADE, blank=True, null=True)
    endereco = models.CharField(max_length=200, blank=False, null=False)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    idade = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Telefone(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    numero = models.CharField(max_length=20)
    descricao = models.CharField(max_length=80)

    def __str__(self):
        return '{1} - {0}'.format(self.numero, self.descricao)