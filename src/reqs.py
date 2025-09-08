import requests

# Base URL of your local API
url = "http://localhost:8000/predict"

# Query parameters (adjust to whatever your API expects)
params = {"text": "hello world"}

try:
    # Make the GET request
    response = requests.get(url, params=params)

    # Check if the request was successful
    response.raise_for_status()  # raises an exception for 4xx/5xx responses

    # Print JSON response
    print("Response JSON:")
    print(response.json())

except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
