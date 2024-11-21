import urllib.request
 import requests

 opener = urllib.request.build_opener()
google = opener.open("https://ua.sinoptik.ua/")
print(google.read())
print("=============================================")
response = requests.get("https://ua.sinoptik.ua/")
print(response.content)
print(f"Datatype - {type(response.content)}")
print("=============================================")
print(response.text)
print(f"Datatype - {type(response.text)}")