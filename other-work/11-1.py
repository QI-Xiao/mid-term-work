#面向过程
def drive (speed, price, distance):
    print ('time is', distance / speed)
    print ('cost', distance * price)

car = {
    'speed':50.0,
    'price': 2.5
}
distance = 180
drive(car['speed'],car['price'],distance)

car2 = {
    'speed':70.0,
    'price':3.5
}
drive(car2['speed'], car2['price'], distance)



#面向对象，一个对象的属性是跟随这个对象的，如果属性被修改，再次访问就是修改后的值
class car:
    def __init__(self, sp = 50.0, pr = 2.5):  #对象被创建时调用
        print ('init a car')
        self.speed = sp
        self.price = pr
        self.distance = 0
    def drive (self, distance):
        self.distance += distance
        print ('total drive', self.distance)
        print ('time is', distance / self.speed)
        print ('cost', distance * self.price)
print ('8888888888888888888')
c1 = car()
c1.drive(180)
c1.drive(100)
c1.drive(80)

print ('2222222222222222222222')
c2 = car(80.0,3.5)
c2.drive(180)

c3 = car(40.0)
c3.drive(100)

c4 = car()
print (type(c4))
print (dir(c4))
print (isinstance(c4, car))
print (isinstance(c4, int))