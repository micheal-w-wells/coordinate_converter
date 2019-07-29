from flask import (
    Flask,
)

import sys
import connexion
import connexion_helper

spec_file_name = 'apispec.yml'

def post_greeting(name: str) -> str:
    return 'Hello {name}'.format(name=name)


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
# Create the application instance
    app = connexion.FlaskApp(__name__, port=9090, specification_dir='./')
    try:
# Read the swagger.yml file to configure the endpoints
        app.add_api(spec_file_name, arguments={'title': 'Hello World Example'})
        app.run(debug=True)
    except Exception as e:
        print("Unable to start the API server, encountered a problem starting up.")
        print(e.message)
