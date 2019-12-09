import math, sys
from itertools import permutations

def main():
    f = open("input_test.txt", "r")
    for x in f:
        tab = list(map(int, x.split(",")))
    perm = permutations([9, 8, 7, 6, 5])
    max = 0
    tabcopy = []
    for x in range(5):
        tabcopy.append(tab.copy())
    for order in list(perm):
        print("order", order)
        previous = 0
        i = 0
        while 1:
            #print("tabcopy[0] =", tabcopy[0])
            for x in range(5):
                param = order[x] if i == 0 else -1
                print("tabcopy =", tabcopy[x], "previous =", previous, "param =", param, "i =", i)
                previous = day_05(tabcopy[x], previous, param)
                print('result =', previous)
            #x  = previous if previous > max else max
            i += 1
    print("max =", max)


def day_05(tab, previous, param):
    i = 0
    output = 0    
    while 1:
        if tab[i] == 99:
            return(output)
        elif tab[i] % 10 == 1:
            param1 =  tab[i + 1] if (tab[i] % 1000 // 100) else tab[tab[i + 1]]
            param2 =  tab[i + 2] if (tab[i] % 10000 // 1000) else tab[tab[i + 2]]
            if tab[i] // 10000:
                tab[i + 3] = param1 + param2
            else:
                tab[tab[i + 3]] = param1 + param2
            i += 4
        elif tab[i] % 10 == 2:
            param1 =  tab[i + 1] if (tab[i] % 1000 // 100) else tab[tab[i + 1]]
            param2 =  tab[i + 2] if (tab[i] % 10000 // 1000) else tab[tab[i + 2]]
            if tab[i] // 10000:
                tab[i + 3] = param1 * param2
            else :
                tab[tab[i + 3]] = param1 * param2
            i += 4
        elif tab[i] % 10 == 3:
            value = param if param >= 0 else previous
            param = -1
            if tab[i] % 1000 // 100:
                tab[i + 1] = value 
            else:
                tab[tab[i + 1]] = value
            i += 2
        elif tab[i] % 10 == 4:
            param1 =  tab[i + 1] if (tab[i] % 1000 // 100) else tab[tab[i + 1]]
            output = param1
            print("output =", output)
            i += 2
        elif tab[i] % 10 == 5:
            param1 =  tab[i + 1] if (tab[i] % 1000 // 100) else tab[tab[i + 1]]
            param2 =  tab[i + 2] if (tab[i] % 10000 // 1000) else tab[tab[i + 2]]
            if param1:
                i = param2
            else:
                i += 3
        elif tab[i] % 10 == 6:
            param1 =  tab[i + 1] if (tab[i] % 1000 // 100) else tab[tab[i + 1]]
            param2 =  tab[i + 2] if (tab[i] % 10000 // 1000) else tab[tab[i + 2]]
            if param1 == 0:
                i = param2
            else:
                i += 3
        elif tab[i] % 10 == 7:
            param1 =  tab[i + 1] if (tab[i] % 1000 // 100) else tab[tab[i + 1]]
            param2 =  tab[i + 2] if (tab[i] % 10000 // 1000) else tab[tab[i + 2]]
            if tab[i] // 10000:
                tab[i + 3] = 1 if param1 < param2 else 0
            else :
                tab[tab[i + 3]] = 1 if param1 < param2 else 0
            i += 4
        elif tab[i] % 10 == 8:
            param1 =  tab[i + 1] if (tab[i] % 1000 // 100) else tab[tab[i + 1]]
            param2 =  tab[i + 2] if (tab[i] % 10000 // 1000) else tab[tab[i + 2]]
            if tab[i] // 10000:
                tab[i + 3] = 1 if param1 == param2 else 0
            else :
                tab[tab[i + 3]] = 1 if param1 == param2 else 0
            i += 4

if __name__ == "__main__":
    main()