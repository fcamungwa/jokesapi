from python:alpine3.12

WORKDIR /

COPY . /
CMD pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000
