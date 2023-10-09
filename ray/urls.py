from django.urls import path

from . import views

urlpatterns = [
    path('', views.page1view, name='page1'),
    path('page2/', views.page2view, name='page2'),
    path('page3/', views.page3view, name='page3'),
    path('page4/', views.page4view, name='page4'),
    path('page5/', views.page5view, name='page5'),
]
