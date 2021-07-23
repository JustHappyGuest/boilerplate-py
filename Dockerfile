# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /app
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8085
RUN apk update && \
    apk add --virtual build-deps gcc python3-dev musl-dev && \
    apk add postgresql-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8085
COPY . .
CMD ["flask", "run"]