import math

def main():
    for noun in range(100):
        for verb in range(100):
            f = open("input.txt", "r")
            for x in f:
                tab = list(map(int, x.split(",")))
            tab[1] = noun
            tab[2] = verb
            #print(tab)
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
            if tab[0] == 19690720:
                print("noun", noun, "verb", verb)
                print(100 * noun + verb)


if __name__ == "__main__":
    main()