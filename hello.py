from flask import (
    Flask,
    render_template
)

import sys
import connexion
import connexion_helper

# Create the application instance
app = connexion.App(__name__, specification_dir='./')
# Read the swagger.yml file to configure the endpoints
spec_file_name = 'apispec.yml'
if not(connexion_helper.load_api_spec(app, spec_file_name)):
	print("Unable to load api spec file: " + spec_file_name + ", exiting...")
	sys.exit()

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')

@app.route('/example')
def exampleOperation():
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return:        the rendered template 'home.html'
    """
    return 200

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)
