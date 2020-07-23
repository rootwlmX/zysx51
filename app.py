from flask import Flask
import sqlite3
from datetime import timedelta
from matplotlib import pyplot as plt
import jieba
import numpy as np
from PIL import Image
from flask import Flask, render_template, request

app = Flask(__name__)


# 首页
@app.route('/')
def hello_world():
    return render_template("index.html")


# About Us
@app.route('/about')
def about():
    return render_template("about_2.html")


@app.route('/portfolio')
def portfolio():
    return render_template("portfolio.html")


@app.route('/p_showdata')
def showdataproject():
    return render_template("p_showdata.html")


@app.route('/showdatalist')
def showdatalist():
    job = []
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    page = 1
    req = request.args.get('page')
    if not req:
        page = 1
    else:
        page = int(req)
    sql = 'select * from jobtable o limit '+str((page-1)*30)+',30'
    data = cur.execute(sql)
    for item in data:
        job.append(item)
    cur.close()
    con.close()
    return render_template("showdatalist.html", job=job, page=page)


if __name__ == '__main__':
    app.run(debug=True)
