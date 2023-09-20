def function(x, y):
    if x > 8:
        z = 3 + y
        return z
    elif x <= 8:
        z = 9 * x * y
        return z
def f(n):
    z = 1
    for i in range(1, n+1):
        z *= i
    return z

x = int(input("Введіть значення х: "))
y = int(input("Введіть значення y: "))
print("Значення виразу z = ", function(x, y))
n = int(input("Введіть число n для визначення факторіалу: "))
print(n, "! =", f(n))