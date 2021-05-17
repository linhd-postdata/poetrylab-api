# Poetrylab API

The PoetryLab API is a REST API that provides an analysis endpoint to extract information about the poems. Currently, only two methdos are supported:

- `scansion`, to extract information about the verse metrics.
- `enjambment`, to check for enjambments.

Only the method POST is allowed at the `/analysis` endpoint.
A playground interface documenting the API can be found at the `/ui` endpoint.

## Example

Let's take as an example the following poem: 
```
La cebolla es 
cerrada y pobre:
escarcha de tus días
y de mis noches.
Hambre y 
hielo negro y 
grande y redonda.
```

### Enjambment output:
```json
{
  "enjambment": {
    "4": {
      "type": "sirrematic_relation_words_conjunction",
      "on": [
        "CONJ",
        "NOUN"
      ]
    },
    "5": {
      "type": "sirrematic_relation_words_conjunction",
      "on": [
        "CONJ",
        "ADJ"
      ]
    }
  }
}
```
The key is the number of the verse where an enjambment is taking place, followed
by the enjambment type.

### Scansion output
```json
{
  "scansion": [
    {
      "tokens": [
        {
          "word": [
            {
              "syllable": "La",
              "is_stressed": false,
              "is_word_end": true
            }
          ],
          "stress_position": 0
        },
        {
          "word": [
            {
              "syllable": "ce",
              "is_stressed": false
            },
            {
              "syllable": "bo",
              "is_stressed": true
            },
            {
              "syllable": "lla",
              "is_stressed": false,
              "has_synalepha": true,
              "is_word_end": true
            }
          ],
          "stress_position": -2
        },
        ...
      ],
      "phonological_groups": [
        {
          "syllable": "La",
          "is_stressed": false,
          "is_word_end": true
        },
        {
          "syllable": "ce",
          "is_stressed": false
        },
        {
          "syllable": "bo",
          "is_stressed": true
        },
        {
          "syllable": "llaes",
          "is_stressed": true,
          "synalepha_index": [
            2
          ],
          "is_word_end": true
        }
      ],
      "rhythm": {
        "stress": "--++-",
        "type": "pattern",
        "length": 5,
        "length_range": {
          "min_length": 5,
          "max_length": 6
        }
      }      
    },
    ...
  ]
}
```

If the `rhyme_analysis` option is set to `True`, the stanza information is added
to the output:
```json
      "structure": "septilla",
      "rhyme": "-",
      "ending": "",
      "ending_stress": 0,
      "rhyme_type": "",
      "rhyme_relaxation": null
```

For an in-dept explanation of the scansion output, please refer to the rantanplan 
documentation at https://rantanplan.readthedocs.io/en/latest/readme.html

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