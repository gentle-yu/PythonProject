from django.shortcuts import render
from django.http import HttpResponse,Http404

# Create your views here.

def index(request):
    return HttpResponse("Hello word ! django~~")

def demo(request):
    return render(request, 'demo.html')

def page(request,num):
    try:
        num == int(num)
        return render(request,'demo.html')
    except:
        raise Http404

def home(request,year = "2018",month = "11"):
    return HttpResponse("获取当前页面home时间标签：%s年/%s月" %(year,month))

def home1(request,year = "2018",month = "11"):
    return HttpResponse("获取当前页面home1时间标签：%s年/%s月" %(year,month))

def home01(request):
    return render(request,'home.html')

def demo01(request):
    return render(request,'demo.html')

def yoyo(request):
    context = {}
    context['name'] = 'yoyo'
    return render(request,'yoyo.html',context)

def base(request):
    context = {"name":"gentle.yu"}
    return render(request,'base.html',context)

def sonpage(request):
    context = {
        "ads":["selenium","appinum","request","pytest"]
        }
    return render(request,'sonpage.html',context)

def basepage(request):
    return render(request,'basepage.html')

def sonpage1(request):
    context = {
        "ads":["selenium","appinum","request","pytest"]
        }
    return render(request,'sonpage1.html',context)
