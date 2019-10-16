
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('about/', views.about, name='about'),
    path('', views.BooklistView.as_view(), name='homepage'),
    path('contact/', views.Contacts, name='contact'),
    path('post/new/', views.bookCreateView.as_view(), name='book-upload'),
    path('post/<int:pk>/update', views.postUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete', views.postDeleteview.as_view(), name='post_delete'),
    path('user/<str:username>', views.UserpostListview.as_view(), name='user_book'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
