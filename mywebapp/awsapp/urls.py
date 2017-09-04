from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.hello, name = 'hello'),
    url(r'^login/', views.login, name = 'login'),
    url(r'^signup/', views.signup, name = 'signup'),
    url(r'^home/', views.home, name='home'),
    url(r'^dashboard/', views.dashboard, name = 'dashboard'),
]

