print("Введите название фигуры")
figure = input()
print("Введите координату Х")
x = int(input())
print("Введите координату У")
y = int(input())
l = []

def remover() :
    rem = []
    for el in l :
        if (el[0] < 1 or el[0] > 8 or el[1] < 1 or el[1] > 8) :
            rem.append(el)
    for el in rem :
        l.remove(el)
    print(l)
    
if figure.lower() == "пешка" :
    l. append((x, y+1))
    remover()                        

elif figure.lower() == "ладья" :
    for el in range(8) :
        if el > 0 :
            l.extend([(x, y+el), (x, y-el), (x+el, y), (x-el, y)])
    remover()      

elif figure.lower() == "король" :
    l.extend([(x, y-1), (x, y+1), (x-1, y), (x+1, y), (x+1, y+1), (x+1, y-1), (x-1, y+1), (x-1, y-1)])
    remover()

elif figure.lower() == "слон" :
    for el in range(8) :
        if el > 0 :
            l.extend([(x+el, y+el), (x-el, y-el), (x+el, y-el), (x-el, y+el)])
    remover()        

elif figure.lower() == "конь" :
    l.extend([(x-2, y-1), (x-2, y+1), (x-1, y-2), (x-1, y+2), (x+1, y-2), (x+1, y+2), (x+2, y-1), (x+2, y+1)])
    remover()

elif figure.lower() == "ферзь" :
    for el in range(8) :
        if el > 0 :
            l.extend([(x+el, y+el), (x-el, y-el), (x+el, y-el), (x-el, y+el), (x, y+el), (x, y-el), (x+el, y), (x-el, y)])
    remover()
    
else : print("Такой фигуры нет")



