from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True)
    
    class Meta:
        verbose_name_plural = 'tags'

    def __str__(self):
        return self.name


