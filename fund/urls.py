from django.urls import include, path
from . import views

app_name='fund'

urlpatterns = [
    path('',views.index, name='index'),
    path('fund_list/',views.fund_list, name='fund_list'),
    path('fund_create/',views.fund_create, name='fund_create')
]
