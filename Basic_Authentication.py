import requests
from requests.auth import HTTPBasicAuth

# Replace with your ePO server details
epo_server = 'Replace me with epo server'
username = 'Replace me with username '
password = 'Replace me with password'

# The endpoint for authentication or any ePO API call
endpoint = f'{epo_server}/remote/core.listQueries'

# Making a GET request to the ePO server with basic auth
response = requests.get(endpoint, auth=HTTPBasicAuth(username, password), verify=False)

# Check if the request was successful
if response.status_code == 200:
    print("Connection successful!")
    print("Response:", response.text)
else:
    print(f"Failed to connect. Status code: {response.status_code}")
    print("Response:", response.text)

# It's also good practice to close the session if you're using one