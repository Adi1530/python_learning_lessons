import unicodedata

s1 = 'é'                   # single code point
s2 = 'e\u0301'             # 'e' + combining accent

print(s1 == s2)             # False

# Normalize before comparing
s1_n = unicodedata.normalize('NFC', s1)
s2_n = unicodedata.normalize('NFC', s2)
print(s1_n == s2_n)         # True


def emoji_name(*args):
    for emoji in args:
        print(name(emoji))


from unicodedata import name
print(name('A'))
print(name(':'))
print(name('😍'))

emoji_name("🤤","😜","😭","😡")




