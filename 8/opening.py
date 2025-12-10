#!/usr/bin/python
file = open("one-million.txt",'r').read().strip().split("\n")

pi_string = ""

for line in file:
    pi_string += line.strip()

if "13092005" in pi_string:
    print("tak")
