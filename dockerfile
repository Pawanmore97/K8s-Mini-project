FROM python:3.8-slim

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

ENV FALSK_APP = app.py

CMD ["python", "app.py"]