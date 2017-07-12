FROM python:3.4-alpine

RUN apk -U add tzdata build-base zlib-dev jpeg-dev
RUN cp /usr/share/zoneinfo/UTC /etc/localtime
RUN pip install djangocms-installer

EXPOSE 80

WORKDIR /usr/src/app
COPY . /usr/src/app/
RUN pip install -r requirements.txt

CMD [ "python", "manage.py", "runserver", "0.0.0.0:80"]
