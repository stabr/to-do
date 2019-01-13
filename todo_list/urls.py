"""todoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

app_name = 'todo_list'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^delete/(?P<list_id>[0-9]*)$', views.delete, name="delete"),
    url(r'^cross_off/(?P<list_id>[0-9]*)$', views.cross_off, name="cross_off"),
    url(r'^uncross/(?P<list_id>[0-9]*)$', views.uncross, name="uncross"),
    url(r'^edit/(?P<list_id>[0-9]*)$', views.edit, name="edit"),
]
