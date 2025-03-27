FROM python:3.13.2-alpine3.21

RUN mkdir -p /app/log
WORKDIR /app

# hadolint ignore=DL3013
RUN pip install --no-cache-dir gunicorn

COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src /app
RUN chown -R nobody:nobody /app

USER nobody
ENTRYPOINT ["gunicorn", "-w", "1", "--bind", "0.0.0.0:8000", "--access-logfile", "/app/log/access.log", "app:app"]
