import os


ADDONS = {
    "entities": {
        "health": {
            "uri": os.environ.get(
                "NER_URI",
                "http://localhost:8080/api"
            ),
            "method": "GET",
            "code": 200,
        },
        "endpoint": {
            "uri": os.environ.get(
                "NER_URI",
                "http://localhost:8080/api/rest/process/processpost"
            ),
            "method": "POST",
            "fields": [{
                "name": "texto",
                "type": str
            }],
            "output": "entities",
        }
    }
}
