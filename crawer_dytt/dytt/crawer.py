#coding:utf-8
'''
Created on Apr 9, 2018

@author: sherl
'''
import urllib,urllib2,re

url_dir=r'http://www.dytt8.net/'

def get_page(url_d):
    headers = { 'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36' }  
    req = urllib2.Request(url_d,None,headers)#req = urllib2.Request(url, data, headers)
    response = urllib2.urlopen(req)
    tepstr=response.read()
    charset_restr=r'content=.*charset\s*=\s*(.*)"'#
    
    #teststr=r'<META http-equiv=Content-Type content="text/html; charset=gb2312">'
    m=re.search(charset_restr, tepstr)
    
    print m
    
    if m:
        print m.groups()
        return tepstr.decode(m.group(1),'ignore').encode('utf-8')
    return tepstr

def parse_index_page(page):
    restr=r'<a.*href=\'(/html/gndy/.*/\d*/\d*.html)\'>\s*(.*)</a>'#<a href='/html/gndy/dyzz/20180409/56680.html'>2017年动作《空天猎/霸天狼》B</a>
    m=re.findall(restr, page)
    return m

if __name__ == '__main__':
    print url_dir
    page=get_page(url_dir)
    #print page
    urls_desc=parse_index_page(page)
    for i in urls_desc:
        print i[0],i[1].decode('utf-8','ignore')