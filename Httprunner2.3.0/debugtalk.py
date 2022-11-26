# -*- coding: utf-8 -*-
import os
import time
import csv
import random
import hashlib
import datetime
from flask import Flask, request, jsonify
from collections import namedtuple
from json_response import JsonResponse
from flask_cors import CORS


def get_cityName():
    citycodes = [
        {"title":"北京","cityName":"北京市","abbreviation":"Beijing","statusCode":200},
        {"title":"平谷","cityName":"平谷区","abbreviation":"Pinggu","statusCode":200},
        {"title":"驻马店","cityName":"驻马店市","abbreviation":"Zhumadian","statusCode":200},
        {"title":"纽约","cityName":"纽约","abbreviation":"New York","statusCode":200},
    ]
    citycode = [citycodes[random.randint(0,3)]]
    return citycode


# print(get_cityName())

# 读取CSV文件，并将指定字段以int类型输出
def csv_cityName():
    # with open('ciytName.csv',mode='r',encoding='utf-8') as readers:
    #     csv_readers = csv.DictReader(readers)
    #     weather_date = []
    #     for row in csv_readers:
    #         weather_date.append(row)
    #     compressed = [(x['title'], x['cityName'], x['abbreviation'], int(x['statusCode'])) for x in weather_date]
    #     return compressed

    with open(r'datas/ciytName.csv', mode='r', encoding='utf-8') as readers:
        csv_datas = csv.DictReader(readers)
        weather_date = []
        for data in csv_datas:
            data['statusCode'] = int(data['statusCode'])
            weather_date.append(dict(data))
        return weather_date

# print(csv_cityName())


#MD5加密
def md5_key(value):
   if isinstance(value, str) == True:
        md5_data = hashlib.md5(value.encode(encoding='UTF-8')).hexdigest()
        return md5_data.upper()
   else:
       print('int')
       value = str(value)
       md5_data = hashlib.md5(value.encode(encoding='UTF-8')).hexdigest()
       return md5_data.upper()


# print(md5_key('123'))

# mock

class JsonFlask(Flask):
    def make_response(self, rv):
        """视图函数可以直接返回: list、dict、None"""
        if rv is None or isinstance(rv, (list, dict)):
            rv = jsonify(rv)
        #     rv = JsonResponse.success(rv)
        #
        # if isinstance(rv, JsonResponse):
        #     rv = jsonify(rv.to_dict())

        return super().make_response(rv)

# class JsonResponse(object):
#     """
#     统一的json返回格式
#     """
#
#     def __init__(self, data, code, msg):
#         self.data = data
#         self.code = code
#         self.msg = msg
#
#     @classmethod
#     def success(cls, data=None, code=0, msg='success'):
#         return cls(data, code, msg)
#
#     @classmethod
#     def error(cls, data=None, code=-1, msg='error'):
#         return cls(data, code, msg)
#
#     def to_dict(self):
#         return {
#             "code": self.code,
#             "msg": self.msg,
#             "data": self.data
#         }

app = JsonFlask(__name__)
CORS(app, supports_credentials=True)


@app.route('/geo/1.0/direct', methods=['POST','GET'])
def get_Zuobiao():
    city_Name = request.values.get("q")

    if city_Name == "北京市":
        return [{"country":"CN","lat":39.906217,"local_names":{"zh":"北京市"},"lon":116.3912757,"name":"Beijing",
                "state":"Beijing"}]
    elif city_Name == "平谷区":
        return [{"name":"Pinggu District","local_names":{"zh":"平谷区"},"lat":40.1390433,"lon":117.1146953,"country":"CN",
                "state":"Beijing"}]
    elif city_Name == "驻马店市":
        return [{"name":"Zhumadian City","local_names":{"zh":"驻马店市"},"lat":33.0115818,"lon":114.0164565,"country":"CN",
                "state":"Henan"}]
    elif city_Name == "纽约":
        return [{"name": "New York", "local_names": {"zh": "纽约"}, "lat": 40.7127281, "lon": -74.0060152, "country": "US",
                "state": "New York"}]

@app.route('/data/2.5/weather', methods=['POST','GET'])
def get_Tianqi():
    city_Lat = request.values.get("lat")
    city_Lon = request.values.get("lon")

    if city_Lat == "39.906217" and city_Lon == "116.3912757":
        return {"coord":{"lon":116.3913,"lat":39.9062},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"base":"stations","main":{"temp":292.09,"feels_like":290.93,"temp_min":292.09,"temp_max":292.09,"pressure":1016,"humidity":34,"sea_level":1016,"grnd_level":1010},"visibility":10000,"wind":{"speed":3.78,"deg":154,"gust":3.22},"clouds":{"all":97},"dt":1652085409,"sys":{"type":1,"id":9609,"country":"CN","sunrise":1652043958,"sunset":1652094951},"timezone":28800,"id":1816670,"name":"Beijing","cod":200}
    elif city_Lat == "40.1390433" and city_Lon == "117.1146953":
        return {"coord":{"lon":117.1147,"lat":40.139},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"base":"stations","main":{"temp":292.19,"feels_like":291.25,"temp_min":292.19,"temp_max":292.19,"pressure":1016,"humidity":42,"sea_level":1016,"grnd_level":1013},"visibility":10000,"wind":{"speed":4.56,"deg":149,"gust":5.24},"clouds":{"all":99},"dt":1652085470,"sys":{"type":1,"id":9609,"country":"CN","sunrise":1652043753,"sunset":1652094809},"timezone":28800,"id":2035469,"name":"Pinggu","cod":200}
    elif city_Lat == "33.0115818" and city_Lon == "114.0164565":
        return {"coord":{"lon":114.0165,"lat":33.0116},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"base":"stations","main":{"temp":286.39,"feels_like":285.55,"temp_min":286.39,"temp_max":286.39,"pressure":1017,"humidity":68,"sea_level":1017,"grnd_level":1007},"visibility":10000,"wind":{"speed":5.25,"deg":18,"gust":8.61},"rain":{"1h":0.37},"clouds":{"all":100},"dt":1652085471,"sys":{"country":"CN","sunrise":1652045375,"sunset":1652094674},"timezone":28800,"id":1783873,"name":"Zhumadian","cod":200}
    elif city_Lat == "40.7127281" and city_Lon == "-74.0060152":
        return {"coord":{"lon":-74.006,"lat":40.7127},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"base":"stations","main":{"temp":281.43,"feels_like":277.7,"temp_min":279.68,"temp_max":282.59,"pressure":1021,"humidity":39},"visibility":10000,"wind":{"speed":7.6,"deg":25,"gust":12.96},"clouds":{"all":0},"dt":1652085471,"sys":{"type":2,"id":2039034,"country":"US","sunrise":1652089507,"sunset":1652140790},"timezone":-14400,"id":5128581,"name":"New York","cod":200}


if __name__ == '__main__':
    app.run()

def sleep_N_secs(response, n_secs):
    # 休眠
    if response.status_code == 200:
        time.sleep(n_secs)
    else:
        time.sleep(0.5)




