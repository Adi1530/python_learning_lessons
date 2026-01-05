text = 'python'
encoded = text.encode('ascii')
print(encoded)
print(type(encoded))
print("-----------")
decoded=encoded.decode("utf-8")
print(decoded)
print(type(decoded))


try:
    decoded=encoded.decode("utf-32")
    print(decoded)
except UnicodeDecodeError as e:
    print(e)

rough='Hiiiii'
encoded_rough=rough.encode("utf-16")
print(encoded_rough)

