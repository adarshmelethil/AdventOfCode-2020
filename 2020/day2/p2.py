#!/usr/bin/env python3

counter = 0
with open("input.txt", "r+") as fp:
    for l in fp:
        r, v, p = l.split(" ")
        lo, hi = map(int, r.split("-"))
        c = v[:-1]
        p = p.strip()
        if (p[lo-1] == c) != (p[hi-1] == c):
            counter += 1
print(counter)
