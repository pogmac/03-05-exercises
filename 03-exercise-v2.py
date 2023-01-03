models = ['Volkswagen - Golf','Renault - Clio','Volkswagen - Polo',
'Ford - Fiesta','Nissan - Qashqai','Peugeot - 208','VW - Tiguan','Skoda - Octavia',
'Toyota - Yaris','Opel - Corsa','Dacia - Sandero','Renault - Captur','Citroen - C3',
'Peugeot - 3008','Ford - Focus','Fiat - 500','Dacia - Duster','Peugeot - 2008',
'Skoda - Fabia','Fiat - Panda','Opel - Astra','VW - Passat','Mercedes-Benz - A-Class',
'Peugeot - 308','Ford - Kuga']

sales2018 = ['445,754','336,268','299,920','270,738','233,026','230,049','224,788',
'223,352','217,642','217,036','216,306','214,720','210,082','204,197','196,583',
'191,205','182,100','180,204','172,511','168,697','160,275','157,986','156,020',
'155,925','154,125']

sales2017 = ['483,105','327,395','272,061','254,539','247,939','244,615','234,916',
'230,116','199,182','232,738','196,067','212,768','207,299','166,784','214,661',
'189,928','NA','180,868','180,136','187,322','217,813','184,123','NA','NA','NA']

sales2016 = ['492,952','315,115','308,561','300,528','234,340','249,047','180,198',
'230,255','193,969','264,844','170,300','217,105','134,560','NA','214,435',
'183,730','NA','NA','177,301','191,617','253,483','208,575','NA','195,653','NA']

answer1 = "" # wskaż nazwę modelu jako string
answer2 = "" # wskaż producenta jako string
answer3 = [] # wskaż odpowiedź jako listę zawierającą wszystkie modele spełniające kryteria
answer4 = "" # wskaż nazwę modelu jako string
answer5 = "" # odpowiedź podaj w formacie procentowym jako string. Np. '21%'

cars = {} #print(len(models));print((len(sales2016)));print((len(sales2017)));print((len(sales2018)))

j = 0
for i in zip(models,sales2018,sales2017,sales2016): # Tworzymy słownik z czterech list
  brand,model = i[0].split(" - ")
#  print(brand, end = " "); print(model)
  brand_models = cars.setdefault(brand,{})
#  print(brand_models)
  brand_model_sales = brand_models.setdefault(model,{})
#  print(brand_model_sales)
  brand_model_sales["sales"] = {"2016": 0 if i[3] == "NA" else int(i[3].replace(',',"")),
                                "2017": 0 if i[2] == "NA" else int(i[2].replace(',',"")),
                                "2018": 0 if i[1] == "NA" else int(i[1].replace(',',""))}
 # print(brand_model_sales["sales"]["2016"])
print();print()
#print(cars)  


#Zadanie1
#Który model samochodu z listy najlepiej sprzedawał się w 2017 roku? Odpowiedź przypisz do zmiennej answer1.

"""
#k - company; l - model, m - sales: {}
answer1 = ""
maxSales2017 = 0
year = "2017"

for k,v in cars.items():
    #print(v)
    for l,m in v.items(): 
        #print(l)
        #print(k)
        #print(l)
        #print(m)
        for n,o in m.items():
        #    print(n)
        #    print(o)
            for p, r in o.items():
                #print (p, end =" "); print(r)
                if p != year:
                    continue
                else:
         #          print("year =", year)
                    if r > maxSales2017:
                        maxSales2017 = r 
         #               print("maxSales2017 =", maxSales2017)
         #               print("najczeszczy =", l)
                        answer = l
                    else: 
                        pass    

print("Najczęściej sprzedawany model samochodu w roku",year, "to", answer, "sprzedaż = ",maxSales2017)
"""

#Zadanie2
#Który producent z listy sprzedał najwięcej egzemplarzy samochodów w 2018 roku? Odpowiedź przypisz do zmiennej answer2.

"""
#k - company; l - model, m - sales: {}
answer2 = ""
maxSales2018 = 0
year = "2018"
sales2018 = {} # dictionary

for k,v in cars.items():
    #print(v)
    for l,m in v.items(): 
 #       print(k)
 #       print(l)
        for n,o in m.items():
        #    print(n)
        #    print(o)
            for p, r in o.items():
#               print (p, end =" "); print(r)
                if p != year:
                    continue
                else:
                    s = sales2018.setdefault(k,0)
                    s = s + r
                    sales2018[k] = s
#                   print(sales2018[k])
                    if sales2018[k] > maxSales2018:
                        maxSales2018 = sales2018[k]
                        answer2 = k 
#                        print("maxSales2018 =", maxSales2018)
#                        print("najczeszczy =", k)

print("Najczęściej wybierana firma samochodowa w roku",year, "to", answer2,"sprzeraż =", maxSales2018)
"""

#Zadanie 3
#Ile modeli samochodów z listy nie sprzedawało się w 2016 roku, a do sprzedaży weszło w roku 2017? Odpowiedź przypisz do zmiennej answer3.
"""
#k - company; l - model, m - sales: {}
answer3 = []
maxSales2018 = 0
year2 = "2017"
year1 = "2016"
sales201617 = {} # słownik 

for k,v in cars.items():
    #print(v)
    for l,m in v.items(): 
 #       print(k)
 #       print(l)
        for n,o in m.items():
        #    print(n)
            print(o)
            if o[year1] == 0 and o[year2] !=0:
                answer3.append(l)
#            for p, r in o.items():
#                print(p)
#               print (p, end =" "); print(r)


print("modele które były sprzedawane w ",year2, "ale nie w", year1,"to", answer3)
"""
#Zadanie 4
#Który z model samochodu z listy ma najmniej sprzedanych egzemplarzy, jeśli weźmiemy pod uwagę lata 2016, 2017 oraz 2018. Odpowiedź przypisz do zmiennej answer4.
"""
#k - company; l - model, m - sales: {}
answer4 = ""
sales20161718 ={} # dictionary
minSales20161718 = 1000000

for k,v in cars.items():
    #print(v)
    for l,m in v.items(): 
        #print(k)
        #print(l)
        #print(m)
        for n,o in m.items():
        #    print(n)
        #    print(o)
            for p, r in o.items():
        #        print (p, end =" "); print(r)
                s = sales20161718.setdefault(l,0)
                s = s + r
                sales20161718[l] = s
       #     print("sales combined" ,sales20161718[l])
            if sales20161718[l] < minSales20161718:
                minSales20161718 = sales20161718[l]
           #     print("bingo! nowe minium znalezione!")
                answer4 = l
       
#print(sales20161718)
#print(answer4)
print("Najrzadziej sprzedawany model samochodu w latach 2016-2018 to", answer4, "sprzedaż = ",minSales20161718)
"""

#Zadanie 5
#O ile procent wzrosła sprzedaż modeli Forda w 2018 roku w stosunku do roku 2017? Odpowiedź przypisz do zmiennej answer5. Odpowiedź podaj w formacie procentowym jako string. Np. '21%'.

#k - company; l - model, m - sales: {}
answer5 = ""
salesFord2018vs2017 ={} # dictionary
salesF2018 = 0
salesF2017 = 0
for k,v in cars.items():
    if k != "Ford":
        continue
    print(k)
    #print(v)
    for l,m in v.items(): 
        #print(k)
        print(l)
        #print(m)
        for n,o in m.items():
        #    print(n)
        #    print(o)
            for p, r in o.items():
                if p == "2016":
                    continue
                    print(p)
                elif p == "2017":
                    salesF2017 = r
                    print(p)
                else: # p == "2018"
                    salesF2018 = r
                    print(p)
                print (p, end =" "); print(r)
            if salesF2017 != 0:
                salesFord2018vs2017[l] = str(round((salesF2018/salesF2017 - 1)*100,2))+'%'
            else:
                salesFord2018vs2017[l] = "N/A" 
            print(salesFord2018vs2017)    

#print("Najrzadziej sprzedawany model samochodu w latach 2016-2018 to", answer4, "sprzedaż = ",minSales20161718)


"""
        v = dice.setdefault(sum(pair),set())
        v = v | {pair}
        dice[sum(pair)] = v
"""

"""
cars2 = {"Opel": {"Corsa":{"sales":{"2016": 264844,
                                   "2017": 232738,
                                   "2018": 217036}},
                 "Astra":{"sales":{"2016": 253483,
                                   "2017": 217813,
                                   "2018": 160275}}
                 },
        "Dacia": ... }
"""
 