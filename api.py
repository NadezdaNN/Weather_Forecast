import requests
import json
        
headers = {
    "Content-Type": "application/json"
}
success = requests.post('http://127.0.0.1:5000/count/Moscou', headers=headers).json()
print(success)