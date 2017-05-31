import WunderlistCommunicator as wc
import Babla as bab
import OnenoteCommunicator as oneCom


wunderList = 'Beer'

wundComuni = wc.WunderCommunicator()
listOfWords = wundComuni.getAllTasks(wunderList)

bablaComuni = bab.Babla()

OC = oneCom.OnenoteCommunicator()


numberOfWords = len(listOfWords)

print(numberOfWords)

ID = OC.getPageID('Translations from app')

for l in listOfWords:

    link = bablaComuni.getLinkForWord(l['title'])
    print(link)


    if link != "not translated":
        OC.uptadeSiteContent(ID, l['title'], link)
        wundComuni.makeTaskCompleted(wunderList, l['title'])



