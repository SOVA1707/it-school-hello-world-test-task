from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from test_app.models import Lesson


@receiver(post_save, sender=Lesson)
def handle_lesson_save(sender, instance, created, **kwargs):
    if created:
        print(f"🆕 Урок '{instance.title}' был создан!")
    else:
        print(f"✏️ Урок '{instance.title}' был обновлён!")


@receiver(post_delete, sender=Lesson)
def handle_lesson_delete(sender, instance, **kwargs):
    print(f"🗑️ Урок '{instance.title}' был удалён!")
