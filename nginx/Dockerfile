FROM python:3.10-slim

WORKDIR /app

COPY app/ ./app
COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["python", "app/main.py"]

