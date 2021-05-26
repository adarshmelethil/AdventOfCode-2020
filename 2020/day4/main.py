#!/usr/bin/env python3

from functools import reduce

# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

import re
color = re.compile(r"^#[0-9a-f]{6}$")
pid = re.compile(r"^[0-9]{9}$")
validator = {
    "byr": lambda x: 1920 <= int(x) <= 2002,
    "iyr": lambda x: 2010 <= int(x) <= 2020,
    "eyr": lambda x: 2020 <= int(x) <= 2030,
    "hgt": lambda x: (x[-2:] == "cm" and (150 <= int(x[:-2]) <= 193)) \
    or (x[-2:] == "in" and (59 <= int(x[:-2]) <= 76)),
    "hcl": lambda x: color.match(x) is not None,
    "ecl": lambda x: x.strip() in [
        "amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda x: pid.match(x) is not None,
    "cid": lambda x: False,
}
counter = 0
passport_fields = 0
with open("input", "r") as fp:
    for line in fp:
        line = line.strip()
        if line == "":
            if passport_fields == 7:
                counter += 1
            passport_fields = 0
            continue

        passport_fields += reduce(
            lambda x, _: x+1, map(
                    lambda l: l.split(":")[0], filter(
                        lambda l: validator[l.split(":")[0]](l.split(":")[1]),
                        line.split(" "))),
            0)
if passport_fields == 7:
    counter += 1
print(counter)
