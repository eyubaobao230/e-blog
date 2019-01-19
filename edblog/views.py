from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from edblog.ArtForm import AddArtForm, EditArtForm
from edblog.models import Article, SuperUser


def hindex(request):
    if request.method == 'GET':
        return render(request, 'h/hindex.html')


# 登录
def login(request):
    if request.method == 'GET':
        return render(request, 'h/login.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('userpwd')
        user = SuperUser.objects.filter(username = username, password = password).first()
        if not user:
            return render(request, 'login.html')

        request.session['user_id'] = user.id
        return HttpResponseRedirect(reverse('edblog:article'))


# 登录成功后跳转的页面,后端的首页
def article(request):
    if request.method == 'GET':
        page = int(request.GET.get('page', 1))
        articles = Article.objects.all()
        paginator = Paginator(articles, 2)
        page = paginator.page(page)
        return render(request, 'h/article.html', {'page': page})


# 添加文章
def add_article(request):
    if request.method == 'GET':
        return render(request, 'h/add-article.html')

    if request.method == 'POST':
        form = AddArtForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            desc = form.cleaned_data['describe']
            content = form.cleaned_data['content']
            # icon = form.cleaned_data['icon']
            Article.objects.create(title=title, desc=desc, content=content)
            return HttpResponseRedirect(reverse('edblog:article'))
        else:
            return render(request, 'h/add-article.html', {'form': form})


# 删除文章
def del_art_id(request,id):
    if request.method == 'GET':
        Article.objects.filter(pk=id).delete()
        return HttpResponseRedirect(reverse('edblog:article'))


# 修改文章
def update_article(request,id):
    if request.method == 'GET':
        article = Article.objects.filter(pk=id).first()
        return render(request, 'h/update-article.html', {'article': article})

    if request.method == 'POST':
        form = EditArtForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            desc = form.cleaned_data['describe']
            content = form.cleaned_data['content']
            article = Article.objects.filter(pk=id).first()
            article.title = title
            article.desc = desc
            article.content = content
            article.save()
            return HttpResponseRedirect(reverse('edblog:article'))
        else:
            article = Article.objects.filter(pk=id).first()
            return render(request, 'h/update-article.html', {'form': form, 'article': article})










