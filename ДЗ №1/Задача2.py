print("Введите номер билета")
ticket = input()
str1 = ticket[0: len(ticket)//2]
str2 = ticket[len(ticket)//2:len(ticket)]
sum1 = 0
sum2 = 0
for el in str1:
    sum1 += int(el)
for el in str2:
    sum2 += int(el)        
print(sum1 == sum2)    

    

    
