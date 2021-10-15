
class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def drive(self):
        print(str(self.year) + " " + self.make + " " + self.model + " is driving. Vroom vroom.")

