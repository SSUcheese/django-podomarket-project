from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    # AbstractUser을 이용해 유저 모델을 만들 예정이니까 관련된 내용 상속받자
    # 이후 settings.py에 가서 AUTH_USER_MODEL을 설정해줘야 하는데 이렇게 해줘야 migration을 했을 때 커스텀 유저 모델을 참조해서 테이블을 만들어주고, allauth가 우리 커스텀 모델을 사용할 수 있다.
    pass