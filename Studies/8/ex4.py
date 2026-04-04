#!/usr/bin/python

try:
    with open("logs.log", 'r') as file:
        f = file.read().strip().split("\n")
except Exception as e:
    print(e)
    exit()

counter = {}
for i in f:
    if "FAIL" in i:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1

try:
    file = open("podejrzane.txt", 'w')
    for k, i in counter.items():
        if i > 2:
            file.write(f"{''.join(k[:len(k) - 5])} - {i}\n")
except Exception as e:
    print(e)
    exit()