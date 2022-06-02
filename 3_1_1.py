def f(x):
    if x <= -2: return 1-(x+2)**2
    elif -2 < x <= 2: return (x/2)*(-1)
    elif x > 2: return (x-2)**2 + 1
y = float(input())
print(f(y))