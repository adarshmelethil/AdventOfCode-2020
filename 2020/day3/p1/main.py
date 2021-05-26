#!/usr/bin/env python3

# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.
counters = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2],
]
for c in counters:
    c.append(-c[0])
    c.append(0)

with open("input.txt", "r+") as fp:
    for i, line in enumerate(fp):
        line = line.strip()
        for c in counters:
            if i % c[1] == 0:
                c[2] += c[0]
                c[2] %= len(line)

                if line[c[2]] == "#":
                    c[3] += 1
p = 1
for c in counters:
    print(c)
    p *= c[3]
print(p)
