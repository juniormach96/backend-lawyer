from blog.models.categories import Category
from blog.models.tags import Tag
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone

STATUS = ((0, "Não Publicado"), (1, "Publicado"))

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    status = models.IntegerField(choices=STATUS, default=-2)
    tags = models.ManyToManyField(Tag, related_name='posts')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('post_detail', args=[str(self.slug)])
