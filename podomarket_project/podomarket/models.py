from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator
from .validators import validate_no_special_characters


# Create your models here.

class User(AbstractUser):
    # AbstractUser을 이용해 유저 모델을 만들 예정이니까 관련된 내용 상속받자
    # 이후 settings.py에 가서 AUTH_USER_MODEL을 설정해줘야 하는데 이렇게 해줘야 migration을 했을 때 커스텀 유저 모델을 참조해서 테이블을 만들어주고, allauth가 우리 커스텀 모델을 사용할 수 있다.
    nickname = models.CharField(
        null=True,
        max_length=15,
        unique=True,
        error_messages= {'unqiue': "이미 사용중인 닉네임입니다."},
        validators=[validate_no_special_characters]
        )
    kakao_id = models.CharField(
        null=True,
        max_length=20,
        unique=False,
        validators=[validate_no_special_characters]
        )
    address = models.CharField(
        null=True,
        max_length=40,
        unique=False,
        validators=[validate_no_special_characters],
        )
    
    def __str__(self):
        return self.email # 이거 이메일로 바꿨으니까 tempalte에서 {{user}} 출력하면 이메일로 나온다.
    
