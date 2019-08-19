"""
Classes to represent Products.
"""

import random

class Product:
    """
    Paramaters
    --------------------------
    name : str
        no default

    price : int
        default 10

    weight : int
        default 20

    flammability : float
        default 0.5

    identifier : int
        randomly generated int
    """
    # changed single quotes to double quotes for comment

    def __init__(self, name, price=10, weight=20, flammability=0.5,
                 identifier=random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        x = self.price / self.weight
        if x < 0.5:
            return 'Not so stealable'
        elif 0.5 <= x < 1.0:
            return 'Kinda stealable'
        else:
            return 'Very stealable!'

    def explode(self):
        x = self.flammability * self.weight
        if x < 10:
            return '...fizzle.'
        elif 10 <= x < 50:
            return '...boom!'
        else:
            return '...BABOOM!!'


class BoxingGlove(Product):

    def __init__(self, name, price=10, weight=10, flammability=0.5,
                 identifier=random.randint(1000000, 9999999)):
        super().__init__(name=name, price=price, weight=weight,
                         flammability=flammability, identifier=identifier)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        x = self.weight
        if x < 5:
            return 'That tickles.'
        elif 15 > x >= 5:
            return 'Hey that hurt!'
        else:
            return 'OUCH!'
