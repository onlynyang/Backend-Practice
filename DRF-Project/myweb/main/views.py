from django.shortcuts import render, get_object_or_404, redirect
from .models import Photo
from .forms import PhotoForm

# Create your views here.
def photo_list(request): # 뷰는 데이터베이스에서 데이터를 꺼내 템플릿으로 전달 + 템플릿을 보이게 하는 역할을 한다
    photos = Photo.objects.all() # 모델에서 데이터를 꺼내옴
    return render(request, 'main/photo_list.html', {'photos': photos}) # {}를 활용하면 템플릿으로 데이터를 보낼 수 있음

def photo_detail(request, pk): # url 에서 pk 값을 가져옴
    photo = get_object_or_404(Photo, pk=pk) # 모델로부터 Photo라는 데이터를 pk(장고의 기본 아이디)로 찾아보고 없으면 404에러 반환
    return render(request, 'main/photo_detail.html', {'photo': photo})

def photo_post(request):
    if request.method == "POST": # 요청이 POST인지 확인 / 폼에 있는 버튼이 눌림 = 사진 게시물을 만들어 올리겠다~
        form = PhotoForm(request.POST) # 요청으로 들어온 폼 데이터를 form이라는 변수에 받아옴
        if form.is_valid(): # 형식에 맞게 잘 작성된 데이터인지 검사(Django 제공 기능) -> not valid하면 맨 밑 render로 감 -> 다시 작성하라는 뜻으로 빈 폼페이지 제공 
            photo = form.save(commit=False) # photo 라는 변수에 form에서 나온 데이터를 받아옴
            photo.save() # 데이터 저장
            return redirect('photo_detail', pk=photo.pk) #redirect: 다른페이지로 이동시켜주는 함수, 저장을 마치면 세부 페이지로 이동(새롭게 저장된 pk로)
    else: # POST요청이 아니면 = 새롭게 해당 페이지로 들어온 사용자임 -> 폼을 제공하여 맞이함
        form = PhotoForm() # form 선언
    return render(request, 'main/photo_post.html', {'form': form}) #렌더 함수로 템플릿과 form을 넘겨주어 입력할 수 있는 화면 보여줌