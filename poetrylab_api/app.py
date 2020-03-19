#!/usr/bin/python
import os
import connexion
from flask_cors import CORS


app = connexion.App(__name__, options={"swagger_ui": True})
app.add_api('openapi.yml')
# Added to prevent bug with jsonify and sorted keys
app.app.config['JSON_SORT_KEYS'] = False
# Adding CORS support
CORS(app.app)

if __name__ == "__main__":  # pragma: no cover
    app.run(port=os.environ.get("PORT", 5000))
