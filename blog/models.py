from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from unidecode import unidecode
from django.urls import reverse

User = get_user_model()

class Post(models.Model):
    STATUS_CHOICES = (
        ('published', 'Опубликован'),
        ('draft', 'Черновик')
    )

    title = models.CharField(max_length=200, unique=True, verbose_name = 'Заголовок')
    slug = models.SlugField(max_length=200, unique=True, editable=False, verbose_name = 'Слаг')
    category = models.ForeignKey('Categories', related_name='posts', on_delete=models.CASCADE, null=True, verbose_name='Категория')
    content = models.TextField()
    image = models.ImageField(upload_to="post_images/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    status = models.CharField(choices=STATUS_CHOICES, default='draft', verbose_name='Статус') 


    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.title))

        super().save(*args, **kwargs)


class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    slug = models.SlugField(editable=False, verbose_name='Слаг')

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.name))

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("blog:category_posts", kwargs={"category_slug": self.slug})
    
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        db_table = 'blog_categories'
