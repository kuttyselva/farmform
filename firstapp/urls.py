from django.conf.urls import url
from firstapp import views
import django.contrib.auth.views
from firstapp.views import login,index
from django.views.generic import TemplateView
urlpatterns=[
    url('',views.index,name='index'),
    url('help/',views.help,name='help'),
    url('connection/',views.login,name= 'login.html'),
    url('login/',views.login, name = 'login')

]
