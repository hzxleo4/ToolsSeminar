import re
with open("name.txt","r") as file:
    str = file.read()
    #str = "(1)attttttttttttt(2)afiahaaa(3)aiufdhaaaaaaaaaaaaaaaaa(4)sfaefefastsssssssststst"
    a = re.findall(r'[0-9]*?\)[a-z]{1}[a-zA-Z_-]{4,19}\(',str)
    b = re.findall(r'\([0-9]*?\)[a-z]{1}[a-zA-Z_-]{4,19}$',str)
    print(len(a)+len(b))
    #print(a)
    file.close()
