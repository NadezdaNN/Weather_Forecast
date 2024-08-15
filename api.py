import requests
import json
from sys import argv

name_city = argv

if __name__ == '__main__':    
    for i in name_city[1::]:
        success = requests.post(f'http://127.0.0.1:5000/count/{i}').json()
        print(success)