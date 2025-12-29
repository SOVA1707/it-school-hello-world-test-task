from unittest.mock import patch

import pytest


@pytest.fixture
def m_logger():
    with patch('test_app.tasks.logger') as mock_logger:
        yield mock_logger
