from ubuntu:latest

RUN apt-get update \
	&& apt-get -qq -y install python3-dev \
	&& apt-get -qq -y install python3-pip \
    && pip3 install --upgrade pip

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["app.py"]