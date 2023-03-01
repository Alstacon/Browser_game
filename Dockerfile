FROM python:3.10

WORKDIR /opt
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

EXPOSE 80

CMD gunicorn --config gunicorn.conf.py wsgi:app
