
import os
import time
import csv
import random
import hashlib
import datetime
from flask import Flask, request
from collections import namedtuple

def sleep(n_secs):
    time.sleep(n_secs)


def get_cityCode():
    citycodes = [
        {"title":"平谷","cityCode":"756","statusCode":200},
        {"title":"昌平","cityCode":"785","statusCode":200},
        {"title":"大兴","cityCode":"826","statusCode":200},
        {"title":"房山","cityCode":"827","statusCode":200},
        {"title":"怀柔","cityCode":"752","statusCode":200}
    ]
    citycode = [citycodes[random.randint(0,4)]]
    return citycode


# print(get_cityCode())



# 读取CSV文件，并将制定字段以int类型输出
def csv_cityName():
    with open('/Users/mr/Desktop/Git_httprunner/Httprunner2.3.0/datas/ciytCode.csv',mode='r',encoding='utf-8') as readers:
        csv_readers = csv.DictReader(readers)
        weather_date = []
        for row in csv_readers:
            weather_date.append(row)
        compressed = [(x['title'], x['cityName'], x['abbreviation'], int(x['statusCode'])) for x in weather_date]
        return compressed

print(csv_cityName())



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

app = Flask(__name__)
@app.route('/WebServices/WeatherWS.asmx/getWeather',methods=['POST','GET'])

def getWeather():
    theCityCode = request.values.get("theCityCode")
    if theCityCode == '756':
        return {"data":{"cityname":"平谷","cityid":theCityCode,"status":"小雨","centigrade":"9℃/18℃","wind":"北风小于3级"}}
        # return ('<ArrayOfString xmlns="http://WebXml.com.cn/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><string>直辖市 北京</string><string>平谷</string><string>756</string><string>2022/05/04 22:25:30</string><string>今日天气实况：气温：26℃；风向/风力：南风 2级；湿度：33%</string><string>紫外线强度：很强。</string><string>感冒指数：少发，感冒机率较低，避免长期处于空调屋中。 运动指数：较适宜，请适当减少运动时间，降低运动强度。 过敏指数：较易发，外出需远离过敏源，适当采取防护措施。 穿衣指数：炎热，建议穿短衫、短裤等清凉夏季服装。 洗车指数：适宜，天气较好，适合擦洗汽车。 紫外线指数：很强，涂擦SPF20以上，PA++护肤品，避强光。 </string><string>5月4日 晴转多云</string><string>18℃/32℃</string><string>西南风转东南风小于3级</string><string>0.gif</string><string>1.gif</string><string>5月5日 多云</string><string>13℃/29℃</string><string>南风小于3级转北风4-5级</string><string>1.gif</string><string>1.gif</string><string>5月6日 多云</string><string>8℃/23℃</string><string>北风转东南风小于3级</string><string>1.gif</string><string>1.gif</string><string>5月7日 多云转晴</string><string>8℃/24℃</string><string>东南风小于3级</string><string>1.gif</string><string>0.gif</string><string>5月8日 晴</string><string>9℃/24℃</string><string>西南风转东风小于3级</string><string>0.gif</string><string>0.gif</string></ArrayOfString>')
    elif theCityCode == '785':
        return {"data":{"cityname":"昌平","cityid":theCityCode,"status":"小雨","centigrade":"9℃/18℃","wind":"北风小于3级"}}
    elif theCityCode == '826':
        return {"data":{"cityname":"大兴","cityid":theCityCode,"status":"小雨","centigrade":"9℃/18℃","wind":"北风小于3级"}}



# if __name__ == '__main__':
#     app.run()
