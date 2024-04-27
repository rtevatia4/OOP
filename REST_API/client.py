import requests

class Client(object):
    def __init__(self, url, ssl_verify = True):
        self.url = url
        self.ssl_verify = ssl_verify
    
    def get(self):
        response = requests.get(self.url, verify = self.ssl_verify)
        return response.content

if __name__ == "__main__":
    client_verify = Client('https://self-signed.badssl.com')
    try:
        print(client_verify.get())
    except Exception as e:
        print("Certificate with Verification enabled")
        print("Caught Exception", e)
    
    client_no_verify = Client('https://self-signed.badssl.com', False)
    print(client_no_verify.get())
    

