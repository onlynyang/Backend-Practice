from django.shortcuts import render, get_object_or_404
from .models import Photo

# Create your views here.
def photo_list(request): # 뷰는 데이터베이스에서 데이터를 꺼내 템플릿으로 전달 + 템플릿을 보이게 하는 역할을 한다
    photos = Photo.objects.all() # 모델에서 데이터를 꺼내옴
    return render(request, 'main/photo_list.html', {'photos': photos}) # {}를 활용하면 템플릿으로 데이터를 보낼 수 있음

def photo_detail(request, pk): # url 에서 pk 값을 가져옴
    photo = get_object_or_404(Photo, pk=pk) # 모델로부터 Photo라는 데이터를 pk(장고의 기본 아이디)로 찾아보고 없으면 404에러 반환
    return render(request, 'main/photo_detail.html', {'photo': photo})