FROM python:3.6-alpine

WORKDIR /app

COPY ./requirements.txt /app
RUN pip install -r requirements.txt

COPY ./app.py /app

HEALTHCHECK --interval=5s CMD wget --spider http://localhost:5000/ || exit 1

CMD ["python", "app.py"]