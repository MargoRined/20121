import numpy as np
import matplotlib.pyplot as plt
from SumPy import diff
from scipy.integrate import quad

# Вывод первой и второй производной 
x = Symbol("x")
fx = np.sin(x) * np.cos(x ** 2 + 5)
x1 = np.linspace(0, 5, 100)
fx1 = fx.diff(x)
fx2 = fx1.diff(x)
plt.figure(figsize = (12, 0))
plt.subplot(3, 1, 1)
plt.plot(x1, fx, label='f(x) = sin(x) * cos(x^2 + 5)')
plt.title('График функции')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.legend()
plt.subplot(3, 1, 2)
plt.plot(x1, fx1, label="f'(x)", color='orange')
plt.title('Первая производная')
plt.xlabel('x')
plt.ylabel("f'(x)")
plt.grid()
plt.legend()
plt.subplot(3, 1, 3)
plt.plot(x1, fx2, label="f''(x)", color='green')
plt.title('Вторая производная')
plt.xlabel('x')
plt.ylabel("f''(x)")
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()

# наибольшее и наименьшее значение функции 
max_value = np.max(fx)
min_value = np.min(fx)
max_index = np.argmax(fx)
min_index = np.argmin(fx)
plt.figure(figsize=(8, 6))
plt.plot(x1, fx, label='f(x)')
plt.plot([x1[max_index]], [max_value], 'o', color='b', label='Максимум')
plt.plot([x1[min_index]], [min_value], 'o', color='r', label='Минимум')
plt.title('График функции с максимумом и минимумом')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.legend()
plt.show()

print(f"Наибольшее значение: {max_value} при x = {x[max_index]}")
print(f"Наименьшее значение: {min_value} при x = {x[min_index]}")

# Построение касательной и нормали
x0 = x1[max_index]
slope = fx1(x0)
tangent_eq = lambda x: slope * (x - x0) + max_value
normal_eq = lambda x: -1/slope * (x - x0) + max_value
plt.figure(figsize=(8, 6))
plt.plot(x1, fx, label='f(x)')
plt.plot([x0], [max_value], 'o', color='b', label='Максимум')
plt.plot(x1, tangent_eq(x1), '--', color='orange', label='Касательная')
plt.plot(x1, normal_eq(x1), '--', color='green', label='Нормаль')
plt.title('Касательная и нормаль к функции')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.legend()
plt.show()

# касательное расслоение 
plt.figure(figsize=(8, 6))
for xi in np.linspace(0, 5, 10):
    slope = fx1(xi)
    plt.plot(x1, fx(xi) + slope * (x1 - xi), '--', color='gray', alpha=0.5)
plt.plot(x1, fx, label='f(x)')
plt.title('Касательное расслоение')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.legend()
plt.show()

# длина кривой через интеграл
x2 = np.sqrt(1 + (fx1(x1))**2)
length, _ = quad(x2, 0, 5)

print(f"Длина кривой: {length}")