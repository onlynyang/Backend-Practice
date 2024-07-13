from django.urls import path
from . import views

urlpatterns = [
    path('', views.photo_list, name='photo_list'), # ''는 루트 주소(http://127.0.0.1:8000)를 가르킨다
                                                   # views.py를 불러와 photo_list함수를 부르고 있음
]