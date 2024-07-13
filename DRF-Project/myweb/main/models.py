from django.db import models # django.db 로 부터 models 가져옴
                             # models: Django의 데이터베이스와 관련된 내용을 미리 작성해놓은 도구
                             # 따라서 models.Model이라는 클래스를 상속받아서 그 기능과 필드 설정을 그대로 가져다 쓸 수 있는것

# Create your models here.
class Photo(models.Model): # models.Model을 상속받음
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    descriptions = models.TextField()
    price = models.IntegerField()

'''
필드 설정 종류
CharField: 문자열(길이제한 필요)
IntegerField: 정수
TextField: 문자열(길이제한 필요없음)
DateField: 날짜
DateTimeField: 날짜+시간
FildField: 파일
ImageField: 이미지 파일
ForeignKey: 외래 키(관계)
OneToOneField: 1대1 관계
ManyToManyField: 다대다 관계
'''