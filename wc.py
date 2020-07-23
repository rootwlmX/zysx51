# -*- coding: utf-8 -*-
# @Time    : 2020/7/23 22:45
# @Author  : 周勇吉
# @File    : wordcloud.py
# @Software: PyCharm
import sqlite3
import jieba
import numpy as np
from PIL import Image
from wordcloud import WordCloud
from matplotlib import pyplot as plt

if __name__ == '__main__':
    con = sqlite3.connect('database.db')  # 连接数据库
    cur = con.cursor()
    sql = 'select job_name from jobtable'
    data = cur.execute(sql)
    text=""
    for item in data:  # 将查询出的结果连接成一个字符串
        text = text + item[0]
        print(text)
    cur.close()
    con.close()
    cut = jieba.cut(text)  # 分词
    string = ' '.join(cut)
    print(len(string))  # 打印分词数量
    img = Image.open('static/img/wordcloud/bear.png')  # 打开图片
    img_array = np.array(img)  # 将图片装换为数组
    wc = WordCloud(  # 词云参数设置
        background_color='white',  # 设置背景颜色
        mask=img_array,  # 设置背景图片
        font_path="msyh.ttc"
    ).generate_from_text(string)

    fig = plt.figure(1)  # 新建一个名叫 Figure1的画图窗口
    plt.imshow(wc)  # 显示图片，同时也显示其格式
    plt.axis('off')  # 是否显示x轴、y轴下标
    # plt.show() #显示生成合成图片
    plt.savefig('static/img/wordcloud/new.png', dpi=500)