import requests
import json

class Client:
    def __init__(self, url, ssl_verify=True):
        self.url = url
        self.ssl_verify = ssl_verify
    
    def get(self):
        body = requests.get(self.url, verify=self.ssl_verify).content
        return json.loads(body)

client = Client('https://api.met.no/weatherapi/airqualityforecast/0.1/stations')

stations = client.get()
print("Name of the first station:", stations[0].get('name'))