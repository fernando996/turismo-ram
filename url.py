import datetime

URL     = 'http://www.procivmadeira.pt/images/dispositivo-socorro/acidentes-percursos-terrestres/al_'
ZIP_URL = 'http://www.procivmadeira.pt/images/dispositivo-socorro/zip'

def isValidDate(date):
    if isinstance(date, datetime.date) is False:
        raise Exception("The date parameter is not a valid date object!")
    return True

def getUrlForDownload(date):
    isValidDate(date)
    return URL + date.strftime("%m_%Y") + ".pdf"

def getZipUrlForDownload(date):
    isValidDate(date)
    return ZIP_URL + date.strftime("%Y") + ".zip"