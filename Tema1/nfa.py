with open("input.txt") as f:
    numarStari = int(f.readline())
    stari = [x for x in f.readline().split()]
    numarLitere = int(f.readline())
    litere = [x for x in f.readline().split()]
    stareaInitiala = f.readline().strip()
    numarStariFinale = int(f.readline())
    stariFinale = [x for x in f.readline().split()]
    numarTranzitii = int(f.readline())
    tranzitii = set()
    for i in range(numarTranzitii):
        tranzitii.add(tuple(f.readline().split()))
    tranzitii=list(tranzitii)
    numarCuvinte = int(f.readline())
    cuvinte = []
    for i in range(numarCuvinte):
        cuvinte.append(f.readline().strip())

# print(numarStari)
# print(stari)
# print(numarLitere)
# print(litere)
# print(stareaInitiala)
# print(numarStariFinale)
# print(stariFinale)
# print(numarTranzitii)
# print(tranzitii)
# print(numarCuvinte)
# print(cuvinte)

def starePrinLitera(stare_, litera_):
    multime = set()
    for tranzitie in tranzitii:
        if tranzitie[0] == stare_ and tranzitie[1] == litera_:
            multime.add(tranzitie[2])
    return multime

def nfa(cuvant):
    stariCurente = {stareaInitiala}
    for litera in cuvant:
        stariViitoare = set()
        for stare in stariCurente:
            tranzitie = starePrinLitera(stare, litera)
            stariViitoare |= tranzitie;
        stariCurente = stariViitoare
    return any(stare in stariFinale for stare in stariCurente)

with open("output.txt", "w") as g:
    for cuvant in cuvinte:
        if(nfa(cuvant) == True):
            g.write("DA\n")
        else:
            g.write("NU\n")
