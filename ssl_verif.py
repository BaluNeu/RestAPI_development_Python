import requests
from ssl import SSLError, SSLCertVerificationError
import json


class Client(object):

    def __init__(self,url:str,ssl_verify:bool=True, cert_path:str=None):
        self.url = url
        self.ssl_verify = ssl_verify

        if cert_path:
            self.ssl_verify = cert_path
        else:
            self.ssl_verify = ssl_verify
        
    def get(self):
        response = requests.get(self.url,verify=self.ssl_verify)
        return json.loads(response.content)
    


if __name__ == '__main__':
    client = Client('https://api.met.no/weatherapi/airqualityforecast/0.1/stations')
    stations = client.get()
    print('Name of the first station (in alphabetical order) = ' + stations[0].get("name"))
    
# if __name__ == '__main__':
#     # client_verify_cert = Client('https://self-signed.badssl.com', cert_path=str("badssl-com.pem"))
#     client_verify_cert = Client('https://self-signed.badssl.com',ssl_verify=True, cert_path=str("badssl-com.pem"))




    # try:
    #     print(client_verify_cert.get())
    # except Exception as e:
    #     print("Client with Verification Enabled")
    #     print("Caught exception", e)
    #     print("\n")

    # client_verify = Client('https://self-signed.badssl.com')
    # client_no_verify = Client('https://self-signed.badssl.com', ssl_verify=False)
    # print(client_no_verify.get())
    # print(client.get())