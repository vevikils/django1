from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin
from . import views
from django.urls import path
from . import views


    
urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

    path('admin/', admin.site.urls),
    
    # Ruta para la vista de login
    path('home/', LoginView.as_view(), name='home'),

    # Ruta para la vista de logout
    path('logout/', LogoutView.as_view(), name='logout'),
    
    # Otras rutas para tus vistas personalizadas
    path('home/', views.home, name='home'),
    path('saludo/', views.saludo, name='saludo'),

    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]




