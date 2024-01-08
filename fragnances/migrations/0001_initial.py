# Generated by Django 3.2.16 on 2024-01-08 18:16

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Fragnance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('brand', models.CharField(max_length=35)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='fragnances/', verbose_name='Изображение духов')),
                ('size', models.CharField(max_length=50)),
                ('available', models.BooleanField(default=True)),
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
            ],
            options={
                'verbose_name': 'Духи',
                'verbose_name_plural': 'Духи',
            },
        ),
        migrations.CreateModel(
            name='FragnanceComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('fragnance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='fragnances.fragnance')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Отзывы про духи',
            },
        ),
        migrations.CreateModel(
            name='ShoppingList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fragnance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shopping_recipe', to='fragnances.fragnance', verbose_name='Духи')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shopping_recipe', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Список для покупок',
                'verbose_name_plural': 'Списки для покупок',
                'abstract': False,
                'default_related_name': 'shopping_recipe',
                'unique_together': {('user', 'fragnance')},
            },
        ),
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fragnance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourites_fragnances', to='fragnances.fragnance', verbose_name='Духи')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourites_fragnances', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Избранные духи',
                'verbose_name_plural': 'Избранные духи',
                'abstract': False,
                'default_related_name': 'favourites_fragnances',
                'unique_together': {('user', 'fragnance')},
            },
        ),
    ]
