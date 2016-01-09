#!/usr/bin/env python

from abc import ABCMeta, abstractmethod
class Vehicle(object):
    """
    Attributes:
        wheels: An integer representing the number of wheels the vehicle has.
        miles: The integral number of miles driven on the vehicle.
        make: The make of the vehicle as a string.
        model: The model of the vehicle as a string.
        year: The integral year the vehicle was built.
        sold_on: The date the vehicle was sold.
    """

    __metaclass__ = ABCMeta

    base_sale_price = 0
    wheels = 0

    def __init__(self, miles, make, model, year, sold_on):
        self.miles = int(miles)
        self.make = make
        self.model = model
        self.year = int(year)
        self.sold_on = str(sold_on)

    def sale_price(self):
        if self.sold_on != 'None':
            return 0.0  # Already sold
        return 5000.0 * self.wheels

    def purchase_price(self):
        if self.sold_on == 'None':
            return 0.0  # Not yet sold
        return self.base_sale_price - (.10 * self.miles)

    @classmethod
    def from_string(cls, string):
        miles, make, model, year, sold_on = map(str, string.split(' '))
        vehicle = cls(miles, make, model, year, sold_on)
        return vehicle

    @staticmethod
    def make_sound():
        print 'VRooooommmm!'

    @abstractmethod
    def vehicle_type(self):
        pass

class Car(Vehicle):
    base_sale_price = 8000
    wheels = 4

    def vehicle_type(self):
        return 'car'

class Truck(Vehicle):
    base_sale_price = 10000
    wheels = 4

    def vehicle_type(self):
        return 'truck'

class Motorcycle(Vehicle):
    base_sale_price = 4000
    wheels = 2

    def vehicle_type(self):
        return 'motorcycle'

honda = Car(1000, 'Honda', 'Accord', 2014, 'Yes')
suzuki = Motorcycle.from_string('0 Suzuki Supersport 2014 None')
print 'Honda:'
print honda.purchase_price()
print honda.vehicle_type()
honda.make_sound()
print '\nSuzuki:'
print suzuki.sale_price()
print suzuki.vehicle_type()
suzuki.make_sound()
