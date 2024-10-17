import requests

class UserApi:
    def __init__(self, base_url):
        self.base_url = base_url
    
    def login(self, username, password):
        url = f"{self.base_url}/login"
        response = requests.post(url, data={"username": username, "password": password})
        response.raise_for_status()
        return response.json()