import math

def main():
    f = open("input.txt", "r")
    tab = []
    i = 0
    for line in f:
        tab.append([])
        for char in line:
            if char != '\n':
                num = 0 if char == '.' else 1
                tab[i].append(num)
        i += 1
    #for i in tab:
    #    print(i)
    height = len(tab)
    print("height =", height)
    width = len(tab[0])
    print("width =", width)
    max = [0, 0, 0]
    for i in range(height):
        for j in range(width):
            detected = 0
            if tab[i][j] == 1:
                for k in range(height):
                    for l in range(width):
                        if tab[k][l] == 1 and (k != i or l != j):
                            delta_x = l - j
                            delta_y = k - i
                            #print("delta_x =", delta_x, "delta_y =", delta_y)
                            if delta_x == 0 and delta_y != 0:
                                start = 1 if delta_y > 0 else -1
                                increment = 1 if delta_y > 0 else -1
                                for portion_y in range(start, delta_y, increment):
                                    portion_x = delta_x * portion_y / delta_y
                                    #print(portion_y)
                                    if portion_x % 1 == 0 and tab[i + portion_y][j + int(portion_x)] == 1:
                                        break
                                else:
                                    #print("detected ++", l, k)
                                    detected += 1
                            elif delta_x != 0:
                                start = 1 if delta_x > 0 else -1
                                increment = 1 if delta_x > 0 else -1
                                for portion_x in range(start, delta_x, increment):
                                    portion_y = delta_y * portion_x / delta_x
                                    #print(portion_y)
                                    if portion_y % 1 == 0 and tab[i + int(portion_y)][j + portion_x] == 1:
                                        break
                                else:
                                    #print("detected ++", l, k)
                                    detected += 1
                #print("detected =", detected)
                if detected > max[0]:
                    max[0] = detected
                    max[1] = j
                    max[2] = i
    print("max =", max)


if __name__ == "__main__":
    main()