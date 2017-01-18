import requests
def PyAPI(UserN, PassW):
	""" Input Your Git Username and Password as strings separated by a comma"""
	
	GitAddressRequest = requests.get('https://api.github.com/', auth=(UserN, PassW))
	
	print(GitAddressRequest.status_code)	
	print GitAddressRequest.headers['content-type']
