from email.policy import default

from django.db import models
from django.urls import reverse_lazy

class Human(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя сотрудника')
    surname = models.CharField(max_length=100, verbose_name='Фамилия сотрудника')
    photo = models.ImageField(upload_to='media/%y/%m/%d', verbose_name='Фото')
    date_birth = models.DateField(verbose_name='Дата рождения')
    place_residence = models.CharField(max_length=200, verbose_name='Адрес проживания')
    is_published = models.BooleanField(default=True, verbose_name='Запомнить')
    profession = models.ForeignKey('Profession', on_delete=models.PROTECT, null=True, verbose_name='Профессия')

    def get_absolute_url(self):
        return reverse_lazy('View_project', kwargs={'pk':self.pk})

    class Meta:
        verbose_name='Таблица сотрудников'
        verbose_name_plural='Сотрудники'
        ordering = ['id']

class Profession(models.Model):
        title = models.CharField(max_length=150, db_index=True, verbose_name='Профессия')

        def get_absolute_url(self):
            return reverse_lazy('Profession', kwargs={'profession_id':self.pk})

        class Meta:
            verbose_name = 'Профессия'
            verbose_name_plural = 'Профессии'
            ordering = ['title']