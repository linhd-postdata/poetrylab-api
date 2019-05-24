FROM python:alpine3.7
RUN apk update &&\
    apk upgrade &&\
    apk add --no-cache --virtual=build_deps g++ gfortran &&\
    pip install --no-cache-dir spacy &&\
    python -m spacy download en &&\
    apk del build_deps
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -U pip
RUN pip install --no-cache-dir -r requirements.txt
COPY poetrylab_api ./
EXPOSE 8000
CMD [ "gunicorn", "-b", "0.0.0.0:8000", "--workers", "8", "--timeout", "120", "poetrylab_api.app:app" ]
