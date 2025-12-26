# Dockerfile
FROM python:3.14

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.8.3 \
    POETRY_HOME=/opt/poetry \
    POETRY_VENV=/opt/poetry-venv \
    POETRY_CACHE_DIR=/opt/.cache

RUN python3 -m venv $POETRY_VENV && \
    $POETRY_VENV/bin/pip install -U pip setuptools && \
    $POETRY_VENV/bin/pip install poetry==$POETRY_VERSION

ENV PATH="$POETRY_VENV/bin:$PATH"

WORKDIR /app

COPY poetry.lock pyproject.toml ./
RUN poetry install --only=main --no-root

COPY . .

RUN poetry run python manage.py collectstatic --noinput

EXPOSE 8080

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8080"]
