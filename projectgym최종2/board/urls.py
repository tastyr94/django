from django.conf.urls import url
from . import views



urlpatterns =[
    url(r'^$', views.main, name='board_main'),
    url(r'^about/$', views.about, name='about'),
    url(r'^board_list/$', views.board_list, name= 'board_list'),
    url(r'^food_list/$', views.food_list, name= 'food_list'),
    #url(r'^list$', views.board_new),
    url(r'^board_list/(?P<pk>\d+)/$', views.board_detail, name = 'board_detail'),
    url(r'^food_list/(?P<pk>\d+)/$', views.food_detail, name = 'food_detail'),
    #url(r'^(?P<board_slug>[-\w]+)/$', views.board_detail, name = 'board_detail'),
    url(r'^board_list/(?P<board_pk>\d+)/comments/new/$', views.comment_new, name='comment_new'),
    url(r'^board_list/(?P<board_pk>\d+)/comments/(?P<pk>\d+)/edit/$', views.comment_edit, name='comment_edit'),
    url(r'^board_list/(?P<board_pk>\d+)/comments/(?P<pk>\d+)/delete/$', views.comment_delete, name='comment_delete'),
]