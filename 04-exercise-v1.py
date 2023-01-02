dice = {}
tulpeList = []

for i in range(1,7):
    for j in range(1,7):
        tulpeList.append((i,j))

#print(tulpeList);print(len(tulpeList));print(type(tulpeList))

sumTulpeList = list(map(sum,tulpeList)) #print(sumTulpeList);print(len(sumTulpeList));print(type(sumTulpeList))

for i in range(0,len(tulpeList)):
    v = dice.setdefault(sumTulpeList[i],set()) # przypisuje na zmienną v wartości słownika o sumie oczek z dwóch rzutów (i-ta kolejka). Jeśli w kluczach słownika dice nie było do tej pory tej wartości to przypisuje na v wartość default = "set()" "zbiór pusty"
    v = v | {tulpeList[i]} # rozszeżenie słownika o zbiór jednoelementowy zawierający i-tą tuple (krotkę) 
    dice[sumTulpeList[i]] = v # nadpisanie wartości słownika o "wzbogaconą" zmienną v
#   print(v)

for k, v in dice.items():
    print("Dla wartości", k, end =" "); print("występują następujące pary oczek:", v)
#print(dice)

