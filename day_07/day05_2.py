import math

def main():
    f = open("input.txt", "r")
    for x in f:
        tab = list(map(int, x.split(",")))
    i = 0
    while 1:
        if tab[i] == 99:
            break
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
            if tab[i] % 1000 // 100:
                tab[i + 1] = int(input("value ?"))
            else:
                tab[tab[i + 1]] = int(input("value ?"))
            i += 2
        elif tab[i] % 10 == 4:
            param1 =  tab[i + 1] if (tab[i] % 1000 // 100) else tab[tab[i + 1]]
            print("test", param1)
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