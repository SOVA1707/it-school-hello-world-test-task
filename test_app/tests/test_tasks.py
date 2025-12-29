from unittest.mock import Mock, patch
from django.test import TestCase, override_settings
from django.core.exceptions import ValidationError
from django.utils import timezone
from test_app.models import Lesson, LessonDuration


@override_settings(CELERY_TASK_ALWAYS_EAGER=True)
class LessonModelTest(TestCase):

    def setUp(self):
        self.valid_started_at = timezone.now()

    def test_create_lesson_triggers_created_task_and_logging(
        self,
        m_logger: Mock,
    ):
        lesson = Lesson.objects.create(
            title='Алгебра',
            started_at=self.valid_started_at,
            duration=LessonDuration.MINUTES_45
        )

        self.assertEqual(lesson.title, 'Алгебра')
        self.assertEqual(lesson.duration, 45)
        self.assertEqual(str(lesson), f'Урок «Алгебра» ({lesson.started_at})')

        m_logger.info.assert_called_with('lesson created', lesson_id=lesson.id)

    @patch("test_app.tasks.logger")
    def test_update_lesson_triggers_updated_task_and_logging(self, mock_logger):
        lesson = Lesson.objects.create(
            title='Физика',
            started_at=self.valid_started_at,
            duration=LessonDuration.MINUTES_90
        )
        mock_logger.reset_mock()  # сброс вызовов после создания

        lesson.title = 'Новая физика'
        lesson.save()

        mock_logger.info.assert_called_with('lesson updated', lesson_id=lesson.id)

    @patch("test_app.tasks.logger")
    def test_delete_lesson_triggers_deleted_task_and_logging(self, mock_logger):
        lesson = Lesson.objects.create(
            title='Химия',
            started_at=self.valid_started_at,
            duration=LessonDuration.MINUTES_45
        )

        lesson_id = lesson.id
        lesson.delete()

        mock_logger.info.assert_called_with('lesson deleted', lesson_id=lesson_id)

    def test_duration_choices_are_limited(self):
        lesson = Lesson(
            title='Невалидный урок',
            started_at=self.valid_started_at,
            duration=60,  # недопустимое значение
        )
        with self.assertRaises(ValidationError):
            lesson.full_clean()

    def test_verbose_names(self):
        self.assertEqual(Lesson._meta.verbose_name, 'Урок')
        self.assertEqual(Lesson._meta.verbose_name_plural, 'Уроки')