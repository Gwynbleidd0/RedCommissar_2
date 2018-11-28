from requests_html import HTMLSession
import fille 
def get_url():
    ses=HTMLSession()
    r = ses.get('https://s11028.edu35.ru/2013-06-12-15-17-31/raspisanie')
    i=0
    m=len(r.html.find('.at_icon'))
    hg = []
    while i<m:
        f=r.html.find('.at_icon')[i].attrs
        f=f.get('href')
#        print(f)
        result=f.find('1 смена')
        if result!=-1:
            hg.append(f)
        result=f.find('1_смена')
        if result!=-1:
            hg.append(f)
        result=f.find('1смена')
        if result!=-1:
            hg.append(f)
        i=i+1
    month=fille.get_month()
    count=0
    for m in hg:
        print(int(m[m.find('224/')+4:m.find('224/')+6]))
        if count<int(m[m.find('224/')+4:m.find('224/')+6]):
            count = int(m[m.find('224/')+4:m.find('224/')+6])
            last=m
    print(last)
    try:
        uk=hg[-1]
    except IndexError:
        return(0,0)
    kh=uk.find(month)
    fh=uk.find('224/')
    cast = uk[fh+4:kh+len(month)]
    return(hg[-1],cast)
print(get_url())
