from collections.abc import Callable

import pytest
from unittest.mock import patch
from test_app.tasks import (
    handle_lesson_created,
    handle_lesson_updated,
    handle_lesson_deleted,
)


@pytest.mark.parametrize(
    'task,expected_message',
    [
        (handle_lesson_created, 'lesson created'),
        (handle_lesson_updated, 'lesson updated'),
        (handle_lesson_deleted, 'lesson deleted'),
    ],
)
def test_lesson_tasks_log_correctly(
    task: Callable,
    expected_message: str,
):
    lesson_id = 123

    with patch('your_module.logger') as mock_logger:
        task(lesson_id)

        mock_logger.info.assert_called_once_with(expected_message, lesson_id=lesson_id)
