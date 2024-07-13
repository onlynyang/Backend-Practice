from django.contrib import admin
from .models import Photo # main/models를 불러오고 그 안에있는 Photo 클래스 불러옴
                          # .는 현재 디렉토리, ..은 부모 디렉토리

# Register your models here.
admin.site.register(Photo) # 어드민 페이지에 Photo모델 등록