#!/usr/bin/python
try:
    with open("wejscie.txt", 'r') as file:
        f = file.readlines()
except Exception as e:
    print(e)
    exit()

try:
    file = open("wyjscie.txt", 'w')
    f = f[::-1]
    for i in range(len(f)):
        f[i] = f[i][::-1]
    for i in f:
        file.write(i)
except Exception as e:
    print(e)
    exit()
