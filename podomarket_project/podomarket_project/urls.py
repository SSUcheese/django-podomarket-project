"""podomarket_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from podomarket.views import CustomPasswordChangeView

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    
    # podomarket
    path('', include('podomarket.urls')),
    
    # allauth urls
    path('email-confirmation-done/',
         # 단순히 email 인증 완료를 나타내는 페이지를 만들면 되는 것이기에 그냥 template을 로드한다. 
         TemplateView.as_view(template_name='podomarket/email_confirmation_done.html'),
         name='account_email_confirmation_done'),
    # 아래의 경우를 url 오버라이딩이라 부른다.
    path('password/change/', CustomPasswordChangeView.as_view(), name='account_change_password'),
    path('', include('allauth.urls')),
    # 이거 설정해두고 기호에 맞게 allauth에서 제공하는 url을 사용하면 된다.
]
