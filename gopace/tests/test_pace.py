import requests
from src.gopace import Pace

class AllTests:

    def TestInit(self):
        self.p = Pace('private_key')
        self.p.init()
        assert self.p.token != ""

    def TestGetFareEstimateAddress(self):
        resp = self.p.getFareEstimateAddress(data = {})
        assert resp.statusCode == 200

    def TestGetFareEstimateCoordinate(self):
        resp = self.p.getFareEstimateCoordinate(data = {})
        assert resp.statusCode == 200

newTest = AllTests()
newTest.TestInit()
newTest.TestGetFareEstimateAddress()
newTest.TestGetFareEstimateCoordinate()