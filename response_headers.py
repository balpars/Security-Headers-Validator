import requests

url=input()

response = requests.get(url)
headers = response.headers

print(headers)