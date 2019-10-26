# -*- coding: UTF-8 -*-
from aip import AipOcr

""" 百度ocr申请到的三个秘钥 """
APP_ID = '*******'
API_KEY = '************************'
SECRET_KEY = '******************************'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片的方法 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

""" 定义图片的绝对路径 """
image = get_file_content('/home/***/Software/OCR/Pictures/1.png')

""" 调用通用文字识别（高精度版）"""
restu1 = client.basicAccurate(image)   # 通用文字高精度识别，每天 500 次免费
#restu1 = client.basicGeneral(image)   # 通用文字识别，每天 50 000 次免费

""" 输出识别到的文字 """
lists = restu1['words_result']      #列表
for listss in lists:
    print(listss['words'])