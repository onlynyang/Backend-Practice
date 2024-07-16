from django.urls import path
from . import views

urlpatterns = [
    path('', views.photo_list, name='photo_list'),
    # ''는 루트 주소(http://127.0.0.1:8000)를 가르킨다
    # views.py를 불러와 photo_list함수를 부르고 있음
    path('photo/<int:pk>/', views.photo_detail, name='photo_detail'),
    # photo 뒤에 오는 정수 값을 pk라는 변수로 캡쳐 -> 캡쳐한 pk값을 뷰함수에 전달
    path('photo/new/', views.photo_post, name='photo_post'),
    path('photo/<int:pk>/edit/', views.photo_edit, name='photo_edit'),
]