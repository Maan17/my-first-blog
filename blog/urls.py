from django.urls import path
from . import views

<<<<<<< HEAD
urlpatterns = [
    path('', views.post_list, name='post_list'),
=======
urlpatterns=[
    path('',views.post_list,name='post_list'),
>>>>>>> 8ca4e883f97755ff6ce0fc1ba73a7b2dd3f20125
]