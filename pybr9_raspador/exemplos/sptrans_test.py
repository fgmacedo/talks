#coding: utf-8

import unittest
from sptrans_parser import SPTrans


class TestSpStrans(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.parser = SPTrans()
        with open('sptrans_setembro.txt') as f:
            self.data = list(self.parser.parse(f))

        if self.data:
            self.data = self.data[0]

    def test_fluxo_caixa(self):
        item = [
            'Saldo', '02/09', '03/09', '04/09', '05/09',
            '06/09', '09/09', '10/09', '11/09', '12/09',
            '13/09', '16/09', '17/09', '18/09', '19/09',
            '20/09', '23/09', '24/09', '25/09', '26/09',
            'Total',
        ]
        self.assertEqual(self.data.FluxoDeCaixa, item)

    def test_venda_credito(self):
        item = [
            0, 20184474, 17407435, 20095264,
            13197893, 11332662, 9414443, 10719501,
            12496515, 10446554, 9796763, 7305125,
            7727924, 12092532, 9972108, 9042939,
            11623829, 13182085, 25445015, 23603709,
            255086770
        ]
        self.assertEqual(self.data.CreditoEletronico, item)

if __name__ == '__main__':
    unittest.main()
