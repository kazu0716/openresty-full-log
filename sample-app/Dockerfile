FROM python:3.8-slim-buster

LABEL maintainer="kazu0716"

WORKDIR /usr/local/src/

COPY ./sample-app/main.py /usr/local/src/main.py 
COPY ./sample-app/res_body.json.gz /usr/local/src/res_body.json.gz
COPY ./sample-app/requirements.txt /usr/local/src/requirements.txt

RUN pip3 install -r /usr/local/src/requirements.txt

CMD ["/usr/local/bin/python", "main.py"]