# !/usr/bin/python
# -*- coding: utf-8 -*-

'''
PROPOSTA: Suite de Testes do Aplicativo Editor Gráfico (editor_grafico.py).
AUTOR: ANDRÉ TOLEDO BIANCO
       abianco.allegro@gmail.com
DATA:  2016-10-04
'''

import unittest
from editor_grafico import editor


class EditorGraficoTest(unittest.TestCase):
    '''Suite de testes do Editor Gráfico'''

    def test_send_command_I_5_6(self):
        result = editor(['I', 5, 6])
        expected = '00000\n00000\n00000\n00000\n00000\n00000\n'
        self.assertEqual(result, expected)

    def test_send_command_I_x_2(self):
        result = editor(['I', 'x', 2])
        expected = 'Invalid command!'
        self.assertEqual(result, expected)

    def test_send_command_I_0_4(self):
        result = editor(['I', 0, 4])
        expected = 'Invalid command!'
        self.assertEqual(result, expected)

    def test_send_command_I_2_0(self):
        result = editor(['I', 2, 0])
        expected = 'Invalid command!'
        self.assertEqual(result, expected)
