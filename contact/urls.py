from django.urls import path
from . import views
urlpatterns=[
    path('contact/new', views.addcontact.as_view(),name='add_new'),
    path('contact/list',views.listcontact.as_view(), name='list'),
    path('contact/detail/<int:pk>/',views.detailcontact.as_view(), name='detail')
]