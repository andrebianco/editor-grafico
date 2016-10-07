# !/usr/bin/python
# -*- coding: utf-8 -*-

'''
PROPOSTA: Editor Gráfico que retorna uma imagem bitmap como resultado do
          processamento.
AUTOR: ANDRÉ TOLEDO BIANCO
       abianco.allegro@gmail.com
DATA:  2016-10-04


Explicação
----------
Dada uma matriz de tamanho MxN na qual cada elemento represente um pixel, crie
um programa que leia uma sequência de comandos e os interprete manipulando a
matriz de acordo com a descrição abaixo de cada comando.

Comandos
--------
I M N
Cria uma nova matriz MxN. Todos os pixels são brancos (O).

C
Limpa a matriz. O tamanho permanece o mesmo. Todos os pixels ficam brancos (O).

L X Y C
Colore um pixel de coordenadas (X,Y) na cor C.

V X Y1 Y2 C
Desenha um segmento vertical na coluna X nas linhas de Y1 a Y2 (intervalo
inclusivo) na cor C.

H X1 X2 Y C
Desenha um segmento horizontal na linha Y nas colunas de X1 a X2 (intervalo
inclusivo) na cor C.

K X1 Y1 X2 Y2 C
Desenha um retangulo de cor C. (X1,Y1) é o canto superior esquerdo e (X2,Y2) o
canto inferior direito.

F X Y C
Preenche a região com a cor C. A região R é definida da seguinte forma:
O pixel (X,Y) pertence a região. Outro pixel pertence a região, se e somente
se, ele tiver a mesma cor que o pixel (X,Y) e tiver pelo menos um lado em comum
com um pixel pertencente a região.

S name
Escreve a imagem em um arquivo de nome name.

X
Encerra o programa.

Considerações
-------------
Comandos diferentes de I, C, L, V, H, K, F, S e X devem ser ignorados

Testes
------

Entrada 01:

I 5 6
L 2 3 A
S one.bmp
G 2 3 J
V 2 3 4 W
H 3 4 2 Z
F 3 3 J
S two.bmp
X

Saida 01:

one.bmp
OOOOO
OOOOO
OAOOO
OOOOO
OOOOO
OOOOO

two.bmp
JJJJJ
JJZZJ
JWJJJ
JWJJJ
JJJJJ
JJJJJ

Entrada 02:

I 10 9
L 5 3 A
G 2 3 J
V 2 3 4 W
H 1 10 5 Z
F 3 3 J
K 2 7 8 8 E
F 9 9 R
S one.bmp
X

Saida 02:

one.bmp
JJJJJJJJJJ
JJJJJJJJJJ
JWJJAJJJJJ
JWJJJJJJJJ
ZZZZZZZZZZ
RRRRRRRRRR
REEEEEEERR
REEEEEEERR
RRRRRRRRRR
'''

import sys


current_matrix = ''


def editor(command):
    '''Editor Gráfico que retorna um bitmap'''

    if command[0] == 'I':
        return create_matrix(command)
    elif command[0] == 'C':
        return clear_matrix()
    else:
        return 'Invalid command!'


def create_matrix(command):
    '''
    I M N
    Cria uma nova matriz MxN. Todos os pixels são brancos (O).
    '''

    columns, rows, matrix = 0, 0, ''

    try:
        columns = '0' * int(command[1])
        rows = int(command[2])
    except ValueError:
        return 'Invalid command!'

    if columns == '' or rows == 0:
        return 'Invalid command!'

    row = 0

    while row != rows:
        matrix += columns + '\n'
        row += 1

    return matrix


def clear_matrix():
    '''
    C
    Limpa a matriz. O tamanho permanece o mesmo. Todos os pixels
    ficam brancos (O).
    '''

    if current_matrix == '':
        return 'Nothing to do!'

    return '00000\n00000\n00000\n00000\n00000\n00000\n'


def write_matrix_on_file(matrix):
    '''Grava a matriz em um arquivo texto'''
    file = open('matrix.txt', 'w')
    file.write(matrix)
    file.close()


def read_matrix_on_file():
    '''Lê a matriz de um arquivo texto'''
    pass


if __name__ == '__main__':

    command = sys.argv[1:]

    current_matrix = editor(command)

    write_matrix_on_file(current_matrix)

    print(current_matrix)
