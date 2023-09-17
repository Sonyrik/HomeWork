def second_to_str(sec):
    sec_mem=sec
    if sec>=86400:
        den=sec/86400
        sec=sec%(24*3600)
        hour=sec//3600
        sec%=3600
        min=sec//60
        sec%=60
    else:
        sec=sec%(24*3600)
        hour=sec//3600
        sec%=3600
        min=sec//60
        sec%=60
    if sec_mem<60:
        return  "%02ds" % (sec)
    if 60<=sec_mem<3600:
        return  "%02dm%02ds" % (min, sec)
    if 3600<=sec_mem<86400:
        return  "%02dh%02dm%02ds" % (hour, min, sec)
    if sec_mem>=86400:
        return  "%02dd%02dh%02dm%02ds" % (den, hour, min, sec)
x = int(input("Введите колличество секунд:"))
print(second_to_str(x))