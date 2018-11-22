class Pen:
    name = 'Pen'
    def write(self):
        print ('I have a', self.name)

# 创建两个 Pen 子类，并修改各自的 name
# 一个叫 ApplePen
class ApplePen(Pen):
    name = 'ApplePen'
    def write(self):
        super(ApplePen, self).write()

# 一个叫 PineapplePen
class PineapplePen(Pen):
    name = 'PineapplePen'
    def write(self):
        super(PineapplePen, self).write()

# 分别创建这两个子类的对象
ap = ApplePen()
pp = PineapplePen()
ap.write()
pp.write()
