import requests
import json
import urllib3
from bs4 import BeautifulSoup

class OnenoteCommunicator():

    def __init__(self):
        self.s = requests.Session()

        self.BaseUrl = 'https://www.onenote.com/api/v1.0/me/notes'


    def getAuthorisationWithCode(self):
        header = {'Content-Type': 'application/x-www-form-urlencoded'}

        payload = {'grant_type': 'authorization_code'
                   ,'client_id':''
                   ,'client_secret':''
                   ,'code':''
                   ,'redirect_uri':'https://localhost'
                   }

        r = requests.post("https://login.live.com/oauth20_token.srf", headers = header,data=payload)

        data = r.json()
        print(data)

        F = open('workFile', 'w')

        F.write(data['access_token'])
        F.write('\n')
        F.write(data['refresh_token'])

        F.close()

    def getAccessToken(self):
        F = open('workFile', 'r')

        data = F.readlines()
        token = data[0].strip('\n')
        # print(data[1].strip('\n')

        # print(token)
        return token

    def refreshAccesToken(self):

        F = open('workFile', 'r')
        fileData = F.readlines()
        token = fileData[1].strip('\n')

        F.close()

        header = {'Content-Type': 'application/x-www-form-urlencoded'}

        payload = {'grant_type': 'refresh_token'
            , 'client_id': ''
            , 'client_secret': ''
            , 'redirect_uri': ''
            , 'refresh_token' : token
                   }

        r = requests.post("https://login.live.com/oauth20_token.srf", headers=header, data=payload)



        data = r.json()
        # print("data:", data)
        #
        # print(r.status_code)

        if(r.status_code == 200):
            F = open('workFile', 'w')

            F.write(data['access_token'])
            F.write('\n')
            F.write(data['refresh_token'])

            F.close()

    def getAllPages(self): # get all pages

        self.refreshAccesToken()

        url = self.BaseUrl + '/pages'

        token = self.getAccessToken()

        header = {'Authorization': 'Bearer ' +token}

        r = self.s.get(url, headers=header)
        data = r.json()

        data = data['value']

        return data

    def getAllSections(self): # get all pages

        self.refreshAccesToken()

        url = self.BaseUrl + '/sections'

        token = self.getAccessToken()

        header = {'Authorization': 'Bearer ' + token}

        r = self.s.get(url, headers=header)
        data = r.json()

        data = data['value']

        return data

    def getIdOfSpecificSection(self, name):

        data =  self.getAllSections()

        id = ""

        for d in data:
            if d['name'] == name:
                id = d['id']

        return id

    def getPageID(self, name):

        data = self.getAllPages()

        id = ""

        for d in data:
            if d['title'] == name:
                id = d['id']

        return id

    def getAllPagesInASpecyficSection(self, sectionID):

        self.refreshAccesToken()

        url = self.BaseUrl + '/sections/' + sectionID + '/pages'

        token = self.getAccessToken()

        header = {'Authorization': 'Bearer ' + token}

        r = self.s.get(url, headers=header)
        data = r.json()

        data = data['value']

        return data

    def getContentOfGivenPage(self,pageID):

        # url = 'https://www.onenote.com/api/v1.0/me/notes/' + 'pages/'+ pageID +'/preview'
        url = 'https://www.onenote.com/api/v1.0/me/notes/' + 'pages/' + pageID + '/content?includeIDs'

        token = self.getAccessToken()

        header = {'Authorization': 'Bearer ' + token}

        r = self.s.get(url, headers=header)

        print(r.content)

    def uptadeSiteContent(self,pageID, vocabulary, translationLink):

        transLink = translationLink
        vocab =  vocabulary

        url = 'https://www.onenote.com/api/v1.0/me/notes/' + 'pages/' + pageID + '/content'
        self.refreshAccesToken()
        token = self.getAccessToken()

        header = {'Content-Type': 'application/json'
                   ,'Authorization': 'Bearer ' + token}

        payload = [
                  {
                    'target':'body',
                    'action':'append',
                    'content':'<p data-id="last-child"><a href=\"' + transLink + '\">' + vocab + '</a></p>'
                  # '<p data-id="last-child"><a href="http://pl.bab.la/slownik/angielski-polski/scent">scent</a></p>'
                  }
                  ]
        r = self.s.patch(url,headers=header,data=json.dumps(payload))

        print(r.content)






# OC = OnenoteCommunicator()
# ID = OC.getPageID('Translations from app')
#
# OC.uptadeSiteContent(ID,'scent', 'http://pl.bab.la/slownik/angielski-polski/scent')
#




