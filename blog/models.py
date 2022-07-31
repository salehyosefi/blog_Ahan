from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    STATUS_CHOICES = [('draft', 'پیش نویس'), ('published', 'منتشر شده'), ]
    title = models.CharField(max_length=250, verbose_name='عنوان پست')
    slug = models.SlugField(max_length=250, unique_for_date='publish', allow_unicode=True, verbose_name='آدرس پست')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', verbose_name='نویسنده')
    image = models.ImageField(default='', null=True, blank=True, verbose_name='عکس پست')
    body = models.TextField(verbose_name='محتوا')
    publish = models.DateTimeField(default=timezone.now, verbose_name='زمان انتشار')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name='وضعیت')


    class Meta:
        ordering = ('-publish',)
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.slug])

    #self.publish.year, self.publish.month, self.publish.day,

