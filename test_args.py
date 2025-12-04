def suma(*args):
    s = 0
    for arg in args:
        s += arg
    return s

print(suma(1,5,6,12))
print(suma(3,3))

"""
Ahora veamos la manera pitonica de hacerlo correctamente
"""

def suma_pytonica(*args):
    return sum(args)

print(f"Manera pytonica: {suma_pytonica(6,6,12)}")