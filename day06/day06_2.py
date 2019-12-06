import math

def main():
    f = open("input.txt", "r")
    tab = []
    dictio = {}
    for x in f:
        tab.append(x.split(")"))
    for x in tab:
        if x[0][0:3] in dictio:
            dictio[x[0][0:3]]["nb_next"] += 1
        else:
            dictio[x[0][0:3]] = {}
            dictio[x[0][0:3]]["nb_next"] = 1
            dictio[x[0][0:3]]["len"] = 0
            dictio[x[0][0:3]]["next"] = []
        dictio[x[0][0:3]]["next"].append(x[1][0:3])
        if x[1][0:3] not in dictio:
            dictio[x[1][0:3]] = {}
            dictio[x[1][0:3]]["nb_next"] = 0
            dictio[x[1][0:3]]["len"] = 0
            dictio[x[1][0:3]]["next"] = []
        dictio[x[1][0:3]]["prev"] = x[0][0:3] 
    rec("COM", dictio, 0)
    #print(dictio)
    #result = 0
    #for x in dictio:
    #    result += dictio[x]["len"] * dictio[x]["nb_next"]
    #print(result)
    precedent1 = "SAN"
    precedent2 = "YOU"
    while 1:
        if precedent1 == "COM" and precedent2 == "COM":
            break
        print(precedent1, precedent2)
        if "prev" in dictio[precedent1]:
            precedent1 = dictio[precedent1]["prev"]
        if "prev" in dictio[precedent2]:
            precedent2 = dictio[precedent2]["prev"]

def rec(name, dictio, previous):
    if name in dictio:
        dictio[name]["len"] = previous + 1
        for x in dictio[name]["next"]:
            rec(x, dictio, dictio[name]["len"])


if __name__ == "__main__":
    main()