__author__ = 'kido'
import urllib2
import cookielib
import re
import json
import time
import threading
import urllib

def detect_VJ(name):
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
    }
    req = urllib2.Request(
        url = 'http://acm.hust.edu.cn/vjudge/problem/status.action#un='+name+'&length=20000'+name,
        headers = headers
    )
    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    result = opener.open(req)
    # html =result.read() #get cookie
    req = urllib2.Request(
        url = 'http://acm.hust.edu.cn/vjudge/problem/fetchStatus.action',
        headers = headers
    )
    result = opener.open(req)
    flag = True
    cnt = 1
    tot = 0
    detect = []
    while flag == 1:
        postData = {
            'draw':	cnt,
            'columns[0][data]':	'0',
            'columns[0][name]': '',
            'columns[0][searchable]':'true',
            'columns[0][orderable]':'false',
            'columns[0][search][value]':'',
            'columns[0][search][regex]':'false',
            'columns[1][data]' :'1',
            'columns[1][name]' :'',
            'columns[1][searchable]' :'true',
            'columns[1][orderable]' :'false',
            'columns[1][search][value]' :'',
            'columns[1][search][regex]' :'false',
            'columns[2][data]' :'2',
            'columns[2][name]' :'',
            'columns[2][searchable]' :'true',
            'columns[2][orderable]' :'false',
            'columns[2][search][value]' :'',
            'columns[2][search][regex]' :'false',
            'columns[3][data]' :'3',
            'columns[3][name]' :'',
            'columns[3][searchable]' :'true',
            'columns[3][orderable]' :'false',
            'columns[3][search][value]' :'',
            'columns[3][search][regex]' :'false',
            'columns[4][data]' :'4',
            'columns[4][name]' :'',
            'columns[4][searchable]' :'true',
            'columns[4][orderable]' :'false',
            'columns[4][search][value]' :'',
            'columns[4][search][regex]' :'false',
            'columns[5][data]' :'5',
            'columns[5][name]' :'',
            'columns[5][searchable]' :'true',
            'columns[5][orderable]' :'false',
            'columns[5][search][value]' :'',
            'columns[5][search][regex]' :'false',
            'columns[6][data]' :'6',
            'columns[6][name]' :'',
            'columns[6][searchable]' :'true',
            'columns[6][orderable]' :'false',
            'columns[6][search][value]' :'',
            'columns[6][search][regex]' :'false',
            'columns[7][data]' :'7',
            'columns[7][name]' :'',
            'columns[7][searchable]' :'true',
            'columns[7][orderable]' :'false',
            'columns[7][search][value]' :'',
            'columns[7][search][regex]' :'false',
            'columns[8][data]' :'8',
            'columns[8][name]' :'',
            'columns[8][searchable]' :'true',
            'columns[8][orderable]' :'false',
            'columns[8][search][value]' :'',
            'columns[8][search][regex]' :'false',
            'columns[9][data]' :'9',
            'columns[9][name]' :'',
            'columns[9][searchable]' :'true',
            'columns[9][orderable]' :'false',
            'columns[9][search][value]' :'',
            'columns[9][search][regex]' :'false',
            'columns[10][data]' :'10',
            'columns[10][name]' :'',
            'columns[10][searchable]' :'true',
            'columns[10][orderable]' :'false',
            'columns[10][search][value]' :'',
            'columns[10][search][regex]' :'false',
            'columns[11][data]' :'11',
            'columns[11][name]' :'',
            'columns[11][searchable]' :'true',
            'columns[11][orderable]' :'false',
            'columns[11][search][value]' :'',
            'columns[11][search][regex]' :'false',
            'order[0][column]' :'0',
            'order[0][dir]' :'desc',
            'start':(cnt-1)*1000+1,
            'length':'1000',
            'search[value]':'',
            'search[regex]':'false',
            'un':name,
            'OJId':'All',
            'probNum':'',
            'res':'1',
            'language':'',
            'orderBy':'run_id',
        }
        postData = urllib.urlencode(postData)
        req = urllib2.Request(
            url = 'http://acm.hust.edu.cn/vjudge/problem/fetchStatus.action',
            headers = headers,
            data = postData
        )
        cnt+=1
        jsonstring = opener.open(req)
        string = jsonstring.read()
        s = json.loads(string)
        for i in s['data'] :
            string = i[11]+i[12]
            try :
                detect.index(string)
            except :
                detect.append(string)
        tot +=len(detect)
        if len(s['data'])==0 :
            flag = False
    return len(detect)

def detect_poj(name):
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
    }
    req = urllib2.Request(
        url = 'http://poj.org/userstatus?user_id='+name,
        headers = headers
    )
    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    result = opener.open(req)
    html =result.read()
    #print html
    sem = re.findall('Solved:</td>.*?<td align=center width=25%>.*?<.*?>(.*?)</a></td>',html,re.S)
    #print re.search('Solved:</td>.*?<td align=center width=25%>.+<.*?>(.*?)</a></td>',html,re.S)
    try :
        return sem[0]
    except:
        return  0
    #for item in sem:
        #print item
        #return  item
    #print result.read()

def detect_hdu(name):
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
    }
    req = urllib2.Request(
        url = 'http://acm.hdu.edu.cn/userstatus.php?user='+name,
        headers = headers
    )
    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    result = opener.open(req)
    html =result.read()
    #print html
    sem = re.findall('<tr><td>Problems Solved</td><td align=center>(.*?)</td></tr>',html,re.S)
    try :
        return sem[0]
    except:
        return  0
    #for item in sem:
        #print item
        #return item

def detect_cf(name):
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
    }
    req = urllib2.Request(
        url = 'http://codeforces.com/profile/'+name,
        headers = headers
    )
    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    result = opener.open(req)
    html =result.read()
    #print html
    sem = re.findall('Contest rating:.*?<span.*?>(.*?)</span>',html,re.S)
    #for item in sem:
        #print item
        #return item
    try :
        return sem[0]
    except:
        return 'Not found'


def detect_zoj(name):
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
    }
    req = urllib2.Request(
        url = 'http://acm.zju.edu.cn/onlinejudge/showUserStatus.do?handle='+name,
        headers = headers
    )
    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    result = opener.open(req)
    html =result.read()
    #print html
    sem = re.findall('<font size="3">AC Ratio:</font> <font color="red" size="4">(.*?)/.*?</font><br/>',html,re.S)
    try:
        return sem[0]
    except:
        return 0
    #for item in sem:
        #print item
        #return item
    #return 0

def detect_fzu(name):
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
    }
    req = urllib2.Request(
        url = 'http://acm.fzu.edu.cn/user.php?uname='+name,
        headers = headers
    )
    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    result = opener.open(req)
    html =result.read()
    #print html
    sem = re.findall('<tr>.*?<td>Total Accepted</td>.*?<td>(.*?)</td>.*?</tr>',html,re.S)
    try:
        return sem[0]
    except:
        return 0

def codeforce(start,end):
    i = start

    while i<end:
        global cnt
        i+=1
        print '|       detecting Codeforce page :',i,'/',lastpage
        req = urllib2.Request(
            url = 'http://codeforces.com/submissions/'+name+'/page/'+str(i)
        )

        #headers = headers
        cookie = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        result = opener.open(req)
        html =result.read()
        sem = re.findall('<span class=.verdict-accepted.>Accepted</span>',html,re.S)
        cnt +=len(sem)

def detect_codeforce(name):
    global cnt
    cnt=0
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
    }
    req = urllib2.Request(
        url = 'http://codeforces.com/submissions/'+name+'/page/1',
        #headers = headers
    )
    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    result = opener.open(req)
    html =result.read()
    #print html
    sem = re.findall('<span class=.verdict-accepted.>Accepted</span>',html,re.S)
    page = re.findall('<span class=.*? pageIndex=.*?><a href="/submissions/.*?/page/.*?">(.*?)</a></span>',html,re.S)
    global lastpage
    try :
        #print 'last page : ',int(page[len(page)-1])
        lastpage = int(page[len(page)-1])
    except :
        lastpage = 1
    i=1
    #print page

    cnt=cnt+len(sem)
    if lastpage > 10:
        t = threading.Thread(target=codeforce,args=(1,lastpage/2))
        p = threading.Thread(target=codeforce,args=(lastpage/2,lastpage))
        threads =[]
        threads.append(t)
        threads.append(p)
        for i in threads:
            i.setDaemon(True)
            i.start()
        t.join()
        p.join()
    return cnt

def detect_acdream(name):
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
    }
    req = urllib2.Request(
        url = 'http://acdream.info/user/'+name,
        headers = headers
    )
    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    try :
        result = opener.open(req)
    except :
        return 0
    html =result.read()
    sem = re.findall('Submissions:.*?<span.*?>(.*?)</span>',html,re.S)
    try:
        return sem[0]
    except:
        return 0

def detect_timus(name):
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
    }
    req = urllib2.Request(
        url = 'http://acm.timus.ru/search.aspx?Str='+name,
        headers = headers
    )
    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    result = opener.open(req)
    html =result.read()
    #print html
    sem = re.findall(r'<TD CLASS="name"><A HREF="(.*?)">'+name+'</A></TD>',html,re.S)
    #print sem[0]
    try:
        req = urllib2.Request(
            url = 'http://acm.timus.ru/'+sem[0],
            headers = headers
        )
    except:
        return 0
    try:
        result = opener.open(req)
    except :
        return 0
    html =result.read()
    sem = re.findall(r'Problems solved</TD><TD CLASS="author_stats_value">([0-9]*?) out of',html,re.S)
    #print html
    #print sem
    try:
        return sem[0]
    except:
        return 0

def detect_dashiye(name):
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
    }
    req = urllib2.Request(
        url = 'http://www.lydsy.com/JudgeOnline/userinfo.php?user='+name,
        headers = headers
    )
    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    result = opener.open(req)
    html =result.read()
    sem = re.findall(r'<tr bgcolor=#D7EBFF><td>Solved<td align=center><a href=.*?>(.*?)</a>',html,re.S)
    try:
        return sem[0]
    except:
        return 0

def detect_codef(name):
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
    }
    postdata = urllib.urlencode({
        'handle':'kidozh',
        'password':'8520967123',
        'action':'enter'
    })
    req = urllib2.Request(
        url = 'http://codeforces.com/enter',
        data=postdata,
        headers = headers
    )
    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    try:
        result = opener.open(req)
    except:
        return 0
    print '> Logined (by means of kidozh)'
    #print result.read()
    post = urllib.urlencode({
        'isAdd':'true'
    })
    requ = urllib2.Request(
        url ='http://codeforces.com/profile/'+name,
        data = post,
        headers = headers
    )
    result = opener.open(requ)
    print '> Successfully attach ! '
    #print result.read()
    #file_object = open('attach.html','w')
    #file_object.writelines(result.read())
    #file_object.close()
    #print result.read()
    requ = urllib2.Request(
        url = 'http://codeforces.com/problemset/standings',
        data = post,
        headers = headers
    )

    result = opener.open(requ)
    #print result.read()
    print '> Connected With dashboard'
    html = result.read()
    #file_object = open('dashboard.html','w')
    #file_object.writelines(html)
    #file_object.close()
    #csrf = re.findall('<span style=.*? class=.*? data-csrf=.(\w*?).>&nbsp;</span>',html,re.S)
    #code = csrf[0]
    requ = urllib2.Request(
        url = 'http://codeforces.com/problemset/standings?&friendsEnabled=on',
        data = post,
        headers = headers
    )

    result = opener.open(requ)
    print '> Crawling Dashboard...'
    #file_object = open('thefile.html','w')
    html = result.read()
    #print html
    #file_object.writelines(html)
    #file_object.close()
    #match = name+'</a>.*?</td>.*?<td >.*?(\d*?).*?</td>'
    match = name+'</a>(.*?)<tr>'
    if name =='kidozh':
        match = r'class=.rated-user user-violet.>kidozh</a>            </td>.*?([0-9]+).*?'
    #p = re.compile(match,re.DOTALL)
    #pi = p.findall(html)
    #print re.search(match,html,re.DOTALL)
    #print match[0]
    mark = re.findall(match,html,re.S)
    #print mark[0]
    try :
        num = re.findall('<td.>\W*?([0-9]+).*?<.td>\W*?',mark[0],re.S)
    except :
        return 0
    print mark
    nat = re.findall('.*?([0-9]+).*?',mark[0],re.S|re.DOTALL)
    print num,nat
    try :
        return nat[0]
    except :
        return 0

def detect_csu(name):
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
    }
    req = urllib2.Request(
        url = 'http://acm.csu.edu.cn/OnlineJudge/userinfo.php?user='+name,
        headers = headers
    )
    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    try :
        result = opener.open(req)
    except :
        return 0
    html =result.read()
    sem = re.findall(r'<td>Solved<td .*?><a href=.*?>(.*?)</a>',html,re.S)
    #print html
    #print "Csu : ",sem[0]

    try:
        return sem[0]
    except:
        return 0

def detect_uestc(name):
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
    }
    req = urllib2.Request(
        url = 'http://acm.uestc.edu.cn/#/user/center/'+name+'/problems',
        headers = headers
    )
    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    try :
        result = opener.open(req)
    except :
        return 0
    html =result.read()
    sem = re.findall(r'<span class="font-success ng-binding" ng-bind="targetUser.solved">(.*?)</span>',html,re.S)
    print html
    print "UESTC : ",sem[0]

    try:
        return sem[0]
    except:
        return 0

def detect_hust(name):
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
    }
    req = urllib2.Request(
        url = 'http://acm.hust.edu.cn/u/'+name,
        headers = headers
    )
    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    try :
        result = opener.open(req)
    except :
        return 0
    html =result.read()
    sem = re.findall(r'<li class="accept" value=".*?" id=".*?">([0-9]*?)</li>',html,re.S)
    #print html
    #print "HUSTOJ : ",sem[0]

    try:
        return sem[0]
    except:
        return 0

def detect_spoj(name):
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
    }
    req = urllib2.Request(
        url = 'http://www.spoj.com/users/'+name,
        headers = headers
    )
    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    try :
        result = opener.open(req)
    except :
        return 0
    html =result.read()
    sem = re.findall(r'<dd>([0-9].*?)</dd>',html,re.S)
    #print html
    #print "HUSTOJ : ",sem[0]

    try:
        return sem[0]
    except:
        return 0

def detect_sgu(name):
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
    }
    postData = {
        'find_id':name
    }
    postData = urllib.urlencode(postData)
    req = urllib2.Request(
        url = 'http://acm.sgu.ru/find.php',
        headers = headers,
        data =postData
    )

    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    try :
        result = opener.open(req)
    except :
        return 0
    html =result.read()
    sem = re.findall(r'</h5><ul><li>[0-9]*?.*?<a href=.teaminfo.php.id=([0-9]*?).>.*?</a></ul>',html,re.S)
    #print html
    try:
        temp = sem[0]
    except:
        return 0
    try:
        req = urllib2.Request(
            url = 'http://acm.sgu.ru/teaminfo.php?id='+str(temp),
            headers = headers
        )
        result = opener.open(req)
        html=result.read()
        #print html
        sem = re.findall(r'Accepted: ([0-9]*?)<br>',html,re.S)
        #print sem[0]
    except :
        sem = [0]
    try:
        return sem[0]
    except:
        return 0

#-------------main part---------------------


quit = 1
while 1:
    formattime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    try:
        print '-------------------------------'
        print '     Author : kidozh       '
        print '     supported OJ : POJ,HDU,ZOJ,Codeforce,FZU,ACdream,BZOJ,URAL,CSU,HUST,SPOJ,SGU，Virtual Judge      '
        print '     Current time : '+formattime
        print '     language  : Python'
        print '     if your accounts don\'t keep consistency you can type many times'
        print '--------------------------------'
    except :
        print 'Cannot show welcome page...'+formattime
    name = raw_input('please input your account(For example : vjudge1): ')

    poj = detect_poj(name)
    print 'POJ : ',poj
    hdu = detect_hdu(name)
    print 'HDU : ',hdu
    zoj = detect_zoj(name)
    print 'ZOJ : ',zoj
    fzu = detect_fzu(name)
    print 'FZU : ',fzu
    acdream = detect_acdream(name)
    print 'ACdream : ',acdream
    try :
        acdream = int(acdream)
    except:
        acdream =0
    dashiye = detect_dashiye(name)
    print 'BZOJ : ',dashiye
    cf = detect_codef(name)
    print 'CodeForce : ',cf
    timus = detect_timus(name)
    print 'Timus( URAL ) : ',timus
    csu =detect_csu(name)
    print 'Csu : ',csu
    hust = detect_hust(name)
    print 'HUST :',hust
    spoj = detect_spoj(name)
    print 'SPOJ : ',spoj
    sgu = detect_sgu(name)
    print 'SGU : ',sgu
    print 'Total : ',int(poj)+int(hdu)+int(zoj)+int(fzu)+int(acdream)+int(dashiye)+int(timus)+int(hust)+int(spoj)+int(sgu)
    print '+----------------------Code Force Score----------------------'
    print '+         Codeforce Score    : ',detect_cf(name)
    print '+------------------------------------------------------------'
    print 'Virtual judge : ',detect_VJ(name)




