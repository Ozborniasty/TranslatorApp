import requests
import json

class WunderlistCommunicator():

    def __init__(self):
        self.s = requests.Session()
        self.url = dict()

        self.url['list']  = 'https://a.wunderlist.com/api/v1/lists'
        self.url['tasks'] = 'https://a.wunderlist.com/api/v1/tasks'
        self.url['root']  = 'https://a.wunderlist.com/api/v1/root'

        self.headers = {
              'X-Access-Token': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
             ,'X-Client-ID': 'xxxxxxxxxxxxxxxxxxxxxxxxx'
             ,'Content-type': 'application/json'}

    def getRoot(self):
        r = self.s.get(self.url['root'], headers=self.headers)
        rootData = r.json()
        return rootData

    def getRevision(self):
        rootData = self.getRoot()
        return rootData['revision']

    def getAllListsts(self):
        r = self.s.get(self.url['list'], headers=self.headers)
        data = r.json()
        return data

    def getListID(self, titleOfList):
        lists = self.getAllListsts()
        for l in lists:
            if l['title'] == titleOfList:
                return l['id']

    def getAllTasks(self, titleOfList):
        list_id = self.getListID(titleOfList)
        params= {'list_id':list_id}
        tasks = self.s.get(self.url['tasks'], params=params ,headers=self.headers)
        tasks = tasks.json()
        return tasks

    def getTaskID(self, titleOfList, titleOfTask):
        tasks = self.getAllTasks(titleOfList)
        for t in tasks:
            if t['title'] == titleOfTask:
                return t['id']

    def makeTaskCompleted(self, titleOfList, titleOfTask):
        task_id = self.getTaskID(titleOfList, titleOfTask)
        url = self.url['tasks'] + '/' + str(task_id)

        r = self.s.get(url, headers=self.headers)
        task_data = r.json()

        data = {
               'completed': True
                ,'revision':int(task_data['revision'])
        }

        r = self.s.patch(url,data=json.dumps(data), headers=self.headers)



