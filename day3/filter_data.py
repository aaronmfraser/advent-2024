import re

path = "./day3/"
data = path + "real.data"
#data = path + "sample.data"
verbose=False
results=0

with open(data, "r") as f1:
    r_raw = f1.readlines()

if verbose:
    print(r_raw)

for i in r_raw:
    list = re.findall("mul\(\d{1,3},\d{1,3}\)",i)
    if verbose:
        print(list)
    for x in list:
        digits = re.findall("\d{1,3},\d{1,3}",x)[0].split(',')
        results = results + (int(digits[0]) * int(digits[1]))

    
print(f"Total: {results}")