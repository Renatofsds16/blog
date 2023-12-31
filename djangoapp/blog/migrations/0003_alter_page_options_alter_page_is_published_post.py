# Generated by Django 4.2.3 on 2023-07-31 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_category_page'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'verbose_name': 'Page', 'verbose_name_plural': ' Pages'},
        ),
        migrations.AlterField(
            model_name='page',
            name='is_published',
            field=models.BooleanField(default=False, help_text='marque se quiser exiibir a pagina'),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, default='', max_length=255, null=True, unique=True)),
                ('excerpt', models.CharField(max_length=255)),
                ('is_published', models.BooleanField(default=False, help_text='marque se quiser exiibir o post')),
                ('content', models.TextField(max_length=255)),
                ('cover', models.ImageField(blank=True, default='', upload_to='post/%Y/%m')),
                ('cover_in_post_content', models.BooleanField(default=True, help_text='se marcado exibira a capa dentro do post')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.category')),
                ('tag', models.ManyToManyField(blank=True, default='', to='blog.tag')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': ' Posts',
            },
        ),
    ]
