FROM python:3.7.0
ENV WORKERS 4
ENV TIMEOUT 300
ENV PORT 5000
RUN apt-get update -y &&\
    apt-get install g++ gfortran libstdc++ -y &&\
    pip install -U pip &&\
    pip install --no-cache-dir numpy &&\
    pip install --no-cache-dir spacy &&\
    python -m spacy download es_core_news_md
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install Cython
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir gunicorn
COPY poetrylab_api ./poetrylab_api
EXPOSE $PORT
CMD sh -c "gunicorn -b 0.0.0.0:${PORT} --workers ${WORKERS} --timeout ${TIMEOUT} poetrylab_api.app:app"
