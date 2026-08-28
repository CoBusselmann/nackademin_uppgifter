"""import math
x1 = float(input("Ange avstånd för X1: "))
x2 = float(input("Ange avstånd för X2: "))
y1 = float(input("Ange avstånd för Y1: "))
y2 = float(input("Ange avstånd för Y2: "))

utrakning = math.sqrt((x1 - x2)**2 +  (y1-y2)**2)

print(f"{utrakning:.2f}")
"""
import math
n0 = int(input("Ange startmängd: "))
t = int(input("Ange hur många år: "))
lambda_ = math.log(2) / t
n = n0 * math.exp(-lambda_ * t)
print(f"{n}")
