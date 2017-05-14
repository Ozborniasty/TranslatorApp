import requests
import WunderlistCommunicator
from urllib.request import urlopen
import bs4 as bs
import urllib.request

class Babla():
    # http: // pl.bab.la / slownik / angielski - polski / war
    # http: // pl.bab.la / slownik / polski - angielski / wojna
    def __init__(self):
        self.basicURL = 'http://pl.bab.la/slownik/'


    def checkIfLinkExists(self, url):
        answ = True
        sauce = urllib.request.urlopen(url).read()
        # print(sauce)
        soup = bs.BeautifulSoup(sauce,'lxml')
        # print(soup)
        content = list()
        for div in soup.find_all('div', class_='quick-result-overview'):
            content.append(div.text)

        # print(content[0])

        if content[0] == 'Nasz zespół został poinformowany o brakującym tłumaczeniu.':
            answ = False

        return answ


    def getLinkForWord(self ,word):

        urlS = [self.basicURL + 'angielski-polski/' + word , self.basicURL + 'polski-angielski/' + word]
        link =""

        # r = requests.head(urlEng)
        # print(r.status_code)
        # print(r.url)

        for url in urlS:
            if self.checkIfLinkExists(url) == True:
                link = url

        print(link)




B = Babla()
B.getLinkForWord('war')






