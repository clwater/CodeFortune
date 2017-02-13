import re
import time
import requests

def check(ymd):
    print(ymd)
    filepath = 'date.txt'
    f = open(filepath , "r")
    _date = f.read()
    f.close()

    if _date == ymd:
        return False
    else:
        with open(filepath, 'w') as f:
            f.write(ymd)
        return True


def getToday():
    html = requests.get('http://www.wannianli.net/')
    html.encoding = 'gb2312'
    html = html.text
    #print(html)

    yinli_date = re.findall('<span class="rl_txt_1">.*</span>' , html , re.I)
    print(yinli_date)

def getNewDate():
    ymd = time.strftime("%Y%m%d", time.localtime())
    if check(ymd):
        getToday()
    else:
        getToday()

getNewDate()