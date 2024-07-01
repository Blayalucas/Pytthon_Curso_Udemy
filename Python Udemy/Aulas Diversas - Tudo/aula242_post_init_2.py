# _post_init_

"""
_Post_init sem a criação de um _init_

field é uma função em python de configuração 

"""

from dataclasses import dataclass, field


@dataclass
class Order:
    net: float
    vat: float
    total: float = field(init=False)

    def __post_init__(self):
        self.total = self.net + self.vat


order = Order(net=100.00, vat=22.00)
print(order)  