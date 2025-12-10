import sched, time

def fn():
    print("used!!!")

s = sched.scheduler(time.time, time.sleep)

for i in range(3):
    s.enter(2+i,999,fn)

s.run()
