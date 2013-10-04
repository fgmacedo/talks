#coding: utf-8
from raspador import Parser, BaseField


class ListField(BaseField):
    conversion_function = lambda self, x: x

    def to_python(self, value):
        value = value.replace('.', '')
        return [self.conversion_function(v) for v in value.split()]


class FloatListField(ListField):
    conversion_function = lambda self, x: float(x)


class SPTrans(Parser):
    FluxoDeCaixa = ListField(r'FLUXO DE CAIXA(.*)')
    CreditoEletronico = FloatListField(
        r'Venda de Crédito Eletrônico([\s\d.]+)'
    )
    DiversasFinanceiras = FloatListField(
        r'Venda de Crédito Eletrônico([\s\d.]+)'
    )

    def process_item(self, item):
        return item
