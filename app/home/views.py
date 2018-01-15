# coding:utf-8

from . import home
from flask import render_template
from app.models import r
import datetime


@home.route('/<int:page>',methods=['GET'])
def hello(page=None):
    MONTH=('JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AGUEST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER')
    if page==None:
        page=1
    jokes=[]
    count=r.zcard('qiushicontent')
    value=r.zrange('qiushicontent',0,count)
    for v in value:
        jokes.append(v.decode('utf-8'))
    pagenum = []
    if count%10==0:
        count=int(count/10)
    else:
        count=int(count/10)+1
    for a in range(1, count + 1):
        pagenum.append(a)
    page_data = jokes[(page - 1) * 10:page * 10]
    pre_page=page-1
    next_page=page+1
    year=datetime.datetime.now().year
    month=datetime.datetime.now().month
    day=datetime.datetime.now().day
    time=MONTH[month]+' '+str(day)+','+str(year)
    return render_template('index.html',page_data=page_data,pre_page=pre_page,next_page=next_page,count=count,time=time)