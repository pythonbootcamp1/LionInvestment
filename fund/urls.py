from django.urls import include, path
from . import views

app_name='fund'

urlpatterns = [
    path('',views.index, name='index'),
    path('fund_list/',views.fund_list, name='fund_list'),
    path('fund_create/',views.fund_create, name='fund_create'),
    path('fund_detail/<int:pk>/', views.fund_detail, name="fund_detail"),
    path("fund_update/<int:pk>/", views.fund_update, name='fund_update'),
    path("fund_delete/<int:pk>/", views.fund_delete, name="fund_delete")
]
