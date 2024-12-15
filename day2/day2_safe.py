reports_data = []
reports_safe = 0
verbose=False
#data = "report_data"
data = "sample_data"
with open(data, "r") as f1:
    r_raw = f1.readlines()
    
    for x in r_raw:
        x_c = x.rstrip("\n").split()
        reports_data.append(x_c)

def check_dir(x, y): 
    if int(x) > int(y):
        x_d = "Inc"
    else:
        x_d = "Dec"
    return x_d

def safe_diff(x, y):
    if abs(int(x) - int(y)) > 3 or abs(int(x) - int(y)) == 0:
        return False
    else:
        return True

def is_safe(x):
    report_dir=check_dir(x[0], x[1])
    safe = True
    for i in range(len(x)-1):
        if check_dir(x[i], x[i+1]) != report_dir:
            safe = False
        elif not safe_diff(x[i], x[i+1]):
            safe = False
        if verbose:
            print(f" - {safe} - {report_dir} - {check_dir(x[i], x[i+1])} - {safe_diff(x[i], x[i+1])}")
    return safe 

for x in reports_data:
    # Check direction:

    safe = is_safe(x)
    
    if not safe:
        if verbose:
            print(f"Report Unsafe: {x}")
    else:
        reports_safe = reports_safe + 1
        
print(f"Safe Reports: {reports_safe}")