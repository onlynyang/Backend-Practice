from django import forms
from .models import Photo

class PhotoForm(forms.ModelForm): #장고의 기본 ModelForm을 상속받아 아래 필드값을 입력받는 폼
    class Meta:
        model = Photo
        fields = (
            'title',
            'author',
            'image',
            'descriptions',
            'price',
        )
