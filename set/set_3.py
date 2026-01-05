from unicodedata import name

set_sym={chr(i) for i in range(32,256) if 'SIGN' in name(chr(i),'')}
print(set_sym)

s={1,2,3,4,5}
u={4,5,6}
print(s | u)
# print(s ^ u) #symmetric differemce

