from django.urls import re_path
from . import views

app_name = 'boards'

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
]
