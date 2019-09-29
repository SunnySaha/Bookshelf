
from django.urls import path
from . import views
urlpatterns = [

    path('', views.about, name='about'),
    path('new', views.BooklistView.as_view(), name='homepage'),
]
