reports = {}
reports_safe = 0
data = "report_data"
#data = "sample_data"

verbose=False

with open(data, "r") as f1:
    r_raw = f1.readlines()
    
    idx=0
    for x in r_raw:
        x_c = x.rstrip("\n").split()
        reports[idx]={"data": x_c, "safe": True, "mod_used": False, "recheck": False}
        idx=idx+1

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
            print(f"   * safe: {safe} - str_dir: {report_dir} - dir: {check_dir(x[i], x[i+1])} - safe_diff: {safe_diff(x[i], x[i+1])}")
    return safe 

if verbose:
    print(reports)
for x in reports:
    if verbose:
        print(f"Report {x} Starting")
        
    data=reports[x]['data']
    report_dir=check_dir(data[0], data[1])
    # Check direction:
    if verbose:
        print(f" - Direction: {report_dir} - Length: {len(data)}")
    
    safe = is_safe(data)
    
    if safe:
        print(f" Report {x} Passed!!")
        reports_safe = reports_safe + 1
    else:
        if verbose:
            print(f" Report {x} Failed!!")
            print(f" - Running Module")
        safe = False
        
        if verbose:
            print(f"   * {data}")
        for i in range(len(data)):
            a = data[:]
            del a[i]
            if verbose:
                print(f"   * {len(a)} - {a} - {safe}")
            if is_safe(a):
                safe = True
                break
            
        if safe:
            print(f" Report {x} Passed!!")
            reports_safe = reports_safe + 1
        else:
            if verbose:
                print(f"Report {x} Failed again")

print(f"Safe Reports: {reports_safe}")