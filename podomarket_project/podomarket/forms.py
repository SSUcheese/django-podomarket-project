from django import forms
from django import forms
from .models import User

# 해당 form의 내용 구성이 끝나면 settings.py에 가서 우리의 SignupForm을 회원가입 때 사용하겠다고 선언해야 한다.
class SignupForm(forms.ModelForm):
    class Meta:
        model = User # 이거는 기본적으로 제공해주는 내용들
        fields = ["nickname", "kakao_id", "address"]
        
        def signup(self, request, user):
            # 위에 signup 옆에 괄호를 통해서 form 데이터를 user 필드에 할당한 다음, 아래 코드 흐름을 통해 user에 데이터를 넣어준다.
            user.nickname = self.cleaned_data['nickname']
            user.kakao_id = self.cleaned_data['kakao_id']
            user.address = self.cleaned_data['address']
            user.save()
            