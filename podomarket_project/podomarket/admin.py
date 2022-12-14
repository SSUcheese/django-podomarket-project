from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.


from .models import User, Post

admin.site.register(User, UserAdmin)
UserAdmin.fieldsets += ('Custom fields', {'fields': ('nickname', 'kakao_id', 'address',)}),

admin.site.register(Post)