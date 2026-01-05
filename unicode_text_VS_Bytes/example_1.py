char ='A'
print(ord(char))

print(hex(ord(char)))


char_='*'
print(ord(char_))
print(char_.encode("utf-8"))


b=b'hello'
print(type(b))
ba=bytearray(b)

print(type(ba))
print(ba[0])
ba[0]=72
print(ba)

