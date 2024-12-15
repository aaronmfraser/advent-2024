verbose = True

path = "day5/"
order = path + "sample_order.data"
updates = path +  "sample_updates.data"
in_page_order = []
in_page_updates = []

def get_data():
    with open(order, "r") as f1:
        for ln in f1:
            in_page_order.append(ln.strip())
        
    with open(updates, "r") as f2:
        for ln in f2:
            in_page_updates.append(ln.strip())

    if verbose: 
        print(in_page_order)
        print(in_page_updates)

get_data()

page_orders = {}
for i in in_page_order:
    po = i.split('|')
    if po[0] in page_orders:
        page_orders[po[0]].append(po[1])
    else:
        page_orders[po[0]] = []

if verbose:
    print(page_orders)

update_num = 0
for update in in_page_updates:
    pg_update = update.split(',')
    bad_order = 0
    if verbose:
        print(f"Update#: {update_num}")
    for idx in range(len(pg_update) - 1):
        check_len = len(pg_update) - 1
        if verbose:
            print(f" - idx: {pg_update[idx]} + update: {pg_update}")

        if pg_update[idx] in page_orders.keys():
            if verbose:
                print(f" - order: {page_orders[pg_update[idx]]}")

            id_i = 0
            pg_idx = idx
            while id_i < check_len:
                pg_idx = pg_idx+1
                if pg_update[pg_idx] in page_orders[pg_update[idx]]:
                    good_order = good_order + 1
                id_i = id_i + 1
                if verbose:
                    print(f"   - id_i++: {id_i} - lb_idx: {pg_update[pg_idx]}")
            if verbose:
                print(f" - bad?: {bad_order}")
        check_len = check_len - 1
    update_num = update_num + 1