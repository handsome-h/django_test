from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse('hello')


def hello(request, name):
    # return HttpResponse(f'hello, {name}')

    # 渲染模板，django默认使用Jinja2模板
    context = {'name': name}
    # 为什么模板文件夹中还要在创建一个hello子文件夹呢？这是由于django的文件搜索机制所导致的。当搜索模板文件的时候django会从所有app的templates文件夹中搜索，但是并不会区分它们，所以如果在多个app中有相同的文件名，django会使用找到的第一个。因此为了区分它们我们只能自己多创建一层文件夹用于区分。
    return render(request, 'app01/index.html', context)
