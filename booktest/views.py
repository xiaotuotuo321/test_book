from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
from booktest.models import BookInfo, HeroInfo


# Create your views here.
# 1. 定义视图函数，HttpRequest
# 2. 进行url配置，建立url地址和视图之间的对应关系

def my_render(request, template_path, context_dict={}):
    """使用模板文件"""
    # 使用模板文件
    # 1. 加载模板文件，模板对象
    temp = loader.get_template(template_path)
    # 2. 定义模板上下文，给模板传输数据
    context = RequestContext(request, context_dict)
    # 3. 模板渲染: 产生标准的html内容
    res_html = temp.render(context)
    # 4. 返回给浏览器
    return HttpResponse(res_html)

def index(request):
    # 进行处理，和M和T进行交互。。。
    # return HttpResponse('老铁，没毛病！')
    # return my_render(request, 'booktest/index.html')
    return render(request, 'booktest/index.html', {'content': 'Hello World',
                                                   'list': list(range(1,10))})

def index2(request):
    return HttpResponse('Hello,Python!')

def show_books(request):
    """显示图书信息"""
    # 1. 通过M查找图书表中的数据
    books = BookInfo.objects.all()
    # 2. 使用模板
    return render(request, 'booktest/show_books.html', {'books': books})

def detail(request, bid):
    """查询图书相关联的英雄的信息"""
    # 1. 根据bid查找图书信息
    book = BookInfo.objects.get(id=bid)
    # 2. 查询和book关联的英雄的信息
    heros = book.heroinfo_set.all()
    # 3. 使用模板
    return render(request, 'booktest/detail.html', {'book': book, 'heros': heros})
