dice = {}
tulpeList = []

for i in range(1,7):
    for j in range(1,7):
        pair = (i,j)
        v = dice.setdefault(sum(pair),set()) # przypisuje na zmienną v wartości słownika o sumie oczek z dwóch rzutów (i-ta kolejka). Jeśli w kluczach słownika dice nie było do tej pory tej wartości to przypisuje na v wartość default = "set()" "zbiór pusty"
        v = v | {pair} # rozszeżenie słownika o zbiór jednoelementowy zawierający i-tą tuple (krotkę) 
        dice[sum(pair)] = v # nadpisanie wartości słownika o "wzbogaconą" zmienną v

for k, v in dice.items():
    print(k, end =" "); print(v)
    #print("Dla wartości", k, end =" "); print("pary oczek:", v)


