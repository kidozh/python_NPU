__author__ = 'kido'
# coding=gbk
import urllib2
import cookielib
import re
import thread
import time
import threading
import urllib

def detect_home(website):

    req = urllib2.Request(
        url = website,
        headers = headers
    )
    result = opener.open(req)
    html =result.read()
    #print html.decode('gb2312')

def detect_teacher():
    postData = {
        'callCount':'1',
        'pageSize':'300'
    }
    req = urllib2.Request(
        url = 'http://222.24.192.69/jxpgXsAction.do?oper=listWj&totalrows=11&pageSize=300',
        headers = headers,
    )
    result = opener.open(req)
    html =result.read().decode('gb2312')
    #print html
    sem = re.findall(r'<img name="([0-9]*?)#@([0-9]*?)#@(.*?)#@(.*?)#@(.*?)#@(.*?)" style="cursor: hand;" title=".*?"',html,re.S)
    for i in sem :
        #print i[0],i[1],i[2],i[3],i[4],i[5]
        print "# You are evaluate ",i[2],"Class : ",i[4]
        detect_detail(i[0],i[1],i[5])



def detect_detail(wjbm,bpr,pgnr):# this will send postdata !
    postData = {
        'wjbm':wjbm,
        'bpr':bpr,
        'pgnr':pgnr,
        'oper':'wjShow',
        'page':'1',
        'pageSize':'300',
        'currentPage':'1'
    }
    postData = urllib.urlencode(postData)
    req = urllib2.Request(
        url = 'http://222.24.192.69/jxpgXsAction.do',
        data = postData,
        headers = headers
    )

    result = opener.open(req)
    #print result.read().decode('gb2312')# get linked with table!

    #----------------------------------------#
    postData = {
        'wjbm':wjbm,
        'bpr':bpr,
        'pgnr':pgnr,
        '0000000093':'10_1',
        '0000000094':'10_1',
        '0000000095':'10_1',
        '0000000096':'10_1',
        '0000000097':'10_1',
        '0000000098':'10_1',
        '0000000099':'10_1',
        '0000000100':'10_1',
        '0000000101':'10_1',
        '0000000102':'10_1',
        'zgpj':'very good'
    }
    postData = urllib.urlencode(postData)
    req = urllib2.Request(
        url = 'http://222.24.192.69/jxpgXsAction.do?oper=wjpg',
        data = postData,
        headers = headers
    )
    result = opener.open(req)
    #print result.read().decode('gb2312')# get linked with table!


#----------------------main function-------------------
headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
}
cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
while 1:
    formattime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    try:
        print '-------------------------------'
        print '     Author : kidozh       '
        print '     supported University : Northwestern Polytechnical University      '
        print '     Current time : '+formattime
        print '     language  : Python'
        print '     Shit CAS '
        print '--------------------------------'
    except :
        print 'Cannot show welcome page...'+formattime
    name = raw_input('please input your CAS Address : (eg. http://222.24.192.69/loginAction.do?dlfs=mh&mh_zjh=2013300116&mh_mm=XXXXXX)\n')
    detect_home(name)
    detect_teacher()
