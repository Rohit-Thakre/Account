from django.urls import path
from . import views

# for media
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),

    path('login/', views.login_method, name='login'),
    path('logout/', views.logout_method, name='logout'),
    path('register/', views.register_method, name='register'),
    path('password_change/', views.password_change_method, name='password_change'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)