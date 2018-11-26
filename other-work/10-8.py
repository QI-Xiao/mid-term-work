# -*- coding: 'utf-8' -*-

import requests
import re

while True:
    city = input('请输入城市,回车退出:\n')
    if not city:
        break
        # exit() 如果没有while循环，只能用exit，注意区别

    req = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=%s' % city)
    # requests提供了对于gzip压缩、字符编码、json的自动处理

    dic_city = req.json() # 转换为字典

    # city_data = dic_city['data']
    # 这种方法，城市名错误返回的字典中没有’data‘这个键，程序报错，要用get方法
    city_data = dic_city.get('data')  # 没有’data‘的话返回 []

    if city_data:
        city_forecast = city_data['forecast'][0] # 下面的都可以换成'get'方法
        print(city_forecast.get('date'))
        print(city_forecast.get('high'))
        print(city_forecast.get('low'))
        fengli = re.findall(r'\d.', city_forecast.get('fengli'))
        print('风力：', ''.join(fengli))
        print(city_forecast.get('fengxiang'))
        print(city_forecast.get('type'))
    else:
        print('未获得')
