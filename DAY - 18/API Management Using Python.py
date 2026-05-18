import requests

# GET Method
api_url = "https://reqres.in/api/users?page=1"
#api_url = "https://reqres.in/api/users/2"
#api_url = "https://reqres.in/api/users/25"
responses = requests.get(api_url)   #  ,auth = HTTPBasicAuth('user', 'pass')
print(responses.status_code)
print(responses.json())

print("****************************************")
'''
# POST Method
api_url = "https://reqres.in/api/users"
newvalue = {"first_name": "Arockia", "last_name": "Neo"}
responses = requests.post(api_url, json = newvalue)
print(responses.status_code)
print(responses.json())

# PUT Method

api_url = "https://reqres.in/api/users/1"
responses = requests.get(api_url)
print(responses.json())

toupdate = {"id": 1, "first_name": "Arockia", "last_name": "Neo"}
responses = requests.put(api_url, json=toupdate)
print(responses.json())

# DELETE Method

api_url = "https://reqres.in/api/users/2"
responses = requests.delete(api_url)
print(responses.status_code)
'''

import urllib3

http = urllib3.PoolManager()

url = 'https://google.com'

response = http.request('GET', url)
#print(response.status)
print(response.data)
