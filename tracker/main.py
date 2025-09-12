from dotenv import load_dotenv

load_dotenv()

import os
import requests

pixela_endpoint = "https://pixe.la/v1/users"

TOKEN = os.getenv("TOKEN")
USERNAME = os.getenv("USERNAME")

user_params = {
  "token": TOKEN,
  "username": USERNAME,
  "agreeTermsOfService": "yes",
  "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
  "id": "graph2",
  "name": "Coding",
  "unit": "commit",
  "type": "int",
  "color":"ajisai"
}

headers = {
  "X-USER-TOKEN":TOKEN
}

graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

print(graph_response.text)