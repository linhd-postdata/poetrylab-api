FROM python:alpine3.7
ENV WORKERS 4
ENV TIMEOUT 120
ENV PORT 5000
# We need do downgrade pip due to a bug with alpine in more recent versions
RUN apk update &&\
    apk upgrade &&\
    apk add --no-cache g++ gfortran libstdc++ &&\
    pip install -U pip &&\
    pip install --no-cache-dir numpy &&\
    pip install --no-cache-dir spacy &&\
    python -m spacy download es_core_news_md
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir gunicorn
COPY poetrylab_api ./poetrylab_api
EXPOSE $PORT
CMD sh -c "gunicorn -b 0.0.0.0:${PORT} --workers ${WORKERS} --timeout ${TIMEOUT} poetrylab_api.app:app"
