dict1 = {'shopid1':['userid1','userid2','userid3']}
dict2 = {'userid1':['2020-08-17 09:00','2020-08-18 08:30'], 
'userid2':['2020-08-16 11:00','2020-08-15 13:30'], 
'userid3':['2020-08-18 09:30','2020-08-18 10:00','2020-08-18 11:30']}
combined_dict ={
    'shopid1':{'userid1':['2020-08-17 09:00','2020-08-18 08:30'],
               'userid2':['2020-08-16 11:00','2020-08-15 13:30'],
               'userid3':['2020-08-18 09:30','2020-08-18 10:00','2020-08-18 11:30']}
            }
for i in combined_dict:
    print(i)
    a=combined_dict[i]
    for j in a:
        b=a[j]
        print(j)
        for k in b:
            print(k)