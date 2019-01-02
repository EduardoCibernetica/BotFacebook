import requests

class BaseFacebook:
    HOST = 'https://graph.facebook.com/'
    ENDPOINT = "/oauth/access_token"
    ACTIONAUTH = ""
    # headers = {'Content-Type': 'application/json'}

    def get(self):
        response = requests.get((self.ACTIONAUTH), headers=self.headers)
        return response.json()

    def post(self):
        response = requests.post((self.ACTIONAUTH), headers=self.headers)
        return response.json()

    def put(self):
        response = requests.put((self.ACTIONAUTH), headers=self.headers)
        return response.json()

    def delete(self):
        response = requests.delete((self.ACTIONAUTH), headers=self.headers)
        return response.json()

class FBoauth(BaseFacebook):
    def __init__(self):
        self.ENDPOINT = '/oauth/access_token'
        self.ACTIONAUTH = self.HOST + self.ENDPOINT
