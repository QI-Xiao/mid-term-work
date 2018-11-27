# -*- coding:utf-8 -*-


class MedalTable:
    def __init__(self, ct, gd, sl, br):
        self.country = ct
        self.golden = gd
        self.silver = sl
        self.bronze = br

    def new_medal(self, place):
        if place == 1:
            self.golden += 1
        if place == 2:
            self.silver += 1
        if place == 3:
            self.bronze += 1

    @property
    # 装饰器 @property，将这个类方法转成只读的属性，称为属性函数。在调用时像属性一样，无需再加括号
    def medal_output(self):
        return self.golden+self.silver+self.bronze

    # __str__ 是类的内容方法，用来生成一个可读性好的字符串，可供 print 函数调用
    def __str__(self):
        return '%s：金%d，银%d，铜%d' % (self.country, self.golden, self.silver, self.bronze)


if __name__ == '__main__':
    # 当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行
    china = MedalTable('中国', 26, 18, 26)
    us = MedalTable('美国', 46, 37, 38)
    uk = MedalTable('英国', 27, 23, 17)
    print(china)
    print(us)
    print(uk)
    china.new_medal(2) # 注意下一行结果的变化
    print(china)
    print(china.medal_output)
    # china.medal_output()  # 不能加括号，已经是只读的属性了，加括号报错
    # print(type(us))
    # print(dir(us))
    medal_list = [us, uk, china]
    # print(medal_list)
    print('金牌榜')
    order_golden = sorted(medal_list, key=lambda x:x.golden, reverse=True)
    for i in order_golden:
        print(i)
    print('奖牌榜')
    order_total = sorted(medal_list, key=lambda x:x.golden+x.silver+x.bronze, reverse=True)
    for i in order_total:
        print(i)
