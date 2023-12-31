from django.db import models
from ultils.rands import slugify_new
from django.contrib.auth.models import User
from ultils.image import resize_image


class Tag(models.Model):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
    name = models.CharField(max_length=255)
    slug = models.SlugField(
        unique=True, default=None, null=True,
        blank=True, max_length=255,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.name)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=255)
    slug = models.SlugField(
        unique=True, default=None, null=True,
        blank=True, max_length=255,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.name)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class Page(models.Model):
    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = ' Pages'
    title = models.CharField(max_length=255)
    slug = models.SlugField(
        unique=True, default="", null=True,
        blank=True, max_length=255,
    )
    is_published = models.BooleanField(
        default=False,
        help_text='marque se quiser exiibir a pagina'
    )
    content = models.TextField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.title)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title


class Post(models.Model):
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = ' Posts'
    title = models.CharField(max_length=255)
    slug = models.SlugField(
        unique=True, default="", null=True,
        blank=True, max_length=255,
    )
    excerpt = models.CharField(max_length=255)
    is_published = models.BooleanField(
        default=False,
        help_text='marque se quiser exiibir o post'
    )
    content = models.TextField(max_length=255)
    cover = models.ImageField(upload_to='post/%Y/%m', blank=True, default='')
    cover_in_post_content = models.BooleanField(
        default=True, help_text='se marcado exibira a capa dentro do post',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        blank=True, null=True, default=None,
        related_name='post_created_by'
    )
    update_at = models.DateTimeField(auto_now=True)
    update_by = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        blank=True, null=True, default=None, related_name='post_update_by'
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        null=True, blank=True, default=None
    )
    tag = models.ManyToManyField(Tag, blank=True, default='')

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.title)
        current_cover_name = str(self.cover.name)
        super_save = super().save(*args, **kwargs)
        cover_changed = False

        if self.cover:
            cover_changed = current_cover_name != self.cover.name

        if cover_changed:
            resize_image(self.cover, 900)
        # return super().save(*args, **kwargs)
        return super_save
