
import requests
from base64 import b64encode

# TypingDNA API credentials
API_KEY = 'your_api_key'
API_SECRET = 'your_api_secret'

# Base URL
API_URL = 'https://api.typingdna.com'

# Basic Auth header
auth_header = b64encode(f"{API_KEY}:{API_SECRET}".encode()).decode()

headers = {
    'Authorization': f'Basic {auth_header}',
    'Content-Type': 'application/x-www-form-urlencoded'
}

def enroll_typing_pattern(user_id, typing_pattern):
    url = f'{API_URL}/auto/{user_id}'
    data = {
        'tp': typing_pattern,
        'quality': 2
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json()

def verify_typing_pattern(user_id, typing_pattern):
    url = f'{API_URL}/auto/{user_id}'
    data = {
        'tp': typing_pattern
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json()

if __name__ == '__main__':
    # Simulated typing pattern string (normally captured via TypingDNA Recorder or JS SDK)
    user_id = 'user123'
    sample_typing_pattern = '0,112,98,89,110,96,104,80,105,91,99,77,103,80,110,90'

    print("Enrolling typing pattern...")
    enroll_result = enroll_typing_pattern(user_id, sample_typing_pattern)
    print("Enroll response:", enroll_result)

    print("\nVerifying typing pattern...")
    verify_result = verify_typing_pattern(user_id, sample_typing_pattern)
    print("Verify response:", verify_result)
