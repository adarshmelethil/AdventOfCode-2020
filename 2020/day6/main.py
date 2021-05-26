from functools import reduce

with open("input", "r") as fp:
    group_ans = []
    total = 0
    for line in fp:
        line = line.strip()
        if line == "":
            # t = len(set(group_ans))
            t = len(reduce(lambda x, y: x & y, group_ans))
            # print(t)
            total += t
            group_ans = []
        else:
            group_ans.append(set(line))


print(total+len(reduce(lambda x, y: x & y, group_ans)))
