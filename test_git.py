import requests
print("Hi Sheik")
print("w")

response = requests.get('https://api.github.com')
print(response.status_code)
print(response.json())