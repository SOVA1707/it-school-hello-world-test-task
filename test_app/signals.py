from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Lesson
from .tasks import handle_lesson_created, handle_lesson_updated, handle_lesson_deleted


@receiver(post_save, sender=Lesson)
def handle_lesson_save(sender, instance, created, **kwargs):
    print('AAAAAAAAAA')
    if created:
        handle_lesson_created.delay(instance.id)
    else:
        handle_lesson_updated.delay(instance.id)


@receiver(post_delete, sender=Lesson)
def handle_lesson_delete(sender, instance, **kwargs):
    handle_lesson_deleted.delay(instance.id)