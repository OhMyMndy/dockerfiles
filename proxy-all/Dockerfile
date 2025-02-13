FROM python:3.13.2

RUN pip install Flask requests beautifulsoup4 Pygments

RUN mkdir -p /app
COPY ./src /app 

USER nobody
ENTRYPOINT [ "/app/app.py" ]
