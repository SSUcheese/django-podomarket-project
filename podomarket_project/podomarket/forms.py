from dataclasses import field
from django import forms
from django import forms
from .models import User, Post

# 해당 form의 내용 구성이 끝나면 settings.py에 가서 우리의 SignupForm을 회원가입 때 사용하겠다고 선언해야 한다.
class SignupForm(forms.ModelForm):
    class Meta:
        model = User # 이거는 form 생성할 때 사용하는 model
        fields = ["nickname", "kakao_id", "address"] # 이거는 form에서 받아올 내용들 빈칸 선별
        
        def signup(self, request, user):
            # 위에 signup 옆에 괄호를 통해서 form 데이터를 user 필드에 할당한 다음, 아래 코드 흐름을 통해 user에 데이터를 넣어준다.
            user.nickname = self.cleaned_data['nickname']
            user.kakao_id = self.cleaned_data['kakao_id']
            user.address = self.cleaned_data['address']
            user.save()

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "item_price",
            "item_condition",
            "item_details",
            "image1",
            "image2",
            "image3",
        ]
        widgets = {
            "item_condition": forms.RadioSelect, # 이렇게 하면 기본값으로 사용되는 select 대신에 radioselect 위젯이 사용된다.
        }