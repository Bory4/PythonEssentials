import threading,time

def fun1():
    temp = 0
    for i in range(999999999):
        temp += i
    return temp

def fun2():
    print("AAAAA")
    time.sleep(1)

t1 = threading.Thread(target=fun1())
t2 = threading.Thread(target=fun2())

t1.start()
t2.start()

