import time

def sumowanie(do):
    
    temp = (1+do) * (do//2) 
    if do % 2 == 0:
        return temp
    return (temp + (1+do) / 2)

start = time.time()

print(f"Wynik: {sumowanie(100000000000000000)}")

end = time.time()

print(end-start)

