#coding:utf-8
'''
Created on Apr 9, 2018

@author: sherl
'''
import urllib,urllib2,re
import sys,random
from time import sleep


reload(sys)  
sys.setdefaultencoding('utf-8')  


url_dir=r'http://www.ygdy8.com/'#r'http://www.dytt8.net/'#
imdb_dir=r'http://www.dytt8.net/html/gndy/jddy/20160320/50523.html'#r'http://www.ygdy8.com/html/gndy/jddy/20160320/50541.html'#

def get_page(url_d, cnt=0):
    if cnt>4: return ""
    
    headers = { 'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36' }  
    #headers['Cookie']=r'UM_distinctid=16295165d77b8-066969d905fab7-3a76015a-1fa400-16295165d787e4; 37cs_user=37cs60026302580; 37cs_show=253; CNZZDATA1260535040=169648380-1522918900-http%253A%252F%252Fwww.dytt8.net%252F%7C1523448119; cscpvcouplet4298_fidx=4; cscpvrich5041_fidx=4'

    req = urllib2.Request(url_d,None,headers)#req = urllib2.Request(url, data, headers)
    try:
        response = urllib2.urlopen(req)
        tepstr=response.read()
    except:
        sleep(2**(cnt+1))
        print url_d,'get except!!!now retrying '
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
    return ""

def parse_index_page(page):
    restr=r'<a.*href=\'/html/gndy/.*/\d*/\d*.html\'>\s*(.*)</a>'#<a href='/html/gndy/dyzz/20180409/56680.html'>2017年动作《空天猎/霸天狼》B</a>
    m=re.findall(restr, page)
    if not m:return None
    for i in m:
        print i.decode('utf-8','ignore')
    m=list(map(lambda x:x.decode('utf-8','ignore'), m))
    return m

def parse_download_page(urld):
    if not urld.startswith(r'http'):
        urld=(url_dir+urld)
    print '\n',urld
    
    page=get_page(urld)
    restr=r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(.*?)">'
    links=re.findall(restr,page)
    
    restr=r'<div class="title_all"><h1><font color=#07519a>(.*?)</font>'
    titleobj=re.search(restr, page)
    
    title=None
    if titleobj:
        title=titleobj.group(1).decode('utf-8','ignore')
    
    if not links:
        return title,links
    
    ret=[]
    for i in links:
        ret.append(i.decode('utf-8','ignore'))
    
    return title,ret

def parse_imdblinks_page(urld):
    #http://www.dytt8.net/html/gndy/jddy/20160320/50523.html
    #<p><a href="http://www.ygdy8.com/html/gndy/dyzz/20160307/50446.html">http://www.ygdy8.com/html/gndy/dyzz/20160307/50446.html</a></p>
    if not urld.startswith(r'http'):
        urld=(url_dir+urld)
    print '\nimdb url:',urld
    
    page=get_page(urld)
    if not page:
        return None
    
    restr=r'<p>.*?<a href="(.*?)">http://www.ygdy8.com'#<p><br />7.9高分惊悚战争《共同警备区》BD中文字幕 <br /><a href="http://www.ygdy8.com/html/gndy/jddy/20160502/50873.html">http://www.ygdy8.com/html/gndy/jddy/20160502/50873.html</a></p>
    links=re.findall(restr,page)
    print links
    restr=r'.*</a> <a href=\'(.*?\.html)\'>下一页</a> </center>'
    nextlink=re.search(restr, page)

    if nextlink:
        nextlink=nextlink.group(1)
        sleep(8)
        nextlink=urld.rsplit('/',1)[0]+'/'+nextlink
        print 'going to next link:',nextlink
        tepp=parse_imdblinks_page(nextlink)
        if tepp:links.extend(tepp)
    
    return links
    pass

def startwith_index(url_dir, txtdir):
    print 'startwith_index:',url_dir
    page=get_page(url_dir)
    if not page:return None
    #print page
    urls_desc=parse_index_page(page)
    if not urls_desc:return None
    
    for ind,i in enumerate(urls_desc):
        #print ind,parse_download_page(i[0]),i[1].decode('utf-8','ignore')
        title,links=parse_download_page(i[0])
        print ind,links,title
        sleep(2)
        if links and len(links)>0:
            with open(txtdir,'a+') as f:
                f.write(links[0]+'\n')
        
def download_linklist(downlinks, txtdir):  
    fail=[]    
    for ind,i in enumerate(downlinks):
        #print ind,parse_download_page(i[0]),i[1].decode('utf-8','ignore')
        title,links=parse_download_page(i)
        print ind,links,title
        sleep(4)
        if links and len(links)>0:
            with open(txtdir,'a+') as f:
                f.write(links[0]+'\n')
        else:
            fail.append(i)
    print 'download linklist get fails:',len(fail)
    return fail

def startwith_imdb(url_dir, txtdir):
    print 'startwith_imdb:',url_dir
    downlinks=parse_imdblinks_page(url_dir)
    
    if not downlinks:return None
    print 'get imdb movies:',len(downlinks),'\n',downlinks
    
    while(len(downlinks)>0):
        print 'iterstart:',len(downlinks)
        downlinks=download_linklist(downlinks,txtdir)
    
    

if __name__ == '__main__':
    startwith_imdb(imdb_dir,'imdb_urls3.txt')
    
    
    
    
    
    
    