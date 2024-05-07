# https://estatistica.madeira.gov.pt/download-now/ambiente-territorio/dados-meteorologicos/dados-meteorologicos-serie-retrospetiva.html?start=0
# https://estatistica.madeira.gov.pt/download-now/economica/turismo-pt/turismo-quadros-pt.html?start=0

BASE_URL = 'https://estatistica.madeira.gov.pt/download-now/'

class Url:
    url = ""
    position = 0

    def __init__(self, path):
        self.path = path
        self.url  = self.getUrlForPosition()
        
    def getUrlForPosition(self):
        return "{}{}?start={}".format(BASE_URL, self.path, self.position)

# p = Url('ambiente-territorio/dados-meteorologicos/dados-meteorologicos-serie-retrospetiva.html')
# print(p.getUrlForPosition())
    

# # def isValidDate(date):
# #     if isinstance(date, datetime.date) is False:
# #         raise Exception("The date parameter is not a valid date object!")
# #     return True

# # def getUrlForDownload(date):
# #     isValidDate(date)
# #     return URL + date.strftime("%m_%Y") + ".pdf"

# # def getZipUrlForDownload(date):
# #     isValidDate(date)
# #     return ZIP_URL + date.strftime("%Y") + ".zip"