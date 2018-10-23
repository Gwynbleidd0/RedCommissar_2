from datetime import datetime, timedelta

def get_name_file():
    ll = (datetime.now()+timedelta(days=1)).strftime("%d%m%y")
#    print(list(ll))
    day = int(ll[0]+ll[1])
    mount = int(ll[2]+ll[3])
    if mount == 1:
        mount = 'января'
    elif mount == 2:
        mount = 'февраля'
    elif mount == 3:
        mount = 'марта'
    elif mount == 4:
        mount = 'апреля'
    elif mount == 5:
        mount = 'мая'
    elif mount == 6:
        mount = 'июня'
    elif mount == 7:
        mount = 'июля'
    elif mount == 8:
        mount = 'августа'
    elif mount == 9:
        mount = 'сентября'
    elif mount == 10:
        mount = 'октября'
    elif mount == 11:
        mount = 'ноября'
    elif mount == 12:
        mount = 'декабря'
    else:
        mount='Ошибка'
    day_mounth_1=str(day)+' '+mount
    day_mounth_2=str(day)+'. '+mount
    dowd_link = ['_1 смена.xls','_ 1 смена изменения.xls','. 1 смена.xls','. 1 смена изменения.xls','_1 смена(изменения).xls',' 1 смена(изменения).xls','. 1 смена(изменения).xls','.1 смена (изменения).xls','. 1 смена (изменения).xls','_1 смена (изменения).xls','_ 1 смена (изменения).xls',]
    i=0
    dowd_link_ready=[]
    while i<len(dowd_link):
        dowd_link_ready.append(day_mounth_1+dowd_link[i])
        dowd_link_ready.append(day_mounth_2+dowd_link[i])
        i=i+1
#    print(dowd_link_ready)
    dowd_link_ready.append(day_mounth_1+'.xls')
    dowd_link_ready.append(day_mounth_2+'.xls')
    return(dowd_link_ready)
def get_date():
    ll = (datetime.now()+timedelta(days=1)).strftime("%d%m%y")
    day = int(ll[0]+ll[1])
    mount = int(ll[2]+ll[3])
    if mount == 1:
        mount = 'января'
    elif mount == 2:
        mount = 'февраля'
    elif mount == 3:
        mount = 'марта'
    elif mount == 4:
        mount = 'апреля'
    elif mount == 5:
        mount = 'мая'
    elif mount == 6:
        mount = 'июня'
    elif mount == 7:
        mount = 'июля'
    elif mount == 8:
        mount = 'августа'
    elif mount == 9:
        mount = 'сентября'
    elif mount == 10:
        mount = 'октября'
    elif mount == 11:
        mount = 'ноября'
    elif mount == 12:
        mount = 'декабря'
    else:
        mount='Ошибка'
    day_mounth_1=str(day)+' '+mount
    date=day_mounth_1
    return(date)
def get_real_date():
    ll = (datetime.now()+timedelta(days=1)).strftime("%d%m%y")
    day = int(ll[0]+ll[1])
    return(day)
def get_month():
    ll = (datetime.now()+timedelta(days=1)).strftime("%d%m%y")
    mount = int(ll[2]+ll[3])
    if mount == 1:
        mount = 'января'
    elif mount == 2:
        mount = 'февраля'
    elif mount == 3:
        mount = 'марта'
    elif mount == 4:
        mount = 'апреля'
    elif mount == 5:
        mount = 'мая'
    elif mount == 6:
        mount = 'июня'
    elif mount == 7:
        mount = 'июля'
    elif mount == 8:
        mount = 'августа'
    elif mount == 9:
        mount = 'сентября'
    elif mount == 10:
        mount = 'октября'
    elif mount == 11:
        mount = 'ноября'
    elif mount == 12:
        mount = 'декабря'
    else:
        mount='Ошибка'
    return(mount)
