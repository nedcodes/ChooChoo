import requests 
from requests.auth import HTTPBasicAuth

response = requests.get('https://api.rtt.io/api/v1/json/search/CHR/to/BCU',
            auth = HTTPBasicAuth('rttapi_nedwallis', 'e655d9e30df45265af6cf40e2ecfe82af23652fc'))

print(response.content)

#WORKING KING SHIZ RIGHT HERE   