
# TermiPuzzle
# Jogo de terminal

import sys, os
from pacotes.clickTeclado import *
from pacotes.logicalclass import *
from pacotes.renderizador import *
from pacotes.criarMapa import *

avisos = [
    [
        ['vazio', 'vazio', 'vazio', 'vazio', 'vazio', 'vazio', 'vazio', 'vazio', 'vazio'],
        ['vazio', 'vazio', 'vazio', 'vazio', 'vazio', 'vazio', 'vazio', 'vazio', 'vazio'],
        ['vazio', 'azul', 'azul', 'azul', 'vazio', 'vermelho', 'vermelho', 'vermelho', 'vazio'],
        ['vazio', 'azul', 'vazio', 'azul', 'vazio', 'vermelho', 'vazio', 'vazio', 'vazio'],
        ['vazio', 'azul', 'azul', 'azul', 'vazio', 'vermelho', 'vazio', 'vermelho', 'vazio'],
        ['vazio', 'azul', 'vazio', 'vazio', 'vazio', 'vermelho', 'vermelho', 'vermelho', 'vazio'],
        ['vazio', 'vazio', 'vazio', 'vazio', 'vazio', 'vazio', 'vazio', 'vazio', 'vazio'],
        ['vazio', 'vazio', 'vazio', 'vazio', 'vazio', 'vazio', 'vazio', 'vazio', 'vazio']
    ],
    [
        ['vazio', 'vazio', 'vazio', 'vazio', 'vazio', 'vazio', 'vazio', 'vazio', 'vazio'],
        ['vazio', 'azul', 'azul', 'azul', 'vazio', 'vermelho', 'vermelho', 'vermelho', 'vazio'],
        ['vazio', 'azul', 'vazio', 'vazio', 'vazio', 'vermelho', 'vazio', 'vermelho', 'vazio'],
        ['vazio', 'azul', 'vazio', 'azul', 'vazio', 'vermelho', 'vazio', 'vermelho', 'vazio'],
        ['vazio', 'azul', 'azul', 'azul', 'vazio', 'vermelho', 'vermelho', 'vermelho', 'vazio'],
        ['vazio', 'vazio', 'vazio', 'vazio', 'vazio', 'vazio', 'vazio', 'vazio', 'vazio'],
        ['vazio', 'azul', 'azul', 'azul', 'vazio', 'vermelho', 'vazio', 'vermelho', 'vazio'],
        ['vazio', 'azul', 'vazio', 'azul', 'vazio', 'vermelho', 'vazio', 'vermelho', 'vazio'],
        ['vazio', 'azul', 'azul', 'azul', 'vazio', 'vermelho', 'vazio', 'vermelho', 'vazio'],
        ['vazio', 'azul', 'vazio', 'azul', 'vazio', 'vazio', 'vermelho', 'vazio', 'vazio'],
        ['vazio', 'vazio', 'vazio', 'vazio', 'vazio', 'vazio', 'vazio', 'vazio', 'vazio'],
        ['vazio', 'azul', 'vazio', 'azul', 'vazio', 'vermelho', 'vermelho', 'vermelho', 'vazio'],
        ['vazio', 'azul', 'azul', 'azul', 'vazio', 'vermelho', 'vazio', 'vazio', 'vazio'],
        ['vazio', 'azul', 'vazio', 'azul', 'vazio', 'vermelho', 'vermelho', 'vazio', 'vazio'],
        ['vazio', 'azul', 'vazio', 'azul', 'vazio', 'vermelho', 'vazio', 'vazio', 'vazio'],
        ['vazio', 'azul', 'vazio', 'azul', 'vazio', 'vermelho', 'vermelho', 'vermelho', 'vazio'],
        ['vazio', 'vazio', 'vazio', 'vazio', 'vazio', 'vazio', 'vazio', 'vazio', 'vazio'],
        ['vazio', 'azul', 'azul', 'azul', 'vazio', 'vermelho', 'vermelho', 'vermelho', 'vazio'],
        ['vazio', 'azul', 'vazio', 'vazio', 'vazio', 'vermelho', 'vazio', 'vermelho', 'vazio'],
        ['vazio', 'azul', 'azul', 'vazio', 'vazio', 'vermelho', 'vazio', 'vermelho', 'vazio'],
        ['vazio', 'azul', 'vazio', 'vazio', 'vazio', 'vermelho', 'vermelho', 'vazio', 'vazio'],
        ['vazio', 'azul', 'azul', 'azul', 'vazio', 'vermelho', 'vazio', 'vermelho', 'vazio'],
        ['vazio', 'vazio', 'vazio', 'vazio', 'vazio', 'vazio', 'vazio', 'vazio', 'vazio']
    ]
]

objetos = {
    'jogador': {'cor': 'azul', 'vida': 5},
    'grama': {'cor': 'verde'},
    'parede': {'cor': 'cinza'}
}

# Inicio do jogo
while True:#{

    clickTeclado().clickSemRetorno()
    Renderizar(avisos[1])

#}