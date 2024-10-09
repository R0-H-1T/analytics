FROM python:3.10

WORKDIR /analytics

COPY ./requirements.txt /analytics/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /analytics/requirements.txt

COPY ./app /analytics/app

EXPOSE 80

CMD ["uvicorn", "app.app:app", "--port", "80", "--host", "0.0.0.0"]
