FROM python:3.13-slim

WORKDIR /app

COPY *.py /app

RUN mkdir -p /app/shared_volume

COPY *.txt /app/shared_volume

CMD ["python", "main_score.py"]

