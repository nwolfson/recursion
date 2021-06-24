import matplotlib.pyplot as plt
import numpy as np
import collections
m1 = []
m2 = []
m3 = []
m4 = []
m5 = []
n1 = [0.5, 0.05, 0.0095, 0.001882, 0.000376]    #
n2 = [0.5, 0.125, 0.054688, 0.025848, 0.01259]  # получено в маткаде
n3 = [0.5, 0.25, 0.1875, 0.152344, 0.129135]    #
m1test = []
m2test = []
m3test = []

def a(n, r=0.2):
    n = int(n)
    if n == 0:
        return 0.5
    else:
        x = a(n - 1, r=r)
        return r * x * (1 - x)
for i in range(100):
    m1.append(a(i))

def a(n, r=0.5):
    n = int(n)
    if n == 0:
        return 0.5
    else:
        x = a(n - 1, r=r)
        return r * x * (1 - x)
for i in range(100):
    m2.append(a(i))

def a(n, r=1):
    n = int(n)
    if n == 0:
        return 0.5
    else:
        x = a(n - 1, r=r)
        return x * (1 - x)
for i in range(100):
    m3.append(a(i))

def a(n, r=2):
    n = int(n)
    if n == 0:
        return 0.5
    else:
        x = a(n - 1, r=r)
        return r * x * (1 - x)
for i in range(100):
    m4.append(a(i))

def a(n, r=3):
    n = int(n)
    if n == 0:
        return 0.5
    else:
        x = a(n - 1, r=r)
        return r * x * (1 - x)
for i in range(100):
    m5.append(a(i))

print("m1=", m1, "m2=", m2, "m3=", m3, "m4=", m4, "m5=", m5)

# Построение графиков

q = np.linspace(0, 100, 100)
plt.figure(dpi=100)
plt.plot(q, m1, color='m', linewidth=2)
plt.plot(q, m2, color='b', linewidth=2)
plt.plot(q, m3, color='g', linewidth=2)
plt.plot(q, m4, color='r', linewidth=2)
plt.plot(q, m5, color='y', linewidth=2)
plt.xlabel('n', fontsize=15)
plt.ylabel('x(n)', fontsize=15)
plt.grid()
plt.show()

# Тесты

def a(n, r=0.2):
    n = int(n)
    if n == 0:
        return 0.5
    else:
        x = a(n - 1, r=r)
        return r * x * (1 - x)

for i in range(5):
    m1test.append(a(i))

def a(n, r=0.5):
    n = int(n)
    if n == 0:
        return 0.5
    else:
        x = a(n - 1, r=r)
        return r * x * (1 - x)

for i in range(5):  # беру 5 элементов для простоты
    m2test.append(a(i))

def a(n, r=1):
    n = int(n)
    if n == 0:
        return (0.5)
    else:
        x = a(n - 1, r=r)
        return r * x * (1 - x)

for i in range(5):  # беру 5 элементов для простоты
    m3test.append(a(i))

m1test1 = [round(t, 6) for t in m1test]  #
m2test1 = [round(t, 6) for t in m2test]  # округление списков для r=0.2, 0.5, 1 до 6 знаков
m3test1 = [round(t, 6) for t in m3test]  #

print("m1test1=", m1test1, "n1=", n1)
if collections.Counter(n1) == collections.Counter(m1test1):  # сравнение списков
    print("Списки одинаковые")
else:
    print("Списки неодинаковые")

print("m2test1=", m2test1, "n2=", n2)
if collections.Counter(n2) == collections.Counter(m2test1):  # сравнение списков
    print("Списки одинаковые")
else:
    print("Списки неодинаковые")

print("m3test1=", m2test1, "n3=", n3)
if collections.Counter(n3) == collections.Counter(m3test1):  # сравнение списков
    print("Списки одинаковые")
else:
    print("Списки неодинаковые")
