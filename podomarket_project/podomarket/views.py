from django.shortcuts import render
from django.urls import reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)
from .models import User, Post

from allauth.account.views import PasswordChangeView

# Create your views here.

class IndexView(ListView):
    model = Post
    template_name = 'podomarket/index.html'
    context_object_name = "posts"
    paginate_by = 8
    ordering = ["-dt_updated"]
    
class PostDetailListView(DetailView):
    model = Post
    template_name = "podomarket/post_detail.html"
    pk_url_kwarg = "post_id"

# class PostCreateView(CreateView):
    

# 비밀번호 변경을 하고 홈펭이지로 리디렉트되게 하는 기능은 settings에서 만질 수 없다.
# 이를 구현하기 위해선 아래와 같이 allauth의 passwordchangeview를 상속받아서 리디렉트 url을 설정해 주는 get_success_url 메소드를 오버라이드하는 방식으로 접근한다.
# 또한 class 이름을 custompassword...로 설정했으니 urls.py에 가서 해당 class를 사용하도록 url 패턴을 정의해주면 된다.
class CustomPasswordChangeView(PasswordChangeView):
    # 비밀번호 컨펌 확인 페이지가 아닌 홈페이지로 갈 수 있게 오버라이드한다.
    def get_success_url(self):
        return reverse('index')
    