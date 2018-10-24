import requests

headers = {}
headers["Authorization"] = "Bearer <my_token>"

r = requests.get("http://localhost:8000/paradigms", headers=headers)

print(r.text)
