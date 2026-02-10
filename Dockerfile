FROM python:3.13-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv venv
RUN uv sync --frozen

COPY ./heart_disease ./heart_disease
COPY ./model ./model

ENV VIRTUAL_ENV=/app/.venv
ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8501
CMD ["streamlit", "run", "./heart_disease/app.py", "--server.port=8501", "--server.address=0.0.0.0"]