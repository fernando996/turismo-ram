import url
import requests

class Files:
    # def __init__(self, path):
    #     self.path = path
    #     self.url  = self.getUrlForPosition()
        
    def getHtml(self):

        _url = url.Url('ambiente-territorio/dados-meteorologicos/dados-meteorologicos-serie-retrospetiva.html').getUrlForPosition()
        r = requests.get(_url)
        print(r)
            
       
f = Files()
f.getHtml()


# r.status_code
# 200

# r.headers['content-type']
# 'application/json; charset=utf8'

# r.encoding
# 'utf-8'

# r.text
# '{"type":"User"...'

# r.json()