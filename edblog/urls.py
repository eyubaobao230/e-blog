from django.urls import path

from edblog import views

urlpatterns = [
    # 首页
    path('index/', views.hindex, name='hindex'),
    # 登录
    path('login/', views.login, name='login'),
    # 显示文章
    path('article/', views.article, name='article'),
    # 添加文章
    path('add_article/', views.add_article, name='add_article'),
    # 删除文章
    path('del_art_id/<int:id>/', views.del_art_id, name='del_art_id'),
    # 修改文章
    path('update_article/<int:id>/', views.update_article, name='update_article'),

]