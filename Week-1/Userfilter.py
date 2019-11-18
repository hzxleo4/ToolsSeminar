import re
with open("name.txt","r") as file:
    str = file.read()
    a = re.findall(r'\([0-9]*?\)[a-z][a-zA-Z_-]{4,19}',str)
    print(len(a))
    file.close()
