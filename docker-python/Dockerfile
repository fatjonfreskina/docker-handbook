FROM python:3-alpine

WORKDIR /zone

# Change the GitHub link to another one if you need

RUN apk add --no-cache git && \
    pip install git+https://github.com/fhsinchy/rmbyext.git#egg=rmbyext && \ 
    apk del git

ENTRYPOINT [ "rmbyext" ]
