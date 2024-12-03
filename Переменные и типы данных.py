# Пример 5
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)


# Пример 6
a = int(input("Введите ширину: "))
b = int(input("Введите высоту: "))
s = a * b
p = 2 * (a + b)
print("Площадь", s)
print("Периметр", p)


# Пример 7
n = int(input("С начала суток прошло: "))
h = (n // 60) % 24
n = n % 60
print(h, ":", n)


# Пример 8
a = int(input("Колличество в первом: "))
b = int(input("Колличество во втором: "))
c = int(input("Колличество в третьем: "))
kol_1 = a // 2 + a % 2
kol_2 = b // 2 + b % 2
kol_3 = c // 2 + c % 2
print(kol_1 + kol_2 + kol_3)


