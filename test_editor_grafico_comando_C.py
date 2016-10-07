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
