from django.shortcuts import render

# Create your views here.
def photo_list(request): # 뷰는 데이터베이스에서 데이터를 꺼내 템플릿으로 전달 + 템플릿을 보이게 하는 역할을 한다
    return render(request, 'main/photo_list.html', {})
