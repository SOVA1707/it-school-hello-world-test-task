from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils import timezone

from test_app.models import Lesson, LessonDuration


class LessonModelTest(TestCase):

    def setUp(self):
        self.valid_started_at = timezone.now()

    def test_create_lesson_with_valid_duration_45(self):
        lesson = Lesson.objects.create(
            title='Алгебра',
            started_at=self.valid_started_at,
            duration=LessonDuration.MINUTES_45
        )
        self.assertEqual(lesson.title, 'Алгебра')
        self.assertEqual(lesson.duration, 45)
        self.assertEqual(str(lesson), f'Урок «Алгебра» ({lesson.started_at})')

    def test_create_lesson_with_valid_duration_90(self):
        lesson = Lesson.objects.create(
            title='Физика',
            started_at=self.valid_started_at,
            duration=LessonDuration.MINUTES_90
        )
        self.assertEqual(lesson.title, 'Физика')
        self.assertEqual(lesson.duration, 90)
        self.assertEqual(str(lesson), f'Урок «Физика» ({lesson.started_at})')

    def test_duration_choices_are_limited(self):
        lesson = Lesson(
            title='Химия',
            started_at=self.valid_started_at,
            duration=60,
        )
        with self.assertRaises(ValidationError):
            lesson.full_clean()

    def test_verbose_names(self):
        self.assertEqual(Lesson._meta.verbose_name, 'Урок')
        self.assertEqual(Lesson._meta.verbose_name_plural, 'Уроки')
