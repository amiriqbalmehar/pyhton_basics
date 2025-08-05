# check time of code it not good way to check time of code
import time
start= time.time()
'''for i in range(1,101):
    print(i)'''

i=1
while i<=100:
    print(i)
    i+=1

print(time.time()-start)

