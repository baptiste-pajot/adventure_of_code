import math

def main():
    f = open("input_test1.txt", "r")
    tab = []
    i = 0
    for line in f:
        tab.append([])
        for char in line:
            if char != '\n':
                num = 0 if char == '.' else 1
                tab[i].append(num)
        i += 1
    for i in tab:
        print(i)
    

if __name__ == "__main__":
    main()