FROM python:alpine3.6
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py ./
COPY swagger.yml ./
EXPOSE 8000
CMD [ "gunicorn", "-b", "0.0.0.0:8000", "--workers", "8", "--timeout", "120", "app:app" ]
