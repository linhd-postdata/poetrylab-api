#!/usr/bin/python
import connexion
from flask_cors import CORS


app = connexion.App(__name__, options={"swagger_ui": True})
app.add_api('openapi.yml')
# Added to prevent bug with jsonify and sorted keys
app.app.config['JSON_SORT_KEYS'] = False
# Adding CORS support
CORS(app.app)

if __name__ == "__main__":
    app.run(port=5000)
