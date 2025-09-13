from dotenv import load_dotenv

load_dotenv()

import os
import datetime
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

# graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(graph_response.text)

date = datetime.datetime.now()
format_date = date.strftime("%Y%m%d")

# quantity = input("Enter commits:")

# graph_post_params = {
#   "date": format_date,
#   "quantity": quantity
# }

# graph_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"
# graph_post_response = requests.post(url=graph_post_endpoint, json=graph_post_params, headers=headers)

# graph_put_params = {
#   "quantity" : quantity
# }

# graph_put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{format_date}"
# graph_put_response = requests.put(url=graph_put_endpoint, json=graph_put_params, headers=headers)

# graph_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{format_date}"
# graph_delete_response = requests.delete(url=graph_delete_endpoint, headers=headers)

# print(graph_delete_response.text)