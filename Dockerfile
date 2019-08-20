FROM alpine:3.10

COPY requirements.txt /flask/

RUN echo "**** install Python ****" && \
    apk add --no-cache python3 gcc musl-dev python3-dev && \
    if [ ! -e /usr/bin/python ]; then ln -sf python3 /usr/bin/python ; fi && \
    \
    echo "**** install pip ****" && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --no-cache --upgrade pip setuptools wheel  && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    \
    echo "**** install dependencies ****" && \
    pip install --no-cache -r /flask/requirements.txt

ENV PATH /opt/conda/bin:$PATH
COPY *.py /flask/
copy ./swagger_server/ /flask/swagger_server/
copy swagger-server.yaml /flask/swagger.yaml
WORKDIR /flask

EXPOSE 5000
CMD 'gunicorn' '--bind' '0.0.0.0:5000' 'wsgi:app' '--worker-class=gevent'