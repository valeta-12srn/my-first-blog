from django.contrib import admin

# Register your models here.
from .models import Post

#modelの登録
admin.site.register(Post)
