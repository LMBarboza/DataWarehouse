FROM python:3.12-slim 
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1
ENV UV_SYSTEM_PYTHON=true

WORKDIR /app


COPY pyproject.toml .

RUN uv pip install --system .

COPY utils/ /app/utils/
COPY queries/ /app/queries/
COPY main.py .

CMD ["uv", "run", "main.py", "--create_db"]
