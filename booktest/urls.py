# @Date    : 2019-07-10
# @Author  : whp

from django.conf.urls import url
from booktest import views

# 严格匹配开始和结尾
urlpatterns = [
    # 通过url函数设置url路由配置项
    url(r'^index$', view=views.index), # 建立/index和视图index之间的关系
    url(r'^index2$', view=views.index2),
    url(r'^books$', view=views.show_books), # 显示图书信息
    url(r'^book/(\d+)$', view=views.detail) # 显示和图书相关的英雄的信息
]
