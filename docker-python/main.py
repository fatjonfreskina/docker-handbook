# Test dockerized python script
# Build with "docker build -t <name:latest> ."
# Then run the container with "docker container run <id>"
import requests

try: 
    r = requests.get('https://httpbin.org/get')
    print(f"Status code: {r.status_code}")
except:
    print("Error")