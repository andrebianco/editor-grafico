# !/usr/bin/python
# -*- coding: utf-8 -*-

'''
PROPOSTA: Suite de Testes do Aplicativo Editor Gráfico (editor_grafico.py).
AUTOR: ANDRÉ TOLEDO BIANCO
       abianco.allegro@gmail.com
DATA:  2016-10-04
'''

import unittest
import os
from editor_grafico import editor


class EditorGraficoTest(unittest.TestCase):
    '''Suite de testes do Editor Gráfico'''

    def setUp(self):
        if os.path.exists('matrix.txt'):
            os.remove('matrix.txt')

    def test_send_command_first_C(self):
        result = editor(['C'])
        expected = 'Nothing to do!'
        self.assertEqual(result, expected)

    def test_send_command_C(self):
        editor(['I', 5, 6])
        result = editor(['C'])
        expected = '00000\n00000\n00000\n00000\n00000\n00000\n'
        self.assertEqual(result, expected)

    def test_send_command_C_effective(self):
        file = open('matrix.txt', 'w')
        file.write('0A000\n0000A\n0A000\n00000\n000A0\n00A00\n')
        file.close()
        result = editor(['C'])
        expected = '00000\n00000\n00000\n00000\n00000\n00000\n'
        self.assertEqual(result, expected)
