# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 17:10:47 2021

@author: du_la
"""
# Importando a função urls e todas as views do aplicativo:
from django.urls import path
from . import views

# Adicionando o primeiro padrão de URLs:
# Este padrão dirá ao Django que views.post_list é o lugar correto aonde ir se 
# alguém entra em seu site pelo endereço 'http://127.0.0.1:8000 /'.
urlpatterns = [
    path('', views.post_list, name='post_list'),    # Atribuindo uma view chamada post_list à URL raiz.
]