class vehicle:
    def __init__(self, sp = 15.0):  #对象被创建时调用
        print ('init a vehicle')
        self.speed = sp
        self.distance = 0
        print ('end')
    def drive (self, distance):
        self.distance += distance
        print ('total drive', self.distance)
        print ('time is', distance / self.speed)
        print ()

class car(vehicle):
    def __init__(self, sp = 50.0, pr = 2.5):  #对象被创建时调用
        super(car, self).__init__(sp)
        print ('init a car')
        self.price = pr
    def drive (self, distance):
        print ('cost', distance * self.price)
        super(car, self).drive(distance)
    def fuel(self):
        print ('fuel the car')

class bike(vehicle):
    def __init__(self, sp=15.0):  # 对象被创建时调用
        super(bike,self).__init__(sp)
        print('init a bike')


b1 = bike()
print ("33333333333333")
b1.drive(20)
b1.drive(100)
b1.drive(80)

print ('2222222222222222222222')
c2 = car(80.0,3.5)
c2.drive(180)
c2.fuel()
print ('eeee')

