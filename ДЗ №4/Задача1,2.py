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
    print(ls)    
    file.write(struct.pack('>' + 'l' * size_ls, *ls))
    file.close()
    
def ReadBinaryFile(filename: str, ls, a, b, size_ls) -> list:
    file = open(filename, 'rb')
    row = file.read()
    txt = struct.unpack('>' + 'l' * (len(row) // 4), row)
    file.close()
    return list(txt)

CreateBinaryFile('Бинарный файл', ls, a, b, size_ls)
print(ReadBinaryFile('Бинарный файл', ls, a, b, size_ls))

