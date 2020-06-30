# from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .db.connection import Connection


# Create your views here.
def hello(request):
    data = {'test': 'hello world'}
    return JsonResponse(data)


def msg(request, name, age):
    return HttpResponse('My name is ' + name + ',i am ' + age + ' years old')


def user(request, name):
    mydb = Connection().getConnection()
    mycol = mydb['BLOG_USER']
    data = mycol.find({'name': name}, {'password': 0})
    # mydb.closeConnection()
    return HttpResponse(data)
