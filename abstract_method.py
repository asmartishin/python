#!/usr/bin/env python3

import abc


class PizzaBase(object):
    __metaclass__  = abc.ABCMeta

    def __init__(self, size, ingredients):
        assert isinstance(ingredients, list)
        self.size = size
        self.ingredients = ingredients

    @abc.abstractmethod
    def get_ingredients(self):
        raise NotImplementedError

    def get_size(self):
        return self.size

    def __str__(self):
        return 'size: {}, ingredients: {}'.format(self.size, str(self.ingredients))

class PizzaWithMeat(PizzaBase):
    def __init__(self, size):
        super(PizzaWithMeat, self).__init__(size, ['meat'])

    def get_ingredients(self):
        return self.ingredients


if __name__ == '__main__':
    pizza = PizzaBase(42, ['cheese'])
    pizza_meat = PizzaWithMeat(42)
    print(pizza_meat.get_ingredients())
    print(pizza.ingredients)
