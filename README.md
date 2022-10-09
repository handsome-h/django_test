django练习项目

教程：https://blog.csdn.net/u011054333/article/details/78767724

安装
```
pip install django
```

1、创建项目

Django安装好之后，会附带一个命令行工具django-admin，可以帮助我们管理Django项目。

```
django-admin startproject django_test 
```

2、运行项目

进入项目目录

```
python manage.py runserver
```


3、创建app

进入项目目录

```
django-admin startapp app01
```


4、激活app

进入项目目录下的settings.py文件，将app的配置app01.apps.App01Config加入到INSTALLED_APPS


5、生成迁移文件

```
python manage.py makemigrations app01
```


6、执行迁移生成数据库表
```
python manage.py migrate
```
























