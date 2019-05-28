#!/usr/bin/python
import connexion

options = {"swagger_ui": True}

app = connexion.App(__name__, options=options)
app.add_api('openapi.yml')

# added to prevent bug with jsonify and sorted keys
app.app.config['JSON_SORT_KEYS'] = False


if __name__ == "__main__":
    app.run(port=5000)
