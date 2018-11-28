class Vehicle:
    def __init__(self, sp=15.0):
        print('init a Vehicle')
        self.speed = sp
        self.distance = 0

    def drive(self, distance):
        self.distance += distance
        print('total drive', self.distance)
        print('time is', distance / self.speed)
        print()


class Bike(Vehicle):
    def __init__(self, sp=15.0):
        super(Bike, self).__init__(sp)
        print('init a Bike')


class Car(Vehicle):
    def __init__(self, sp=50.0, pr=2.5):
        super(Car, self).__init__(sp)
        print('init a car')
        self.price = pr

    def drive(self, distance):
        print('cost', distance * self.price)
        super(Car, self).drive(distance)

    def feul(self):
        print('feul the car')


b = Bike()
b.drive(20)

c = Car()
c.drive(180)
c.feul()

print()


class Pen:
    name = 'Pen'
    def write(self):
        print('i have', self.name)


class ApplePen(Pen):
    name = 'ApplePen'


class PineapplePen(Pen):
    name = 'Pine'


ap = ApplePen()
pp = PineapplePen()
ap.write()
pp.write()