from django.contrib import admin

# Register your models here.

# Taskモデルをインポート
from .models import Question

# 管理サイトへのモデルを登録
admin.site.register(Question)