debug = True
verbose = False

#data_type = "real"
data_type = "sample"
path = "day6/"
room_data = path + data_type + ".data"

def getData():
    room_map = []
    with open(room_data, "r") as f1:
        for ln in f1:
            room_map.append(list(ln.strip()))
    if debug:
        print(f" - debug: {room_map}")
    return room_map

getData()