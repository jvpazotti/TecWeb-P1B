from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete',views.delete,name='delete'),
    path('edit',views.edit,name='edit'),
    path('list_of_tags',views.list_of_tags,name='list_of_tags'),
    path('all_tags',views.all_tags,name='all_tags')
]