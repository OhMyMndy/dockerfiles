FROM python:3.13.2

RUN mkdir -p /app

COPY ./src/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY ./src /app 

USER nobody
ENTRYPOINT [ "/app/app.py" ]
