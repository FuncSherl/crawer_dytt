#coding:utf-8
'''
Created on 2018年5月9日

@author:China
'''

import urllib,urllib2,re
import sys,random
from time import sleep

urls=[r'http://jihadology.net',\
      r'http://www.icdg.info',\
      r'http://www.ytmp3downloads.com/downnload/',\
      r'http://www.upuk.net',
      r'http://uyghurbook.com']

def get_page(url_d, cnt=0):
    if cnt>4: return None
    
    headers = { 'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36' }  
    #headers['Cookie']=r'UM_distinctid=16295165d77b8-066969d905fab7-3a76015a-1fa400-16295165d787e4; 37cs_user=37cs60026302580; 37cs_show=253; CNZZDATA1260535040=169648380-1522918900-http%253A%252F%252Fwww.dytt8.net%252F%7C1523448119; cscpvcouplet4298_fidx=4; cscpvrich5041_fidx=4'

    req = urllib2.Request(url_d,None,headers)#req = urllib2.Request(url, data, headers)
    try:
        response = urllib2.urlopen(req)
        tepstr=response.read()
    except:
        sleep(2**(cnt+1))#2^(cnt+1)
        print (url_d,'get except!!!now retrying ')
        return get_page(url_d,cnt+1)
    
    else:
        charset_restr=r'content=.*charset\s*=\s*(.*)"'#
        
        #teststr=r'<META http-equiv=Content-Type content="text/html; charset=gb2312">'
        m=re.search(charset_restr, tepstr)
        
        #print m
        if m:
            #print m.groups()
            return tepstr.decode(m.group(1),'ignore').encode('utf-8')
        return tepstr
    return None

def get_video(urld):
    f = urllib2.urlopen(urld)
    data = f.read()
    name = 'python.mp4' 

    with open(name, "wb") as code:
        code.write(data)
        
    print ('done:',urld)



if __name__ == '__main__':
    print (get_page(urls[0]))
    pass












