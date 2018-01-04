from . import views
from django.conf.urls import url
from django.urls import path

app_name='agri'
urlpatterns = [
    path('', views.index,name="index"),
    path('second',views.second,name="second"),
    path('submit', views.submit, name='submit'),

#    path('<int:album_id>/', views.detail,name='detail'),
#        path('<int:album_id>/artist/', views.aname,name='aname'),



]
