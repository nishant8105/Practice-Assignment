import urllib.request , urllib.parse, urllib.error

url = urllib.request.urlopen('http://127.0.0.1:5000/')

for line in url : 
    print(line.decode().strip())

import requests

url = 'http://127.0.0.1:5000/'

user = {
    'user_agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36'
}

response = requests.get(url=url, headers= user)
print(response)
print(response.status_code)
print(response.headers)
print(response.request.headers)

# print(response.request.headers)