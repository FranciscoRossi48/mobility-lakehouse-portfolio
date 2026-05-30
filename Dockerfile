FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml README.md ./
COPY src ./src
COPY sql ./sql
COPY tests ./tests
COPY Makefile ./

RUN pip install --no-cache-dir -e ".[dev]"

CMD ["make", "pipeline"]

