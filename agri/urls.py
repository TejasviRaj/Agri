from . import views
from django.conf.urls import url
from django.urls import path

app_name='agri'
urlpatterns = [
    path('', views.index,name="index"),
        path('submit', views.detail, name='detail'),

#    path('<int:album_id>/', views.detail,name='detail'),
#        path('<int:album_id>/artist/', views.aname,name='aname'),



]
