from django.conf import settings
from django.db import models
from django.utils import timezone

#models.Model はポストがDjango Modelだという意味で、
#Djangoが、これはデータベースに保存すべきものだと分かるようにしています。
#つまり、DBの構造をmodels.Modelで定義している
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    #関数はインデントされている
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

#migrations "DB名" でマイグレーションファイル（構成ファイル）を作成
#migrate "DB名" で反映させる
