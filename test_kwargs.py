def suma(**kwargs):
    sum = 0
    for key, value in kwargs.items():
        print(key, " = ", value)
        sum += value
    return sum

print(suma(a=2, b=5, c=9))