import requests

class Pace:

    baseurl = 'https://client-api.gopace.xyz/api/v1'

    urls = {
        'serverauth': baseurl + '/app/client-public-auth',
        'getfarecoordinate': baseurl + '/fare/private-estimate',
        'getfareaddress': baseurl + '/fare/private-estimate',
        'trackorder': baseurl + '/order/track',
        'createorder': baseurl + '/order/private-create'
    }
    
    def __init__(self, private_key):
        self.private_key = private_key
        self.token = ""

    def init(self):
        resp = requests.post(self.urls['serverauth'], data = { 'private_key': self.private_key })
        response = resp.json()
        self.token = response['token']

    def getFareEstimateAddress(self, data):
        resp = requests.request('POST', self.urls['getfareaddress'], headers = { 'Authorization': self.token }, data = data)
        response = resp.json()
        return response

    def getFareEstimateCoordinate(self, data):
        resp = requests.post(self.urls['getfarecoordinate'], headers = { 'Authorization': self.token }, data = data)
        response = resp.json()
        return response

    def trackOrder(self, data):
        resp = requests.post(self.urls['trackorder'], headers = { 'Authorization': self.token }, data = data)
        response = resp.json()
        return response

    def createOrder(self, data):
        resp = requests.post(self.urls['createorder'], headers = { 'Authorization': self.token }, data = data)
        response = resp.json()
        return response