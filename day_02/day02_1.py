import math

def main():
    f = open("input.txt", "r")
    for x in f:
        tab = list(map(int, x.split(",")))
    print(tab)
    i = 0
    while 1:
        if tab[i] == 99:
            break
        elif tab[i] == 1:
            tab[tab[i + 3]] = tab[tab[i + 1]] + tab[tab[i + 2]]
        elif tab[i] == 2:
            tab[tab[i + 3]] = tab[tab[i + 1]] * tab[tab[i + 2]]
        i += 4
        #print(tab)
    print(tab)


if __name__ == "__main__":
    main()