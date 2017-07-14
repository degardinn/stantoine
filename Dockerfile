FROM python:3.4-alpine

RUN apk -U add tzdata build-base zlib-dev jpeg-dev

ARG TIMEZONE='UTC'

RUN cp /usr/share/zoneinfo/$TIMEZONE /etc/localtime
RUN pip install djangocms-installer

EXPOSE 80

WORKDIR /usr/src/app
COPY . /usr/src/app/
RUN pip install -r requirements.txt

CMD [ "python", "manage.py", "runserver", "0.0.0.0:80"]
