from bottle import response,request
def set(username):
	response.set_cookie("account", username, secret='some-secret-key')

def get():
	return request.get_cookie("account", secret='some-secret-key')

def islogin():
	return request.get_cookie("account", secret='some-secret-key')!=None
		