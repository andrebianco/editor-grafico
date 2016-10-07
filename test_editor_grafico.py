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