ARG PYTHON_VERSION=3.8

FROM python:${PYTHON_VERSION}

ENV ENV="Local"

WORKDIR /app

ADD app.py .
ADD docker-logo.png .
ADD https://raw.githubusercontent.com/docker-library/docker/master/README.md .


RUN pip install Flask

EXPOSE 8080

ENTRYPOINT ["python","app.py"]