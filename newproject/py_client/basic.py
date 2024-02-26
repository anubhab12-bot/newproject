import requests


# endpoint = "https://httpbin.org/status/200"
# endpoint = "https://httpbin.org/anything" # rest api endpoint
endpoint = "http://localhost:8000/api/"
get_response = requests.get(endpoint, json = {"query" : "hello world"}) # http get requests
print(get_response.text) # print raw text code
# print(get_response.json()) 
print(get_response.status_code)
