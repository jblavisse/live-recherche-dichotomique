# Variable t en Entiers[] -> Déjà rempli
t = [3, 7, 11, 15, 22, 37]
# Variable val en Entier -> Donnée déjà remplie
val = 37

# Variable mil, deb, fin en Entier
# Variable trv en Booléen
# Variable pos en Entier

# trv = FAUX
trv = False
# deb = 0
deb = 0
# fin = longueur de t - 1
fin = len(t)-1

pos=-1

# Tant que trv == FAUX
while not trv and deb <= fin:
#    mil = partie_entiere((deb+fin) /2)
    mil = (deb+fin) // 2

    if t[mil] == val:
        trv = True
        pos = mil
    elif t[mil] < val:
        deb = mil+1
    elif t[mil] > val:
        fin = mil-1

# Ecrire pos
print(pos)