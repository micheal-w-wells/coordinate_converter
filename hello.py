from flask import (
    Flask,
)

import sys
import connexion
import connexion_helper

# Create the application instance
app = connexion.App(__name__, specification_dir='./')
# Read the swagger.yml file to configure the endpoints
spec_file_name = 'apispec.yml'
#if not(connexion_helper.load_api_spec(app, spec_file_name)):
	#print("Unable to load api spec file: " + spec_file_name + ", exiting...")
	#sys.exit()

def post_greeting(name: str) -> str:
    return 'Hello {name}'.format(name=name)


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, port=9090, specification_dir='./')
    app.add_api(spec_file_name, arguments={'title': 'Hello World Example'})
    app.run(debug=True)
