import requests

api_url = "http://127.0.0.1:8000/register"
payload = {
    "username": "testuser",
    "password": "securepassword123"
}

response = requests.post(api_url, json=payload)
print(response.status_code)
print(response.json())
