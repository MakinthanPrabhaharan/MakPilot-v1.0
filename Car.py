import tensorflow as tf
class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def drive(self):
        print(str(self.year) + " " + self.make + " " + self.model + " is driving. Vroom vroom.")

    def honk(self):
        print('beep beep')


class CircuitComponent:

    def __init__(self, posNode, negNode):
        self.posNode = posNode
        self.negNode = negNode
