from django.urls import path
from . import views

# 该文件是自己创建的，整理子应用路由

# 当项目中存在多个app的时候，需要使用命名空间来区分。
app_name = 'app01'



urlpatterns = [
    path('', views.index, name='index'),
    # 路径参数，<类型:变量名>语法
    path('hello/<str:name>', views.hello, name='hello')
    # 在页面中使用url，helloWie上面name属性的值
    # <a href="{% url 'hello' '张三' %}">你好，张三</a>
    # 当项目中存在多个app的时候，需要使用命名空间来区分，然后在标签上添加用冒号分隔开的命名空间名称即可。
    # <a href="{% url 'hello:hello' '张三' %}">你好，张三</a>
]
