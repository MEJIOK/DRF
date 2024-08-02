# Generated by Django 5.0.7 on 2024-08-02 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название курса')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='courses/')),
                ('description', models.TextField(max_length=255, verbose_name='Описание курса')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='название')),
                ('description', models.TextField(max_length=250, verbose_name='описание')),
                ('video', models.FileField(blank=True, null=True, upload_to='materials/video')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='materials/image')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
            },
        ),
    ]
