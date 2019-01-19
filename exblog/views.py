from django.core.paginator import Paginator
from django.shortcuts import render
from edblog.models import Article


# 前台首页
def index(request):
    if request.method == 'GET':
        page = int(request.GET.get('page', 1))
        articles = Article.objects.all()
        paginator = Paginator(articles, 3)
        page = paginator.page(page)
        return render(request, 'q/index.html', {'page': page})


def share(request):
    if request.method == 'GET':
        return render(request, 'q/share.html')


def list(request):
    if request.method == 'GET':
        return render(request, 'q/list.html')


def about(request):
    if request.method == 'GET':
        return render(request, 'q/about.html')



def gbook(request):
    if request.method == 'GET':
        return render(request, 'q/gbook.html')


# 取数据库文章内容
def info(request, id):
    if request.method == 'GET':
        articles = Article.objects.filter(id=id).first()
        return render(request, 'q/info.html', {'article': articles})


