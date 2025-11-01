a, b, c = 10, 20, 30
a = a ^ b ^ c
b = a ^ b ^ c
c = a ^ b ^ c
a = a ^ b ^ c
print(a, b, c)
