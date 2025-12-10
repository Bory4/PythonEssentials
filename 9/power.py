import threading, time, sys, multiprocessing

sys.set_int_max_str_digits(0)

def powerof(x):
    temp = 1
    for i in range(1,x+1):
        temp *= i

print("---Start of normal---")
start = time.time()
powerof(2000)
end = time.time()
normal = end - start
print("---End of normal---")


print("---Start of multithreaded---")
start = time.time()
threads = []

for i in range(10000):
    t = threading.Thread(target=powerof(2000), daemon=True).run()
    threads.append(t)

# for t in threads:
#     t.start()

# for t in threads:
#     t.join()
end = time.time()
multithreadingTime = end - start
print("---End of multithreaded---")


print("---Start of multiprocessing---")
start = time.time()
for i in range(2):
    p = multiprocessing.Process(target=powerof(2000))
    p.start()
    p.join()
end = time.time()
print("---End of multiprocessing---")


print(f"Normal: {normal}")
print(f"Multi-threaded: {multithreadingTime}, time per thread: {(multithreadingTime)/10000}")
print(f"Multi-processing: {end-start}, time per thread: {(end-start)/2}")
