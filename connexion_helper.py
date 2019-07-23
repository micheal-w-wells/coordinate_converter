import connexion

# exists to make troubleshooting the template more friendly for beginners
def load_api_spec(connexion_app, spec_file_path):
	try:
		connexion_app.add_api(spec_file_path)
	except IOError as e:
		print('Was not able to find your spec/swagger file: ' + spec_file_path)
		print(e.message)
	except connexion.exceptions.InvalidSpecification as e:
		print(e.message)
	except Exception as e:
		print("Something unexpected: " + e.message)
	else:
		return True
	finally:
		return False	
