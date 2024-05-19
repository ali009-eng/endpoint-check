import requests
from urllib.parse import urljoin

# Define the base URL of the website
base_url = "https://example.com"

# Define the list of endpoints to check
endpoints = [
    "/login",
    "/dashboard",
    "/profile",
    "/admin",
    # Add more endpoints here
]

# Define the authentication credentials
username = "your_username"
password = "your_password"

# Define the headers for authenticated requests
auth_headers = {
    "Authorization": "Basic <base64_encoded_credentials>"
}

# Function to check the endpoint
def check_endpoint(endpoint, require_auth=False):
    url = urljoin(base_url, endpoint)
    
    # Send a GET request to the endpoint
    if require_auth:
        response = requests.get(url, headers=auth_headers)
    else:
        response = requests.get(url)
    
    # Check the response status code
    if response.status_code == 200:
        print(f"{endpoint} is accessible")
    elif response.status_code == 401:
        print(f"{endpoint} requires authentication")
    elif response.status_code == 403:
        print(f"{endpoint} requires authorization")
    else:
        print(f"{endpoint} returned an unexpected status code: {response.status_code}")

# Check each endpoint
for endpoint in endpoints:
    check_endpoint(endpoint)
    check_endpoint(endpoint, require_auth=True)