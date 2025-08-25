FROM alpine:3.18

RUN apk add python3 py3-pip py3-requests

WORKDIR /app

COPY . /app

RUN pip install -r /app/requirements.txt

CMD ["python3", "app.py"]
