from django.conf.urls import url
from django.urls import re_path,path
from . import view
from helloword import views

urlpatterns = [
    url('^$', view.index),
    url('^yoyo$', view.yoyo),
    url('^demo$', views.demo),
    url('^demo/page=(\d+$)',views.page),

    url('^demo/$',views.demo01,name="demo_page"),
    url('^home/',views.home01,name="home_page"),

    #匹配 archive/2018/10.html
    path("archive/<year>/<month>.html",views.home),

    path('yoyo/',views.yoyo),

    url(r'^archive1/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2}).html$',views.home1),

    path('base/',views.base),

    path('sonpage/',views.sonpage),

    path('basepage/',views.basepage)

]