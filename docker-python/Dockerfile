FROM python:3-alpine

WORKDIR /zone

# Change the GitHub link to another one if you need

RUN apk add --no-cache git && \
    pip install git+https://github.com/fatjonfreskina/test-script-python-setup && \ 
    apk del git

ENTRYPOINT [ "test" ]
