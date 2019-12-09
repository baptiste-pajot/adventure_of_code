def main():
    f = open("input.txt", "r")
    for x in f:
        tab = x
    print(len(tab))
    width = 25
    height = 6
    res = []
    for i in range(len(tab) // (width * height)):
        res.append([])
    for i in range(len(tab)):
        page = i // (width * height)
        print(page)
        res[page].append(tab[i])
    for i in range(len(tab) // (width * height)):
        print(res[i])

if __name__ == "__main__":
    main()