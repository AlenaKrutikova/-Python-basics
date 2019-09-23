str = input()
for char in str:
    if char in " ,?.!/;:":
        str = str.replace(char,'')
newstr = ''.join(reversed(str.lower()))
print(newstr == str.lower())
