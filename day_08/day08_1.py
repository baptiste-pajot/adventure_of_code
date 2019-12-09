def main():
    f = open("input.txt", "r")
    for x in f:
        tab = x
    print(len(tab))
    width = 25
    height = 6
    res = []
    for i in range(len(tab) // (width * height)):
        res.append([0, 0, 0])
    for i in range(len(tab)):
        page = i // (width * height)
        print(page)
        res[page][0] += 1 if tab[i] == '0' else 0
        res[page][1] += 1 if tab[i] == '1' else 0
        res[page][2] += 1 if tab[i] == '2' else 0
    for i in range(len(tab) // (width * height)):
        print(res[i])

if __name__ == "__main__":
    main()