import os


ADDONS = {
    "entities": {
        "health": {
            "uri": os.environ.get(
                "NER_HEALTH_URI",
                "http://localhost:8080/api/"
            ),
            "method": "GET",
            "code": 200,
        },
        "endpoint": {
            "uri": os.environ.get(
                "NER_URI",
                "http://localhost:8080/api/rest/process/text"
            ),
            "method": "POST",
            "fields": [{
                "name": "texto",
                "type": str
            }],
            # A specific path in the returned object
            # can also be specified if needed, e.g.,
            # "output": "entities",
            # will return the value of the key "entities"
            # of the JSON response of the endpoint.
        }
    }
}
