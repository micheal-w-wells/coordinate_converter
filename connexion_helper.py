import connexion

# exists to make troubleshooting the template more friendly for beginners
def load_api_spec(connexion_app, spec_file_path):
	try:
		connexion_app.add_api(spec_file_path)
		return True
	except IOError as e:
		print('Was not able to find your spec/swagger file: ' + spec_file_path)
		return False
