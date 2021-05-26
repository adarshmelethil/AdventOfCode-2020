#!/usr/bin/env python3

with open("input.txt", "r+") as fp:
    data = list(map(int, fp.read().split()))

def ans(data, value, first_val=None):
    for i, n in enumerate(data):
        new_val = value - n
        if new_val < 0:
            continue
        if first_val:
            if new_val in data[i:]:
                return new_val * n * first_val
        else:
            a = ans(data[i+1:], new_val, first_val=n)
            if a:
                return a
    return None


print(ans(data, 2020))
