from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
from django.http import HttpResponse
from .models import NewHouseInfo_table,Province_table,City_table,TypeOfHouse_table
import requests
from django.core.paginator import Paginator
# def city(request,id):
#     city=TypeOfHouse_table.objects.filter(id=id)[0]
#     context={
#         'city':city,
#     }
#     return render(request,'app/city.html',context)
#from django import template
#register=template.Library()
#@register.filter
#def to_and(value):
#    return value.replace("/")
def area(request,city_id,area_id,page_num):     #
    result = NewHouseInfo_table.objects.filter(area_table_id=area_id)
    city = TypeOfHouse_table.objects.filter(id=city_id)[0]
    p=Paginator(result,10)
    if p.num_pages<=page_num:
        page1 = p.page(p.num_pages).object_list
    else:
        page1=p.page(page_num).object_list
    for i in page1:
        i.label=(i.house_label).split("/")
    context={
        "results":page1,
        'next':page_num+1,
        'last':page_num-1,
        'city_id':city_id,
        'area_id':area_id,
        'city': city,
    }
    return render(request,"app/area.html",context)
def index(request):
    provinces=Province_table.objects.all()
    context={
        "provinces":provinces,
    }
    return render(request,"app/home.html",context)

    # # header = {
    # #     'refer': 'https://www.baidu.com',
    # #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
    # # }
    # # date=requests.get(url,header=header)
    # # for i in result[]
    # result=NewHouseInfo_table.objects.filter(Area_table_id=2)
    #
    # context={
    #     "results":result[:10],
    # }
    # return render(request,"app/index.html",context)

def tu(request):
    return render(request,'3.html')

import json
def deal(request):
    x=request.GET['x']
    y=request.GET['y']
    url="http://api.map.baidu.com/place/v2/search?query=%E5%B0%8F%E5%8C%BA&location="+str(y)+","+str(x)+"&radius=2000&output=json&ak=CzyN8k3YK9BVpP2fOwhtiCpkkZKwASd5"
    data=requests.get(url)
    data=data.json()
    #x=data['results'][0]['location']['lat']
    #y=data['results'][0]['location']['lng']
    #data={}
    #data['x']=x
    #data['y']=y
    result="<ul>"
    for name in data['results']:
        result=result+"<li><a>"+name['name']+"</a><li>"
    result=result+"</ul>"
    return HttpResponse(result)
