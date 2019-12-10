import math

def main():
    f = open("input.txt", "r")
    tab = []
    i = 0
    for line in f:
        tab.append([])
        for char in line:
            if char != '\n':
                num = 0 if char == '.' else 1
                tab[i].append(num)
        i += 1
    pos_x = 28
    pos_y = 29
    tab[pos_y][pos_x] = 2
    
    for i in tab:
        print(i)
    height = len(tab)
    print("height =", height)
    width = len(tab[0])
    print("width =", width)
    dictionnary = {}
    for i in range(height):
        for j in range(width):
            if tab[i][j] == 1:
                delta_x = j - pos_x
                delta_y = i - pos_y
                if delta_y == 0:
                    angle = math.pi / 2 if delta_x > 0 else 3 * math.pi / 2
                elif delta_x == 0:
                    angle =  0 if delta_y < 0 else math.pi
                elif delta_x < 0 and delta_y < 0:              
                    angle = - math.atan(delta_x / delta_y) + 2 * math.pi 
                elif delta_x > 0 and delta_y < 0:              
                    angle = - math.atan(delta_x / delta_y)
                elif delta_x < 0 and delta_y > 0:              
                    angle = - math.atan(delta_x / delta_y) + math.pi
                else:
                    angle = math.pi - math.atan(delta_x / delta_y)
                    #print("i =", i, "j =", j, "delta_x=", delta_x, "delta_y=", delta_y, "angle=", angle)
                #if angle < 0:
                    #angle += 2 * math.pi
                angle = round(angle, 6)
                #print("angle =", angle)
                if angle not in dictionnary:
                    dictionnary[angle] = []
                dist = round(math.sqrt(delta_x ** 2 + delta_y ** 2), 1)
                dictionnary[angle].append([dist, j, i])
    #print(dictionnary)
    for i in sorted (dictionnary.keys()):  
        #print(i, dictionnary[i])
        dictionnary[i] = sorted(dictionnary[i], key = lambda x: x[0])     
        #print(i, dictionnary[i])
    tab = [0]
    nb = 0
    for turn in range(3):
        print("turn number ", turn + 1)
        for i in sorted (dictionnary.keys()):
            if len(dictionnary[i]):
                nb += 1
                #print(nb, i, dictionnary[i]) 
                tab.append(dictionnary[i].pop(0)) 
    #print(tab)
    print("tab[1] =", tab[1])
    print("tab[2] =", tab[2]) 
    print("tab[3] =", tab[3]) 
    print("tab[10] =", tab[10]) 
    print("tab[20] =", tab[20]) 
    print("tab[50] =", tab[50]) 
    print("tab[100] =", tab[100])        
    print("tab[200] =", tab[200])   


if __name__ == "__main__":
    main()