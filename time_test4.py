import time
from time import localtime
from datetime import  datetime


str_time = '2018-01-01'
ctime = datetime.strptime(str_time, '%Y-%m-%d')
ctime = datetime(2018, 1, 1)
print(ctime, type(ctime))


str_time = '2018-01-01 23:45:50'
ctime = datetime.strptime(str_time, '%Y-%m-%d %H:%M:%S')
ctime = datetime(2018, 1, 1, 23, 45, 50)
print(ctime, type(ctime))

