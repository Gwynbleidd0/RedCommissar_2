from requests_html import HTMLSession
import fille 
def get_url():
    ses=HTMLSession()
    r = ses.get('https://s11028.edu35.ru/2013-06-12-15-17-31/raspisanie')
    i=0
    m=len(r.html.find('.at_icon'))
    hg = []
    while i<m:
        g=1
        f=r.html.find('.at_icon')[i].attrs
        f=f.get('href')
        print(f)
        result=f.find('1 смена')
#        fh=f.find('224/')
#        day_real=fille.get_real_date()
#        day=int(f[fh+4:fh+6])
#        if result!=-1 and day_real==day:
        if result!=-1: 
            hg.append(f)
        else:
            result=f.find('1_смена')
            if result!=-1: 
                hg.append(f)
            else:
                result=f.find('1смена')
                if result!=-1: 
                    hg.append(f)

        i=i+1
    month=fille.get_month()
    try:
        uk=hg[-1]
    except IndexError:
        return(0,0)
    kh=uk.find(month)
    fh=uk.find('224/')
    cast = uk[fh+4:kh+len(month)]
    return(hg[-1],cast)

