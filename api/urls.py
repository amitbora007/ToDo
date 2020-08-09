from django.conf.urls import url
from api import views

urlpatterns =[
	url(r'^api', views.tlist),
	url(r'^api/(?P<pk>[0-9]+)$', views.todo_detail),
	url(r'^api/admin', views.allUsers_todo),
]