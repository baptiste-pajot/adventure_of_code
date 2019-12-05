import math

def main():
    #size = 30000
    size = 5000
    f = open("input_test1.txt", "r")
    tab = []
    for x in f:
        print(x)
        tab.append(x.split(","))
    #print(tab)
    grid = []
    for x in range(size):
        grid.append([])
        for _ in range(size):
            grid[x].append(0)
    pos_x = size // 2 
    pos_y = size // 2
    grid[pos_x][pos_y] = 1
    #for line in tab:
    for i in range(2):
        line = tab[i]
        #print(line)
        pos_x = size // 2 
        pos_y = size // 2
        min = size
        for elem in line:
            #print(elem[0], int(elem[1:]))
            for _ in range(int(elem[1:])):
                if (elem[0] == 'R'):
                    pos_x += 1
                elif (elem[0] == 'L'):
                    pos_x -= 1
                elif (elem[0] == 'U'):
                    pos_y += 1
                elif (elem[0] == 'D'):
                    pos_y -= 1
                if grid[pos_x][pos_y] == 0 and i == 0:
                    grid[pos_x][pos_y] = 2
                elif grid[pos_x][pos_y] == 0 and i == 1:
                    grid[pos_x][pos_y] = 3
                elif grid[pos_x][pos_y] == 2 and i == 1:
                    grid[pos_x][pos_y] = 3
                    #print(pos_x, pos_y)
                    dist = math.fabs(pos_x - size // 2) + math.fabs(pos_y - size // 2)
                    #print("dist = ", dist)
                    if dist < min:
                        min = dist
        if i == 1:
            print("min=", min)
    #print(grid)

if __name__ == "__main__":
    main()