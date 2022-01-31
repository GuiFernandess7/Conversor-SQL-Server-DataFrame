from datetime import date
from config import info

def access_path():
    today = date.today()
    path = (info[2] + str(today) + '.xlsx')
    return path

