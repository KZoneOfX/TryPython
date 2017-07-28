fahrenheit = 0
print("Fahrenheit Celsius")
while fahrenheit <= 250:
    celsius = (fahrenheit - 32) / 1.8  # 转换为摄氏度
    print("{:5d} {:7.2f}".format(fahrenheit, celsius))
    fahrenheit = fahrenheit + 25

a, b = 45, 54
print("a[{}]".format(a))
print("b[{}]".format(b))
a, b = b, a
print("a[{}]".format(a))
print("b[{}]".format(b))

data = ("xiaolu", "China", "Python")
print(data)
name, country, language = data
print(name)
print(country)
print(language)