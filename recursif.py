# fonction recherche(t,val,deb, fin)
def recherche(t,val,deb,fin):
    if deb > fin:
        return - 1
    else:
        mil = (deb+fin) // 2
        if t[mil] == val:
            return mil
        elif t[mil] < val:
            return recherche(t,val,mil+1,fin)
        elif t[mil] > val:
            return recherche(t,val,deb,mil-1)

print(recherche([3, 7, 11, 15, 22, 37], 9, 0, 5))