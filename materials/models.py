from django.db import models
from users.models import NULLABLE

class Courses(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование курса')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    preview = models.ImageField(upload_to='courses/', verbose_name='превью', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['name', ]
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование урока')
    description = models.TextField(**NULLABLE, verbose_name='Описание урока')
    image = models.ImageField(upload_to='lessons/%Y/%m/%d', **NULLABLE, verbose_name='Фото продукта')
    courses = models.ForeignKey(Courses, related_name='lesson', on_delete=models.CASCADE, verbose_name='Курс')
    video_file = models.FileField(upload_to=' video/', **NULLABLE, verbose_name="видео урока")

    def __str__(self):
        return f'{self.name} ({self.courses})'

    class Meta:
        ordering = ['name']
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
