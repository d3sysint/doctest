import requests
from requests.auth import HTTPBasicAuth
import urllib3

http = urllib3.PoolManager()

# Define the ePO server URL and the API endpoint
epo_server = "https://192.168.85.36:8443"
api_endpoint = "/remote/core.listQueries"

# Define the API headers
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Define your ePO username and password
username = 'admin'
password = 'D3security!'

# Make the API request with Basic Authentication
try:
    response = http.request('GET',f"{epo_server}{api_endpoint}", headers=headers, auth=HTTPBasicAuth(username, password), verify=False)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        response_data = response.json()
        print("API Response:")
        print(response_data)
    else:
        print(f"Error: Received status code {response.status_code}")
        print("Response:", response.text)

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
