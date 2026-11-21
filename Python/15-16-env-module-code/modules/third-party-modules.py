import requests

city =input("Enter your city")
url =f"https://wttr.in/{city}?format=j1"
response = requests.get(url)
data = response.json()
print('data',data)