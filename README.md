# DjangoNote
Organnize some notes about learning Django
Version:Django1.1a1 + Python3.7

一个django的文件树形图:
    project
    │  manage.py
    │
    ├─myApp
    │  │  admin.py
    │  │  apps.py
    │  │  models.py
    │  │  tests.py
    │  │  urls.py
    │  │  views.py
    │  │  __init__.py
    │  │
    │  └─migrations
    │          __init__.py
    │
    ├─project
    │  │  settings.py
    │  │  urls.py
    │  │  wsgi.py
    │  │  __init__.py
    │  │
    │  └─__pycache__
    │          settings.cpython-37.pyc
    │          __init__.cpython-37.pyc
    │
    └─templates
        └─myApp
1 使用教程

    1.1 创建项目:
        >>>django-admin startproject project(Project Name)

        1.1.1 配置数据库:
            在project目录下的settings.py里，修改:DATABASES = {
            'default': {
                #'ENGINE': 'django.db.backends.sqlite3',  
                'ENGINE': 'django.db.backends.数据库',  
                'NAME': '数据库名字',   
                'USER':'用户名',
                'PASSWORD':'密码',
                'HOST':'数据库ip（本机填localhost）',
                'POST':'端口（默认3306）',
                }
            }
        
        1.1.2 引用数据库：
            project目录下的__init__.py里添加：
                import pymysql
                pymysql.install_as_MySQLdb()

        1.1.3 配置url:
            在urls.py里引入include（from django.conf.urls import url, include）
            并在urlpatterns里添加路由:url(r'^$', include('myApp.urls')),

    1.2 创建应用:
        >>>python manager.py startapp myApp(Application Name)

        1.2.1 创建urls.py:
            在myApp目录下创建urls.py, 并在其中引入（from . import views）及 （from django.conf.urls import url）
            添加 urlpattrens = [
                    url(r''),   
                ]

    1.3 创建模板:
        和project， myApp同级目录下创建templates，在templates下创建myApp，
        在project下的settings.py里的TEMPLATES中的'DIRS': [],添加[os.path.join(BASE_DIR, 'templates')]

