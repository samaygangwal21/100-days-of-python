import requests

USERNAME = "samay"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "sflfl93y498hrc3qu4i38",
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)