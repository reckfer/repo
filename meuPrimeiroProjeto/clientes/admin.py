from django.contrib import admin
from clientes.models import Cliente
from clientes.models import Telefone
from clientes.models import CPF
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Telefone)
admin.site.register(CPF)