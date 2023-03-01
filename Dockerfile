FROM python:3.10

WORKDIR /opt
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

EXPOSE 80

CMD flask run -h 0.0.0.0 -p 80


