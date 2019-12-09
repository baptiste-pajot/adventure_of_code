import math

def main():
    f = open("input.txt", "r")
    for x in f:
        tab = list(map(int, x.split(",")))
    for _ in range(1000):    
        tab.append(0)
    i = 0
    base = 0
    while 1:
        #print("i =", i)
        if tab[i] == 99:
            break
        elif tab[i] % 10 == 1:
            if tab[i] % 1000 // 100 == 2:
                param1 =  tab[tab[i + 1] + base]
            elif tab[i] % 1000 // 100:
                param1 =  tab[i + 1]
            else:
                param1 = tab[tab[i + 1]]  
            if tab[i] % 10000 // 1000 == 2:
                param2 =  tab[tab[i + 2] + base]
            elif tab[i] % 10000 // 1000:
                param2 =  tab[i + 2]
            else:
                param2 = tab[tab[i + 2]]
            if tab[i] // 10000 == 2:
                tab[tab[i + 3] + base] = param1 + param2
            elif tab[i] // 10000:
                tab[i + 3] = param1 + param2
            else:
                tab[tab[i + 3]] = param1 + param2
            i += 4
        elif tab[i] % 10 == 2:
            if tab[i] % 1000 // 100 == 2:
                param1 =  tab[tab[i + 1] + base]
            elif tab[i] % 1000 // 100:
                param1 =  tab[i + 1]
            else:
                param1 = tab[tab[i + 1]]  
            if tab[i] % 10000 // 1000 == 2:
                param2 =  tab[tab[i + 2] + base]
            elif tab[i] % 10000 // 1000:
                param2 =  tab[i + 2]
            else:
                param2 = tab[tab[i + 2]]
            if tab[i] // 10000 == 2:
                tab[tab[i + 3] + base] = param1 * param2
            elif tab[i] // 10000:
                tab[i + 3] = param1 * param2
            else:
                tab[tab[i + 3]] = param1 * param2
            i += 4
        elif tab[i] % 10 == 3:
            if tab[i] % 1000 // 100 == 2:
                tab[tab[i + 1] + base] = int(input("value ?"))
            elif tab[i] % 1000 // 100:
                tab[i + 1] = int(input("value ?"))
            else:
                tab[tab[i + 1]] = int(input("value ?"))
            i += 2
        elif tab[i] % 10 == 4:
            if (tab[i] % 1000 // 100) == 2:
                param1 =  tab[tab[i + 1] + base]
            elif (tab[i] % 1000 // 100):
                param1 =  tab[i + 1]
            else:
                param1 = tab[tab[i + 1]]
            print("test", param1)
            i += 2
        elif tab[i] % 10 == 5:
            if tab[i] % 1000 // 100 == 2:
                param1 =  tab[tab[i + 1] + base]
            elif tab[i] % 1000 // 100:
                param1 =  tab[i + 1]
            else:
                param1 = tab[tab[i + 1]]  
            if tab[i] % 10000 // 1000 == 2:
                param2 =  tab[tab[i + 2] + base]
            elif tab[i] % 10000 // 1000:
                param2 =  tab[i + 2]
            else:
                param2 = tab[tab[i + 2]]
            if param1:
                i = param2
            else:
                i += 3
        elif tab[i] % 10 == 6:
            if tab[i] % 1000 // 100 == 2:
                param1 =  tab[tab[i + 1] + base]
            elif tab[i] % 1000 // 100:
                param1 =  tab[i + 1]
            else:
                param1 = tab[tab[i + 1]]  
            if tab[i] % 10000 // 1000 == 2:
                param2 =  tab[tab[i + 2] + base]
            elif tab[i] % 10000 // 1000:
                param2 =  tab[i + 2]
            else:
                param2 = tab[tab[i + 2]]
            if param1 == 0:
                i = param2
            else:
                i += 3
        elif tab[i] % 10 == 7:
            if tab[i] % 1000 // 100 == 2:
                param1 =  tab[tab[i + 1] + base]
            elif tab[i] % 1000 // 100:
                param1 =  tab[i + 1]
            else:
                param1 = tab[tab[i + 1]]  
            if tab[i] % 10000 // 1000 == 2:
                param2 =  tab[tab[i + 2] + base]
            elif tab[i] % 10000 // 1000:
                param2 =  tab[i + 2]
            else:
                param2 = tab[tab[i + 2]]
            if tab[i] // 10000 == 2:
                tab[tab[i + 3] + base] = 1 if param1 < param2 else 0
            elif tab[i] // 10000 :
                tab[i + 3] = 1 if param1 < param2 else 0
            else :
                tab[tab[i + 3]] = 1 if param1 < param2 else 0
            i += 4
        elif tab[i] % 10 == 8:
            if tab[i] % 1000 // 100 == 2:
                param1 =  tab[tab[i + 1] + base]
            elif tab[i] % 1000 // 100:
                param1 =  tab[i + 1]
            else:
                param1 = tab[tab[i + 1]]  
            if tab[i] % 10000 // 1000 == 2:
                param2 =  tab[tab[i + 2] + base]
            elif tab[i] % 10000 // 1000:
                param2 =  tab[i + 2]
            else:
                param2 = tab[tab[i + 2]]
            if tab[i] // 10000 == 2:
                tab[tab[i + 3] + base] = 1 if param1 == param2 else 0
            elif tab[i] // 10000:
                tab[i + 3] = 1 if param1 == param2 else 0
            else :
                tab[tab[i + 3]] = 1 if param1 == param2 else 0
            i += 4
        elif tab[i] % 10 == 9:
            if (tab[i] % 1000 // 100) == 2:
                base += tab[tab[i + 1] + base]
            elif (tab[i] % 1000 // 100):
                base +=  tab[i + 1]
            else:
                base += tab[tab[i + 1]]
            #print("base", base)
            i += 2


if __name__ == "__main__":
    main()