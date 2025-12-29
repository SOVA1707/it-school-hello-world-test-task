from django.db import models


class LessonDuration(models.IntegerChoices):
    MINUTES_45 = 45, '45 минут'
    MINUTES_90 = 90, '90 минут'


class Lesson(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(
        max_length=250,
        help_text='Название урока',
    )
    started_at = models.DateTimeField(
        help_text='Начало урока',
    )
    duration = models.PositiveSmallIntegerField(
        choices=LessonDuration.choices,
        default=LessonDuration.MINUTES_45.value,
        help_text='Продолжительность урока в минутах',
    )

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return f"Урок «{self.title}» ({self.started_at})"
