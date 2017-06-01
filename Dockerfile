FROM python:3.6.1-alpine

RUN mkdir -p /app/src

COPY requirements/requirements.txt /app/requirements.txt

RUN pip3 install -r /app/requirements.txt

COPY src /app/src

WORKDIR /app

EXPOSE 4000

CMD ["python", "-m", "src.app"]