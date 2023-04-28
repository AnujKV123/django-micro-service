FROM python:3.9.0-alpine

#RUN apk add --no-cache curl
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

WORKDIR /app1

COPY /requirements.txt /app1

RUN  pip install -r requirements.txt

COPY . /app1

EXPOSE 8000

CMD [ "python","manage.py","runserver","0.0.0.0:8000" ]