FROM python:3.10

WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY classes classes
COPY data data
COPY templates templates
COPY app.py .
COPY assets.py .

CMD flask run -h 0.0.0.0 -p 80
