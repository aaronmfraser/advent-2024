debug = False
verbose = False

data_type = "real"
#data_type = "sample"
path = "day4/"
xmas_data = path + data_type + ".data"


def getData():
    xmas_map = []
    with open(xmas_data, "r") as f1:
        for ln in f1:
            xmas_map.append(list(ln.strip()))
    if debug:
        print(f" - debug: {xmas_map}")
    return xmas_map

def isValid(x,y,h,w):
    if debug:
        print(f"grid: {x,y} - valid?: {0 <= x < h and 0 <= y < w}")
    return 0 <= x < h and 0 <= y < w

def findWordInDirection(grid, height, width, target, target_index, grid_x, grid_y, adj_x, adj_y ):
    if target_index == len(target):
        return True
#
    if isValid(grid_x, grid_y, height, width) and target[target_index] == grid[grid_x][grid_y]:
        return findWordInDirection(grid, height, width, target, target_index + 1, 
                                grid_x + adj_x, grid_y + adj_y, adj_x, adj_y)


def findWord(grid,target):
    ans = []
    h = len(grid)
    w = len(grid[0])
    
    if debug:
        print(f" - debug: Height: {h}, Width: {w}")
    
    adjacent = [(-1, 1), (-1, 0), (-1, -1), (0, 1), (0, -1), (1, 1), (1, 0), (1, -1)]

    for grid_x in range(h):
        for grid_y in range(w):
            if grid[grid_x][grid_y] == target[0]:
                for adj_x, adj_y in adjacent:
                    if findWordInDirection(grid, h, w, target, 0, grid_x, grid_y, adj_x, adj_y):
                        ans.append([grid_x, grid_y])
    print(len(ans))
    #print(ans)



target = 'XMAS'
grid = getData()

findWord(grid, target)