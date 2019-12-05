nb_psswd_ok = 0
l = 6
for i in range(359282, 820401 + 1):
    txt = str(i)
    if len(txt) == 6:
        cond = 0
        for j in range(l - 1):
            if int(txt[j]) > int(txt[j + 1]):
                cond = 0
                break
            if int(txt[j]) == int(txt[j + 1]):
                cond = 1
        if cond == 1:
            nb_psswd_ok += 1
print(nb_psswd_ok)
