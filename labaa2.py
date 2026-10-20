
x = float(input("Введите значение x: "))

if -7 <= x < -3:
    y = x + 7
elif -3 <= x < -2:
    y = 4
elif -2 <= x < 2:
    y = x ** 2
elif 2 <= x <= 4:
    y = -2 * x + 8
else:
    y = None
    print("Значение x вне заданного интервала")

if y is not None:
    print("x =", x)
    print("y =", y)
