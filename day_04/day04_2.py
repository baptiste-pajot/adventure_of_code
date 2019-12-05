nb_psswd_ok = 0
l = 6
for i in range(359282, 820401 + 1):
    txt = str(i)
    if len(txt) == 6:
        cond = 0
        for j in range(l - 2):
            if int(txt[j]) > int(txt[j + 1]) or int(txt[j + 1]) > int(txt[j + 2]):
                cond = 0
                break
            if j == 0 and int(txt[j]) == int(txt[j + 1]) and int(txt[j + 1]) != int(txt[j + 2]):
                cond = 1
            elif j == l - 3 and int(txt[j]) != int(txt[j + 1]) and int(txt[j + 1]) == int(txt[j + 2]):
                cond = 1
            elif int(txt[j - 1]) != int(txt[j]) and int(txt[j]) == int(txt[j + 1]) and int(txt[j + 1]) != int(txt[j + 2]):
                cond = 1
        if cond == 1:
            nb_psswd_ok += 1
print(nb_psswd_ok)
