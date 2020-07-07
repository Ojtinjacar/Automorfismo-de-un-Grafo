import collections

arrayvertices = []
arrayvertices = ['1','2','3','4','5','6']
arrayaristas = { 12: ("1","2"),23:("2","3"), 13:("1","3"),34:("3","4"),45:("4","5"),46:("4","6"),56:("5","6") }
arrayaristas2 = collections.OrderedDict(sorted(arrayaristas.items()))
def Permutar(Vertices):
    if len(Vertices) == 0:
        return ['']
    ListaPrevia = Permutar(Vertices[1:len(Vertices)])
    Resultado = []
    for i in range(0, len(ListaPrevia)):
        for j in range(0, len(Vertices)):
            newString = ListaPrevia[i][0:j] + Vertices[0] + ListaPrevia[i][j:len(Vertices) - 1]
            if newString not in Resultado:
                Resultado.append(newString)
    return Resultado


Permutaciones = Permutar(arrayvertices)
def CompararCadenas(Original, Permuta):
    Newarray = []
    for a in Permuta:
        Newarray.append(a)
    Diccionario = {}
    for a in range(len(Original)):
        Diccionario.setdefault(Original[a], Permuta[a])
    tuplaciclo = []
    A = []
    for b in Diccionario:
        if Diccionario.get(b) != b:
            if DiccionarioFlag.get(b) != True:
                tuplaciclo.append(b)
                DiccionarioAux = {b: True}
                DiccionarioFlag.update(DiccionarioAux)
                recorridoPermuta(Diccionario, Diccionario.get(b),tuplaciclo)
                tuplaciclo = []
    return Diccionario

def recorridoPermuta(Diccionario, Valor,TuplaFinal):
    if Diccionario.get(Valor) != Valor:
        if DiccionarioFlag.get(Valor) != True:
            TuplaFinal.append(Valor)
            DiccionarioAux = {Valor: True}
            DiccionarioFlag.update(DiccionarioAux)
            recorridoPermuta(Diccionario, Diccionario.get(Valor),TuplaFinal)
        else:
            arryfinal.append(TuplaFinal)

def DefinirAutomorfismo(Diccionario2):
    newDiccionario = {}
    for a in arrayaristas2:
        Tupla = arrayaristas.get(a)
        Pos1 = Diccionario2.get(Tupla[0])
        Pos2 = Diccionario2.get(Tupla[1])

        TuplaFinal = (Pos1,Pos2)
        r = sorted(TuplaFinal,reverse=False)
        tuplar = (r[0],r[1])
        newDiccionario.setdefault(int(r[0]+r[1]),tuplar)
    if newDiccionario == arrayaristas2:
        return 1
    else:
        return 0

for c in Permutaciones:
    DiccionarioFlag = {}
    for a in arrayvertices:
        DiccionarioFlag.setdefault(a, False)
    tuplaciclo = []
    arryfinal = []
    b = CompararCadenas(arrayvertices, c)
    t = DefinirAutomorfismo(b)
    if t == 1:
        print(arryfinal)

