import requests
import json

class OnenoteCommunicator():

    def __init__(self):
        self.s = requests.Session()

        self.BaseUrl = 'https://www.onenote.com/api/v1.0/me/notes'

        self.header = {'Authorization': ""}

    def getAccessToken(self):

        url = 'xxxxxxxxxxxx url to recive auth xxxxxxxxxxxxxxxxxxx'
        r = self.s.post(url)
        data = r.json()
        print(data)


    def getAllPages(self): # get all pages

        url = self.BaseUrl + '/pages'

        r = self.s.get(url, headers=self.header)
        data = r.json()

        print(data)

        return data

    # def getHTMLContentFromPage(self):


OC = OnenoteCommunicator()
OC.getAccessToken()






