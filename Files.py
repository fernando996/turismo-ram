import url
import requests
from bs4 import BeautifulSoup
from pathlib import Path
import json

class Files:
    urlInstance = None
    model       = None
    data        = None

    def __init__(self, model: dict):
        self.model   = model
        self.urlInst = url.Url(model['url'])
        f            = open('./data/data.json')
        self.data    = json.load(f)

        if self.model['model'] not in self.data:
            self.data[self.model['model']] = []
        
    def getHtmlDownloadFiles(self) -> list:
        r    = requests.get(self.urlInst.getUrlForPosition())
        soup = BeautifulSoup(r.content, "html.parser")

        return soup.find_all("a", {"title":"Descarregar", "class":"jd_download_url"})
            
    def getFiles(self, dir: str, url: str) :
        r        = requests.get(url, stream=True)
        filename = "{}/{}".format(dir, r.headers.get("Content-Disposition").split("filename=")[1].replace('"', ""))

        with open(filename, 'wb') as f:
            f.write(r.content)
        return filename
               
    def downloadFilesList(self, model: dict, elements: list):
        dir = "./dataFiles/{}".format(model['model'])

        Path(dir).mkdir(parents=True, exist_ok=True)

        for i in elements:
            txt = i.text.strip()
            fn  = "{}{}".format(self.urlInst.getBaseUrl(), i['href'])
            obj = {"url": fn, "name":txt}
            if len(list(filter(lambda file: file['url'] == fn, self.data[self.model['model']]))) == 0:
                filename = self.getFiles(dir, fn)
                obj['filename'] = filename
                self.data[self.model['model']].append(obj)

    def writeData(self):
        with open('./data/data.json', 'w') as f:
            json.dump(self.data, f)



f = open('./dataModel/dataModels.json')
data = json.load(f)
files = Files(data)

files.downloadFilesList(data, files.getHtmlDownloadFiles())
files.writeData()

# r.status_code
# 200

# r.headers['content-type']
# 'application/json; charset=utf8'

# r.encoding
# 'utf-8'

# r.text
# '{"type":"User"...'

# r.json()