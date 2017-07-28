#  逻辑运算符
print(5 and 4)
print(5 and 4 and 0)
print(5 and 0 and 4 and 0)
print(5 and 1 and 4)
print(5 or 1 or 4)
print(0 or 5 or 1 or 4)
print(0 or 1 or 5 or 1 or 4)
print(2 > 1 and not 3 > 5 or 4)
print(2 > 1 and not 3 > 5)
print(2 > 1)
print(not 3 > 5)

N = 100
a = 2
while a < N:
    print(str(a))
    a *= a
a = 234 * (45 - 56 / 34)
print(a)
print(str(a))

a = 9
b = 12
c = 3
x = a - b / 3 + c * 2 - 1
y = a - b / (3 + c) * (2 - 1)
z = a - (b / (3 + c) * 2) - 1
print("X = ", x)
print("Y = ", y)
print("Z = ", z)

print(float(2))
print(float(3.222))
print(float("2.333"))
print(int("02"))
