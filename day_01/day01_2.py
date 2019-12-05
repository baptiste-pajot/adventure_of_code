import math

def fuel(mass):
    return(math.floor(mass/ 3) - 2)

def recursive(mass):
    mass_fuel = fuel(mass) 
    #print(mass_fuel)
    if mass_fuel > 0:
        mass_fuel += recursive(mass_fuel)
    else:
        return(0)
    return(mass_fuel)

def main():
    f = open("input.txt", "r")
    result = 0
    for x in f:
        result += recursive(int(x))
    print(result)

if __name__ == "__main__":
    main()