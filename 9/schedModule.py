import time, sched

s = sched.scheduler(time.time, time.sleep)

def today():
    print(time.ctime())

s.enter(5,999,today)
s.run()