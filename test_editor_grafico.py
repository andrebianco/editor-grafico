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

    def test_send_command_invalid(self):
        result = editor([])
        expected = 'Invalid command!'
        self.assertEqual(result, expected)