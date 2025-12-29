FROM python:3.14

RUN apt-get update  \
    && apt-get install -y --no-install-recommends gcc \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install poetry

COPY poetry.lock pyproject.toml ./

RUN poetry install --only=main --no-root

COPY . .

RUN poetry run python manage.py collectstatic --noinput

EXPOSE 8080

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]