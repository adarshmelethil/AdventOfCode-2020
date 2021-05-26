#!/usr/bin/env python3

with open("input.txt", "r+") as fp:
    data = list(map(int, fp.read().split()))


for i, n in enumerate(data):
    if (2020 - n) in data[i+1:]:
        print((2020 - n) * n)
        break
