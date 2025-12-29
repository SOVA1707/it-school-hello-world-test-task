from celery import shared_task


@shared_task
def handle_lesson_created(lesson_id):
    print('lesson created', lesson_id)


@shared_task
def handle_lesson_updated(lesson_id):
    print('lesson updated', lesson_id)


@shared_task
def handle_lesson_deleted(lesson_id):
    print('lesson deleted', lesson_id)
