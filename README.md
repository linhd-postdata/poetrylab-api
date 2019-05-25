# Poetrylab API

The PoetryLab API is a REST API that provides an analysis endpoint to extract information about the poems. Currently, only two methdos are supported:

- `scansion`, to extract information about the verse metrics.
- `enjabment`, to check for enjabments.

Only the method POST is allowed at the `/analysis` endpoint.
A playground interface documenting the API can be found at the `/ui` endpoint.

## Deployment
Since `connexion` builds a Flask application from our OpenAPI specification, you can use any WSGI compliant application server. We have tested both `gunicorn` and `uwsgi` and both work fine.
```bash
$ pip install -e .
$ gunicorn poetrylab_api.app:app
```
Alternatively, you can also use the Docker file provided, which exposes the server at the port 5000.
```bash
docker build --tag linhdpostdata/poetrylab-api .
```
Stable versions will be published in the Docker Hub under the `linhdpostdata/poetrylab-api` name.
```bash
$ docker run -p "5000:5000" linhdpostdata/poetrylab-api
```

## Development

For development, you need to install the package in development mode, and then run `connecion run` command. Alternatively, you could also install the `requirements.txt`.
```bash
$ pip install -e .
$ connexion run poetrylab_api/openapi.yml
```

## Tests

To execute the battery tests, you need to install the package in development mode.
```bash
$ pip install -e .
$ python setup.py test
```