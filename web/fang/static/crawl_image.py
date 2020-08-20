import pymysql
import time
import threading
import requests
conn = pymysql.connect(host='127.0.0.1', user ='root', password ='', database ='fang', charset ='utf8')
cursor = conn.cursor()
sql='select house_image from newhouseinfo_table'
cursor.execute(sql)
results=cursor.fetchall()

def getimage(url):
    try:
        a=requests.get(url)
        with open('image/'+'aa.jpg','wb') as fp:
            fp.write(a.content)
    except:
        print('error')
a=0
for result in results:
    a=a+1
    if a%5==0:
        time.sleep(1)
    thread=threading.Thread(target=getimage,args=('http:'+result[0],))
    thread.start()
    break
