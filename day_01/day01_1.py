import math

def main():
    f = open("input.txt", "r")
    result = 0
    for x in f:
        result += math.floor(int(x) / 3) - 2
    print(result)

if __name__ == "__main__":
    main()