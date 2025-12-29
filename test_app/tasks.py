import structlog
from celery import shared_task


logger = structlog.getLogger('test_app_celery')


@shared_task
def handle_lesson_created(lesson_id):
    logger.info('lesson created', lesson_id=lesson_id)


@shared_task
def handle_lesson_updated(lesson_id):
    logger.info('lesson updated', lesson_id=lesson_id)


@shared_task
def handle_lesson_deleted(lesson_id):
    logger.info('lesson deleted', lesson_id=lesson_id)
