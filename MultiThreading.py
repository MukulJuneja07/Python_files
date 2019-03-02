import threading

x=0
y=0

def func1():
    global x
    for i in range(100000000):
        x=x+1

def func2():
    global y
    for i in range(100000000):
        y=y+1

Th1 = threading.Thread(target=func1)
Th2 = threading.Thread(target=func2)
Th1.start()
Th2.start()
Th1.join()
Th2.join()
print(x,y)