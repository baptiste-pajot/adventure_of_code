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
    for i in range(0, len(tab), width):
        page = i // (width * height)
        res[page].append(tab[i: i + width])
    end = []
    for i in range(height):
        end.append([])
        for j in range(width):
            val = 2
            for page in range(len(tab) // (width * height)):
                if res[page][i][j] != '2':
                    val = res[page][i][j]
                    end[i].append(int(val))
                    break
    for i in range(len(tab) // (width * height)):
        print()
        for j in range(height):
            print(res[i][j])
    print("")
    for i in range(height):
        for j in range(width):
            if end[i][j] == 1:
                print('O', end ='')
            else:
                print(' ', end ='')
        print("")

if __name__ == "__main__":
    main()