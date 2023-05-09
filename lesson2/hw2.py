print("task 1")
a = 10
p = a * 4
s = a ** 2
d = (2 ** 0.5) * a
print("Периметр", p, "\n", "Площадь", s, "\n", "Диагональ", d)

print("task 2")
a = 1
b = -5
c = 4
dis = b ** 2 - 4 * a * c
x1 = round((-1 * b + dis ** 0.5 / 2 * a), 2)
x2 = round((-1 * b - dis ** 0.5 / 2 * a), 2)
print("корень1=", x1, "\n", "Корень2=", x2)

print("task 3")
string1 = "надо"
string2 = "делать"
print(string1.replace(string1[:2], string2[:2]) + " " + string2.replace(string2[:2], string1[:2]))

print("task 4")
path = r"D:\projects\homework\hw2.py"
div = path.split('\\')
file = div[-1]
direct = div[1]
disk = div[0]
print("disk=", disk.split(':')[0], "\n", "directory=", direct, "\n", "file=", file.split('.')[0])

print("task 5")
a = 4
b = 5
s = a + b
y = a * b
result = f"""
cумма чисел {a}+{b}={s}
умножение чисел {a}*{b}={y}
"""
print(result)

print("task 6")
string = "надо сразу делать домашнее задание"
print(string[::2])

print("task 7")
string1 = "wtf"
string2 = "brick quz jmpv veldt whangs fox"
a = string2.find(string1[0])
b = string2.find(string1[1])
c = string2.find(string1[2])
print(string2[min(a, b, c):max(a, b, c)+1])
