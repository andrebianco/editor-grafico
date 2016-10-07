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

    def test_send_command_first_I(self):
        result = editor(['I'])
        expected = 'Invalid command!'
        self.assertEqual(result, expected)

    def test_send_command_I_5_6(self):
        result = editor(['I', 5, 6])
        expected = '00000\n00000\n00000\n00000\n00000\n00000\n'
        self.assertEqual(result, expected)

    def test_send_command_exist_file(self):
        editor(['I', 5, 6])
        result = os.path.exists('matrix.txt')
        expected = True
        self.assertTrue(result, expected)

    def test_send_command_I_2_2(self):
        result = editor(['I', 2, 2])
        expected = '00\n00\n'
        self.assertEqual(result, expected)

    def test_send_command_I_x_2(self):
        result = editor(['I', 'x', 2])
        expected = 'Invalid command!'
        self.assertEqual(result, expected)

    def test_send_command_I_4_z(self):
        result = editor(['I', 4, 'z'])
        expected = 'Invalid command!'
        self.assertEqual(result, expected)

    def test_send_command_I_a_b(self):
        result = editor(['I', 'a', 'b'])
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
