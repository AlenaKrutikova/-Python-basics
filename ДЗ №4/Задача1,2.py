import struct
import random

a = int(input())
b = int(input())
size_ls = 10
ls = []

def CreateBinaryFile(filename: str, ls, a, b, size_ls):
    file = open(filename, 'wb')
    for i in range(size_ls):
        ls.append(random.randint(a, b))   
    file.write(struct.pack('>' + 'l' * size_ls, *ls))
    file.close()
    return ls
    
def ReadBinaryFile(filename: str, ls, a, b, size_ls) -> list:
    file = open(filename, 'rb')
    row = file.read()
    txt = struct.unpack('>' + 'l' * (len(row) // 4), row)
    file.close()
    return list(txt)

ls = CreateBinaryFile('Бинарный файл', ls, a, b, size_ls)
print(ReadBinaryFile('Бинарный файл', ls, a, b, size_ls))

max_value = max(ls)
min_value = min(ls)
average_value = sum(ls) / len(ls)
ls.sort()
mediana = ls[len(ls) // 2]

print(max_value, min_value, average_value, mediana)


