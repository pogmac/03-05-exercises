dice = {}
tulpeList = []

for i in range(1,7):
    for j in range(1,7):
        pair = (i,j)
        v = dice.setdefault(sum(pair),set())
        v = v | {pair}
        dice[sum(pair)] = v

for k, v in dice.items():
    print("Dla wartości", k, end =" "); print("pary oczek:", v)


