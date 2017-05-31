import requests
import WunderlistCommunicator
from urllib.request import urlopen
import bs4 as bs
from urllib.request import urlopen
from urllib.parse   import quote
import requests



class Babla():
    # http: // pl.bab.la / slownik / angielski - polski / war
    # http: // pl.bab.la / slownik / polski - angielski / wojna
    def __init__(self):
        self.basicURL = 'http://pl.bab.la/slownik/'



    def checkIfLinkExists(self, url):
        answ = True

        try:
            sauce = urlopen(url).read()
            # print(sauce)
            soup = bs.BeautifulSoup(sauce, 'lxml')
            # print(soup)
            content = list()
            for div in soup.find_all('div', class_='quick-result-overview'):
                content.append(div.text)

            # print(content[0])
            try:
                if content[0] == 'Nasz zespół został poinformowany o brakującym tłumaczeniu.':
                    answ = False
            except:
                pass
        except:
            answ = False

        return answ

    def changePolishLetters(self, url):

        urlPL = ""

        for letter in url:
            if letter == 'ą':
                urlPL += 'a'
            elif letter == 'ć':
                urlPL += 'c'
            elif letter == 'ę':
                urlPL += 'e'
            elif letter == 'ł':
                urlPL += 'l'
            elif letter == 'ń':
                urlPL += 'n'
            elif letter == 'ó':
                urlPL += 'o'
            elif letter == 'ś':
                urlPL += 's'
            elif letter == 'ź':
                urlPL += 'z'
            elif letter == 'ż':
                urlPL += 'z'
            else:
                urlPL += letter

        return urlPL

    def getLinkForWord(self ,word):

        link ="not translated"

        urlENG = 'http://pl.bab.la/slownik/' + 'angielski-polski/' + quote(word.lower())
        urlPL = 'http://pl.bab.la/slownik/' + 'polski-angielski/' + quote(word.lower())

        if self.checkIfLinkExists(urlPL) == True:
            link = 'http://pl.bab.la/slownik/' + 'polski-angielski/' + word.lower()

        if self.checkIfLinkExists(urlENG) == True:
            link = 'http://pl.bab.la/slownik/' + 'angielski-polski/' + word.lower()


        # for url in urlS:
        #
        #     # print(url)
        #     if self.checkIfLinkExists(url) == True:
        #         link = url


        # print(urlS)
        return link


#
#
# B = Babla()
# B.getLinkForWord('war')

# word = 'nóż'
# url = 'http://pl.bab.la/slownik/' + 'polski-angielsk/' + quote(word)

# try:
#     sauce = urlopen(url).read()
#     # print(sauce)
#     soup = bs.BeautifulSoup(sauce, 'lxml')
#     # print(soup)
#     content = list()
#     for div in soup.find_all('div', class_='quick-result-overview'):
#         content.append(div.text)
#
#     # print(content[0])
#
#     if content[0] == 'Nasz zespół został poinformowany o brakującym tłumaczeniu.':
#         answ = False
# except:
#     answ = False




