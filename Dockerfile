FROM python:3.12-slim

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENV PORT=8080
EXPOSE 8080

CMD ["bash", "-lc", "reflex run --env prod --backend-host 0.0.0.0 --backend-port ${PORT}"]
