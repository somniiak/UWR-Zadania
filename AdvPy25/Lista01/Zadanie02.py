import re

def is_palindrom(s):
    s = re.sub(r"[^\w]", "", s.lower())
    return s == s[::-1]

x = is_palindrom("Eine güldne, gute Tugend: Lüge nie!")
print(x)
y = is_palindrom("Míč omočím")
print(y)