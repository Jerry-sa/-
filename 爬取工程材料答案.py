from bs4 import BeautifulSoup
import requests
import re
import random
import webbrowser
import tkinter as tk
import multiprocessing as mp
import time
def start():
    window=tk.Tk()
    window.title('Found answer!')
    window.geometry('500x300')
    l=tk.Label(window,text='input question:',bg='red',font=('Arial',12),width=15,height=1)
    l.place(x=0,y=0)
    global e
    e=tk.Entry(window,width=50)
    e.place(x=140,y=0)
    b=tk.Button(window,text='search',width=15,bg='green',height=2,command=lambda : main())
    b.place(x=75,y=40)
    tk.mainloop()


def getHTMLText(url,param=None):
    try:
        kv={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'Cookie': 'BAIDUID=F9F4A748776732D5A61DBB25B73D546C:FG=1; BIDUPSID=F9F4A748776732D5A61DBB25B73D546C; PSTM=1590203119; BD_UPN=12314753; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; BD_CK_SAM=1; PSINO=6; H_PS_PSSID=31656_1468_31326_21108_31111_31595_31463_30823_22157; H_PS_645EC=377c8JwVg6tsBlrFH1D%2Bqq4d6yRsUN8v1txmRITIoUU4kVuuSGt%2BDawGyQc'}
        r = requests.get(url,params=param,headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "失败"

def main():
    global e
    question=e.get()
    param={'wd':question}
    url="https://www.baidu.com/s"
    html=getHTMLText(url,param=param)
    soup=BeautifulSoup(html,features='lxml')
    urls=[]
    urls_get=soup.find_all('a',{'target':'_blank','href':re.compile("http://www.baidu.com/link.*?")})
    for i in urls_get:
        urls.append(i['href'])
    urls=(list(set(urls)))
    for ur in urls:
        html1=getHTMLText(ur)
        if re.compile('查看.*?答案') in html1:
            pass
        else:
            webbrowser.open(ur)
            time.sleep(1)
        


if __name__=='__main__':   
    #start()
    a=re.compile('查看.*?答案')
    print(a.match('查答案'))