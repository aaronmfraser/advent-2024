import re, itertools

verbose = False

data_type = "real"
#data_type = "sample"
path = "day5/"
order_data = path + data_type + "_order.data"
updates_data = path +  data_type +  "_updates.data"
in_page_order = []
in_page_updates = []

def get_data():
    with open(order_data, "r") as f1:
        for ln in f1:
            in_page_order.append(ln.strip())
        
    with open(updates_data, "r") as f2:
        for ln in f2:
            in_page_updates.append(ln.strip())
    if verbose: 
        print(in_page_order)
        print(in_page_updates)

def prep_rules():
    prep_page_order = []
    with open(order_data, "r") as f1:
        for ln in f1:
            prep_page_order.append(ln.strip())
            
    return set(
        map(
            lambda pair: (int(pair[0]), int(pair[1])),
            re.findall(r"(\d+)\|(\d+)", ",".join(prep_page_order)),
        )
    )


def prep_updates():
    prep_page_updates = []
    with open(updates_data, "r") as f2:
        for ln in f2:
            prep_page_updates.append(ln.strip())
            
    return list(
        map(
            lambda line: list(map(lambda n: int(n), line)),
            itertools.takewhile(
                lambda l: len(l) > 1, [l.split(",") for l in prep_page_updates]
            ),
        )
    )

def prep_data():
    return prep_rules(), prep_updates()


def is_invalid_order(combination, rules):
    to_check = tuple(reversed(combination))
    #if verbose:
    #    print(f" - combo: {to_check}")
    # If the reverse of a combo matches a rule, the unreversed combo is invalid.
    if to_check in rules:
        return True
    else:
        return False

def flippem(combo, update):
    new = update.copy()
    new[update.index(combo[0])] = combo[1]
    new[update.index(combo[1])] = combo[0]
    #if verbose:
    #    print(f"  a2: flipped: {new}")
    return new

def flip_a_pair(update, rules):
    for combination in itertools.combinations(update, 2):
        if is_invalid_order(combination, rules):
            #if verbose:
            #    print(f"  a2: - invalid: {update}")
            return flippem(combination, update)

def is_aligned_to_rules(update, rules):
    for combination in itertools.combinations(update, 2):
        #if verbose:
        #    print(f" - {combination} - {tuple(reversed(combination))}")
        if is_invalid_order(combination, rules):
            if verbose:
                print(f"  - invalid: {update}")
            return False
    if verbose:
        print(f"  - valid: {update}")
    return True

def align_to_rules(update, rules):
    # Check if update is correct, return if it is
    # if its not correct, we need to flip values. Two at a time. 

    return (
        update
        if is_aligned_to_rules(update, rules)
        else align_to_rules(flip_a_pair(update, rules), rules)
    )

def find_mids(updates):
    all = []
    for update in updates:
        if update is not None:
            mid = len(update) // 2
            
            resp = update[mid]
            if verbose:
                print(f" - mid {mid} - {resp}")
            all.append(resp)
        else:
            continue
    return all

def answer_1(rules, updates):
    middles = []
    for update in updates:
        if is_aligned_to_rules(update, rules):
            middles.append(update)
    
    return sum(find_mids(middles))


def answer_2(rules, updates):
    middles = []
    for update in updates:
        if not is_aligned_to_rules(update, rules):
            if verbose:
                print(f"  a2: misaligned {update}")
            fixed = align_to_rules(update, rules)
            if verbose:
                print(f"Fixed: {fixed}")
            middles.append(fixed)
    
    resp = sum(find_mids(middles))
    if verbose:
        print(resp)
    return resp

(rules, updates) = prep_data()
if verbose:
    print(f"Rules: {rules}")
    print(f"Updates: {updates}")
print("1:", answer_1(rules, updates))
print("2:", answer_2(rules, updates))


