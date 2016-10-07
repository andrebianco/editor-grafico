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

    def test_send_command_first_L(self):
        result = editor(['L'])
        expected = 'Invalid command!'
        self.assertEqual(result, expected)

    def test_send_command_L(self):
        editor(['I', 5, 6])
        result = editor(['L'])
        expected = 'Invalid command!'
        self.assertEqual(result, expected)

    def test_send_command_L_2_3(self):
        editor(['I', 5, 6])
        result = editor(['L', 2, 3])
        expected = 'Invalid command!'
        self.assertEqual(result, expected)

    def test_send_command_L_2_3_A(self):
        editor(['I', 5, 6])
        result = editor(['L', 2, 3, 'A'])
        expected = '00000\n00000\n0A000\n00000\n00000\n00000\n'
        self.assertEqual(result, expected)

    def test_send_command_L_2_3_0(self):
        editor(['I', 5, 6])
        result = editor(['L', 2, 3, 0])
        expected = 'Invalid command!'
        self.assertEqual(result, expected)

    def test_send_command_L_z_x(self):
        editor(['I', 5, 6])
        result = editor(['L', 'z', 'x'])
        expected = 'Invalid command!'
        self.assertEqual(result, expected)
