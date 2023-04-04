FROM python:3.10-slim
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 -y
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY ./ /app
RUN pip install --no-cache-dir -r /app/requirements.txt