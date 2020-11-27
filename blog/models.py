from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    author = models.CharField(max_length=100)
    content = models.TextField(max_length=255, blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Published')
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

    class Meta:
        # verbose_name = 'Post'
        # verbose_name_plural = 'Posts'
        ordering = ['-created_at']
