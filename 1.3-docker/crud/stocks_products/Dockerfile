FROM python:3.9

COPY . /src
WORKDIR /src

RUN pip install -r /src/requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:7000"]
