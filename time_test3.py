import time
from time import localtime
from datetime import  datetime

t1 = time.time()
print(t1)



n1 = datetime.now()
print(n1)
time.sleep(0.3)

t2 = time.time()
print(t2)
n2 = datetime.now()
print(n2)

print(t2-t1)
elapsed = (n2-n1)
print(elapsed.total_seconds() )

tt = localtime(t1)
print(tt)
tt = datetime.strptime('2018-1-12 1:33PM', '%Y-%m-%d %I:%M%p')
print(tt)
