FROM python:3.7-alpine

COPY . /app
WORKDIR /app
RUN pip install -r /app/requirements.txt
EXPOSE 5050
ENTRYPOINT["python"]
CMD["main.py"]
