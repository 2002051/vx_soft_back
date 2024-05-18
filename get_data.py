"""
导入数据，只能执行一次
"""

import os
import django
from tranapp.utils import md5_

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'soft.settings')
django.setup()



from tranapp.models import Type,Book,Banner,UserInfo,Campus

def get_type():
    Type.objects.create(title="全部")
    Type.objects.create(title="考研")
    Type.objects.create(title="经管")
    Type.objects.create(title="土木")
    Type.objects.create(title="材料")
    Type.objects.create(title="机械")
    Type.objects.create(title="人文")
    Type.objects.create(title="水利")
    Type.objects.create(title="自动化")
    Type.objects.create(title="计算机")
    Type.objects.create(title="测试")

def get_campus():
    Campus.objects.create(name="黄金校区")
    Campus.objects.create(name="白银校区")
    Campus.objects.create(name="青铜校区")
    Campus.objects.create(name="塑料校区")


def get_user():
    """初始用户用户名 root 密码 123"""
    username = "root"
    password = md5_.setPassword(password="123")
    UserInfo.objects.create(nickname="初始用户1",username=username,password=password,campus_id=1)


def get_book():
    """以为初始用户之名，发布图书"""
    Book.objects.create(type_id=1,name="王道考研数学",price=2200,author="木村",detail="王道考研数学教程",status="崭新",userinfo_id=1,active=1)
    Book.objects.create(type_id=2,name="经济学",price=2243,author="北野",detail="经济学经济学经济学简介",status="崭新",userinfo_id=1,active=1)
    Book.objects.create(type_id=3,name="土木学导论",price=3123,author="毛利",detail="土木学导论教程",status="崭新",userinfo_id=1,active=1)
    Book.objects.create(type_id=4,name="材料化学",price=1245,author="板木",detail="材料化学教程",status="崭新",userinfo_id=1,active=1)
    Book.objects.create(type_id=5,name="机械铸造",price=2212,author="山下",detail="机械铸造教程",status="崭新",userinfo_id=1,active=1)
    Book.objects.create(type_id=6,name="人文科学",price=5542,author="土屋",detail="人文科学教程",status="崭新",userinfo_id=1,active=1)
    Book.objects.create(type_id=8,name="自动化开发",price=6755,author="尾田",detail="自动化开发简介",status="崭新",userinfo_id=1,active=1)
    Book.objects.create(type_id=9,name="大数据导论",price=1233,author="清田",detail="大数据导论教程",status="崭新",userinfo_id=1,active=1)

def run():
    get_type()
    get_campus()
    get_user()
    get_book()

if __name__ == '__main__':
    run()