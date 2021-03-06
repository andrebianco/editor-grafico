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
from PIL import Image, ImageDraw, ImageFont


current_matrix = ''


def editor(command):
    '''Editor Gráfico que retorna um bitmap'''

    try:
        if command[0] == 'I':
            return create_matrix(command)
        elif command[0] == 'C':
            return clear_matrix()
        elif command[0] == 'L':
            return color_matrix(command)
        elif command[0] == 'S':
            return save_bmp(command)
        else:
            return 'Invalid command!'
    except IndexError:
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

    current_matrix = matrix

    write_matrix_on_file(current_matrix)

    return current_matrix


def color_matrix(command):
    '''
    L X Y C
    Colore um pixel de coordenadas (X,Y) na cor C.
    '''

    x, y, len_column, color = 0, 0, 0, ''

    try:
        x = int(command[1])
        y = int(command[2])
        color = command[3]
    except ValueError:
        return 'Invalid command!'

    if not isinstance(color, str):
        return 'Invalid command!'

    if color == '':
        return 'Invalid command!'

    current_matrix = read_matrix_on_file()

    map_file(current_matrix)

    write_matrix_on_file(current_matrix)

    return current_matrix


def clear_matrix():
    '''
    C
    Limpa a matriz. O tamanho permanece o mesmo. Todos os pixels
    ficam brancos (O).
    '''

    current_matrix = read_matrix_on_file()

    if current_matrix == '':
        return 'Nothing to do!'
    else:

        matrix_list = list(current_matrix)

        for idx, char_ in enumerate(matrix_list):
            if char_ not in ('0', '\n'):
                matrix_list[idx] = '0'

        current_matrix = ''.join(matrix_list)

        write_matrix_on_file(current_matrix)

        return current_matrix


def write_matrix_on_file(matrix):
    '''Grava a matriz em um arquivo texto'''

    file = open('matrix.txt', 'w')
    file.write(matrix)
    file.close()


def read_matrix_on_file():
    '''Lê a matriz de um arquivo texto'''

    try:
        file = open('matrix.txt', encoding='utf-8')
        current_matrix = file.read()
        file.close()
    except FileNotFoundError:
        current_matrix = ''

    return current_matrix


def map_file(matrix):
    '''Faz o mapeamento da matriz'''

    rows = []
    row = []
    columns = []

    for c in matrix:
        if c != '\n':
            columns.append(c)
        else:
            row.append(columns)
            rows.append(row)

    print(rows)


def unmap_file(matrix):
    '''Desfaz o mapeamento da matriz'''

    pass


def save_bmp(command):
    '''Salva o arquivo bitmap'''

    file_name = command[1]

    image = Image.new("RGB", (500, 500))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("Arvo-Regular.ttf", 25)
    text = read_matrix_on_file()

    draw.text((0, 0), text, font=font)

    file = open(file_name, "wb")
    image.save(file, "BMP")
    image.show()


if __name__ == '__main__':

    command = sys.argv[1:]

    current_matrix = editor(command)

    print(current_matrix)
