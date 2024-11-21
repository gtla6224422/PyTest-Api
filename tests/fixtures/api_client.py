# tests/fixtures/api_client.py
import pytest
import requests
import yaml

@pytest.fixture(scope="session")
def api_client():
    with open("config/test_config.yaml", "r") as file:
        config = yaml.safe_load(file)
    base_url = config["base_url"]
    
    class APIClient:
        def __init__(self, base_url):
            self.base_url = base_url
        
        def post(self, endpoint, data):
            url = f"{self.base_url}/{endpoint}"
            response = requests.post(url, json=data)
            return response
    
    return APIClient(base_url)

@pytest.fixture(scope="session")
def test_data():
    with open("config/test_data.yaml", "r") as file:
        return yaml.safe_load(file)["test_cases"]