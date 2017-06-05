import time
now = time.asctime(time.localtime(time.time()))
print now
print now[2]
x = 0 
for i in str(now):
    x = x+1
    print i, x
    
    
