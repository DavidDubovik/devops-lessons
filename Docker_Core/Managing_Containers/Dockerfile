ARG PYTHON_VERSION=3.8

FROM python:${PYTHON_VERSION}

ENV ENV="Local"

WORKDIR /app

COPY app.py .

RUN pip install Flask

EXPOSE 8080

ENTRYPOINT ["python","app.py"]


#FROM alpine:3.18
#
#ENTRYPOINT ["echo", "Hello World", "!!"]
#
#CMD ["Evgeniy"]