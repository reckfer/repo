from django.shortcuts import render
from django.http import HttpResponse

def clientes(request):
    return HttpResponse('Olá clientes!')

def cliente_por_codigo(request, id):
    return HttpResponse('Detalhes do cliente: %s' %id)

def cliente_por_nome(request, nome):
    return HttpResponse('Detalhes do cliente: %s' %nome)