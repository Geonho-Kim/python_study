a, b  = input().split()
a = int(a)
b = int(b)
if b >= 45:
    print(a,b-45)
elif b < 45:
    if a == 0:
        a = 23
        b = 60 - 45 + b
        print(a, b)
    else:
        b = 60 - 45 + b
        print(a-1, b)
