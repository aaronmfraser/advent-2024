import re

path = "./day3/"
data = path + "real.data"
#data = path + "real_2.data"
#data = path + "sample_2.data"
verbose=False
results=0

with open(data, "r") as f1:
    r_raw = f1.readlines()


filtered=False
to_filter = re.split("do\(\)","".join(r_raw))
if verbose:
    print(f"Split: {to_filter}")
for i in to_filter:
    lines = re.split("don't\(\)",i)[0]
    if verbose:
        print(f"Lines: {lines}")
    muls = re.findall("mul\(\d{1,3},\d{1,3}\)",lines)
    if verbose:
        print(f"  - muls: {muls}")
    for x in muls:
        digits = re.findall("\d{1,3},\d{1,3}",x)[0].split(',')
        if verbose:
            print(f"  - digits: {digits}")
        results = results + (int(digits[0]) * int(digits[1]))
    
print(f"Total: {results}")
