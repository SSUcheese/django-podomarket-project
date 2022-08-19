from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator
from .validators import validate_no_special_characters

class User(AbstractUser):
    # AbstractUser을 이용해 유저 모델을 만들 예정이니까 관련된 내용 상속받자
    # 이후 settings.py에 가서 AUTH_USER_MODEL을 설정해줘야 하는데 이렇게 해줘야 migration을 했을 때 커스텀 유저 모델을 참조해서 테이블을 만들어주고, allauth가 우리 커스텀 모델을 사용할 수 있다.
    nickname = models.CharField(
        max_length=15,
        unique=True,
        null=True,
        validators=[validate_no_special_characters],
        error_messages={'unique': '이미 사용중인 닉네임입니다.'},
    )

    kakao_id = models.CharField(
        max_length=20,
        null=True,
        validators=[validate_no_special_characters],
    )

    address = models.CharField(
        max_length=40,
        null=True,
        validators=[validate_no_special_characters],
    )

    def __str__(self):
        return self.email # 이거 이메일로 바꿨으니까 tempalte에서 {{user}} 출력하면 이메일로 나온다.


class Post(models.Model):
    title = models.CharField(max_length=60)

    item_price = models.IntegerField(validators=[MinValueValidator(1)])

    CONDITION_CHOICES = [
        ('새제품', '새제품'),
        ('최상', '최상'),
        ('상', '상'),
        ('중', '중'),
        ('하', '하'),
    ]
    item_condition = models.CharField(max_length=10, choices=CONDITION_CHOICES, default=None)

    item_details = models.TextField(blank=True)

    image1 = models.ImageField(upload_to='item_pics')

    image2 = models.ImageField(upload_to='item_pics', blank=True)

    image3 = models.ImageField(upload_to='item_pics', blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    is_sold = models.BooleanField(default=False)

    dt_created = models.DateTimeField(auto_now_add=True)

    dt_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
