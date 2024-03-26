# bazna ubuntu slika
FROM ubuntu:20.04

RUN apt update
RUN apt install -y python3-pip
RUN pip3 install pandas scikit_learn

WORKDIR /app

ENTRYPOINT ["python3"]
