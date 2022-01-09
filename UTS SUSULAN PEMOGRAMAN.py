a = int(input("Bilangan 1: "))
b = int(input("Bilangan 2: "))
c = int(input("Bilangan 3: "))
maks = 0

print(a, b, c)
if a > b:
    maks = a
else:
    maks = b

if c > maks:
    maks = c

print("Bilangan terbesar adalah",maks)