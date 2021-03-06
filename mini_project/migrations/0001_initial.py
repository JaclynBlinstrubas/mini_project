# Generated by Django 3.2.4 on 2021-06-25 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('favorite_food', models.CharField(max_length=25)),
                ('loves_pets', models.CharField(max_length=25)),
                ('photo_url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('body', models.CharField(max_length=100)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='mini_project.cat')),
            ],
        ),
    ]
