FROM python:3.7-slim

WORKDIR /app

ADD . /app

RUN pip install tweepy

RUN pip install google-cloud-pubsub

ENV GOOGLE_APPLICATION_CREDENTIALS="windy-backbone-267320-5dc15516a8ea.json"

CMD [ "python", "my_script_stream.py" ]