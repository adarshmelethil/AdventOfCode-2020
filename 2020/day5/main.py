#!/usr/bin/env python3


with open("input", "r") as fp:
    lines = sorted([line.strip() for line in fp])


def code_val(code, suber="F"):
    seat = 0
    vals = [2**i for i in range(len(code)-1, -1, -1)]

    for c, v in zip(code, vals):
        if c != suber:
            seat += v

    return seat

def si(code):
    t = 0
    for i, c in enumerate(code[::-1]):
        if c in ["R", "B"]:
            t += 2**i
    return t

def seat_id(code):
    return code_val(code[:7])*8 + code_val(code[7:], suber="L")

t = "FBFBBFFRLR"
print(lines[0], seat_id(lines[0]))
print(code_val(t[:7]))
print(lines[-1])
print(si(t))
print(seat_id(t))
print(lines[:5])

i = 0
while True:
   i += 1

   p = lines[int(i)-1]
   c = lines[int(i)]

   if p[:-2] == c[:-2] and p[-1] == c[-1]:

       s = c[:-1] + ("L" if p[-1] == "R" else "R")
       print(p, s, c)
       print(seat_id(p))
       print(seat_id(s))
       print(seat_id(c))
       break
   if i >= len(lines)-1:
       break
