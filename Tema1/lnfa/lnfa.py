def lnfa(cuvant):
    # Possible states through the letter
    def starePrinLitera(stare_, litera_):
        stariLitere = set()
        for tranzitie in tranzitii:
            if tranzitie[0] == stare_ and tranzitie[1] == litera_:
                stariLitere.add(tranzitie[2])
        return stariLitere

    # Possible states through the lambda
    def starePrinLambda(stari_):
        stariLambda = set(stari_)
        while True: # go deeper with lambda
            tranzitiiNoi = set()
            for stare_ in stariLambda:
                for tranzitie in tranzitii:
                    if tranzitie[0] == stare_ and tranzitie[1] == '.':
                        tranzitiiNoi.add(tranzitie[2])
            if tranzitiiNoi.issubset(stariLambda):
                break # stop if there isn't ant state left
            stariLambda |= tranzitiiNoi
        return stariLambda

    for i in range(1, 6):
        print(starePrinLambda([str(i)]))

    stariCurente = starePrinLambda({stareaInitiala})
    
    for litera in cuvant:
        stariViitoare = set()
        for stare in stariCurente:
            tranzitie = starePrinLitera(stare, litera)
            stariViitoare |= tranzitie
        stariCurente = starePrinLambda(stariViitoare)
    for stare in stariCurente:
        if stare in stariFinale:
            return True
    else:
        return False

# Input from file
with open("input_lnfa_greu.txt") as f:
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

# Output in file
with open("output_lnfa_greu_fabi.txt", "w") as g:
    for cuvant in cuvinte:
        if(lnfa(cuvant) == True):
            g.write("DA\n")
        else:
            g.write("NU\n")
