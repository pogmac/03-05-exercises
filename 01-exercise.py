print()
print("")
print()

numbers = [5,32,56,2,2,16,7,10,23,100]
mean_number = 0

numberMin = 0
numberMax = 0
# numbersNew = [], for i in range 
listMean = 0

for i in range(len(numbers)):
    numbers[i] = round(numbers[i]/10+0.000001)*10
#    if numbers[i]> numberMax: # rozwiązanie min max na około. Lepiej użyć finkcji listy min i max
#        numberMax = numbers[i]
#    if numbers[i] < numberMin:
#        numberMin = numbers[i]

numbers.remove(min(numbers))
numbers.remove(max(numbers))

#print(numberMin, numberMax)    
#print(numbers)

numbers = [number for number in numbers if (number != numberMin and number != numberMax)]
listMean = round(sum(numbers)/len(numbers),2)

print()
print("new list = ",numbers)
print("listMean = ", listMean)
print()


    

    

    

