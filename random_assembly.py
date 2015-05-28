__author__ = 'kido'
import xlrd
import random
import math
import pyExcelerator as wrex

dict = {}
sync_list = []
rec = []

def get_aver(ra,rb,rc):
    return (ra+rb+rc)/3

def get_delta(ra,rb,rc):
    aver = (ra+rb+rc)/3
    return math.sqrt((ra-aver)*(ra-aver)+(rb-aver)*(rb-aver)+(rb-aver)*(rb-aver))

def get_name(index):
    return sync_list[index]

def trans_info():
    data = xlrd.open_workbook('Base.xlsx')
    sheet = data.sheets()[0]
    nrows = sheet.nrows
    ncols = sheet.ncols
    name = ''
    #global sync_list = []
    #global dict = {}
    for i in range(nrows):
        max = 0
        list = []
        for j in range(ncols):
            val = sheet.cell_value(i,j)
            if j==1:
                name = val
            if j>1:
                list.append(val)
        list.sort(reverse=True)
        #print list
        dict[name] = list[2]
        sync_list.append(name)
    print dict
    print sync_list

def quchong():
    for i in sync_list:
        if i in rec:
            pass
        else :
            print '****Name : ',i,' Rating : ',dict[i]
        break

def wrt():
    w = wrex.Workbook()
    ws = w.add_sheet('Rat')
    cnt = 1
    for i in dict:
        ws.write(cnt,0,i[0])
        ws.write(cnt,0,i[1])
    w.save('GoodRating.xls')


def calc():
    print len(sync_list)
    tot = len(sync_list)
    leave = tot
    cnt = 0
    for i in dict.items():
        print i[0],'\t',i[1]
    while leave !=0:
        first = 0
        i = int(random.randint(0,10000))%tot
        #print 'Random : ',random.randint(0,10000)
        j = int(random.randint(0,10000))%tot
        while i==j :
            j = int(random.randint(0,10000))%tot
            first =first+1
            if first>100:
                quchong()
                break
            #print "J :",j
        k = random.randint(0,10000)%tot
        while i==k or j==k :
            k = int(random.randint(0,10000))%tot
            first =first+1
            if first >100:
                quchong()
                break
        namei = get_name(i)
        namej = get_name(j)
        namek = get_name(k)
        if namei in rec or namej in rec or namek in rec:
            #quchong()
            continue
        ratinga = dict[namei]
        ratingb = dict[namej]
        ratingc = dict[namek]
        cnt +=1
        delta = get_delta(ratinga,ratingb,ratingc)
        if delta <=120 :
            rec.append(namei)
            rec.append(namej)
            rec.append(namek)
            rec.append(get_aver(ratinga,ratingb,ratingc))
            rec.append(delta)
            leave -=3
            print namei,'\t',namej,'\t',namek,'\t',ratinga,'\t',ratingb,'\t',ratingc,'\t',get_aver(ratinga,ratingc,ratingb),'\t',delta,'\t',cnt
        #print cnt
        if cnt > 25:
            for i in sync_list:
                if i in rec:
                    pass
                else :
                    print '****Name : ',i,' Rating : ',dict[i]
            break



trans_info()
calc()
wrt()