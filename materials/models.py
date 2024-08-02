from django.db import models


NULLABLE = {"blank": True, "null": True}


class Course(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название курса")
    preview = models.ImageField(upload_to='courses/', **NULLABLE)
    description = models.TextField(max_length=255, verbose_name="Описание курса")

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=255, verbose_name='название')
    description = models.TextField(max_length=250, verbose_name='описание')
    video = models.FileField(upload_to='materials/video', **NULLABLE)
    preview = models.ImageField(upload_to='materials/image', **NULLABLE)

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
