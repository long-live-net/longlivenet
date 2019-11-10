from django.db import models


class Topic(models.Model):
    CATEGORY_CHOICES = (
                ('I', 'INFO'),
                ('S', 'SERVICE'),
                ('W', 'WORK'),
                ('T', 'TECH'),
            )
    release_day = models.DateField(verbose_name='発表日')
    category = models.CharField(
                verbose_name='カテゴリ',
                max_length=1,
                choices=CATEGORY_CHOICES
            )
    title = models.CharField(verbose_name='タイトル', max_length=128)
    content = models.TextField(verbose_name='本文', max_length=4096)
    photo = models.ImageField(
                verbose_name='イメージ',
                upload_to='tphotos',
                blank=True,
                null=True
            )
    link = models.URLField(
                verbose_name='関連リンク',
                blank=True,
                null=True
            )
    votes = models.IntegerField(verbose_name='いいね数', default=0)
    create_date = models.DateTimeField(verbose_name='登録日', auto_now=True)

    def __str__(self):
        return self.title
