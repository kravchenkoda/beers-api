FROM python:3.11-slim

ENV PGHOST postgres-db
ENV PYTHONPATH /

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app .

EXPOSE 8000

CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port 8000"]
