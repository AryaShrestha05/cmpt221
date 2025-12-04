#!/usr/bin/env python3
"""Script to submit a signup form"""
import urllib.request
import urllib.parse

url = "http://localhost:5001/signup"

data = {
    "FirstName": "Alice",
    "LastName": "Johnson",
    "Email": "alice.johnson@example.com",
    "PhoneNumber": "5551234567",
    "Password": "securepass123"
}

try:
    # Encode the data
    data_encoded = urllib.parse.urlencode(data).encode('utf-8')
    
    # Create request
    req = urllib.request.Request(url, data=data_encoded, method='POST')
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    
    # Submit the form
    with urllib.request.urlopen(req) as response:
        print(f"Status Code: {response.getcode()}")
        print(f"Response URL: {response.url}")
        print("✓ Signup form submitted successfully!")
except Exception as e:
    print(f"Error: {e}")

