
# from john/math import geo.py
from john.math import geo
import sys

a1 = geo.circle_area(21)
print("a1: {}".format(a1))
print(geo.rectangle_area(10, 8))
print(geo.square_area(1.3))
print(geo.ANIMAL)
print('-' * 60)
# 1. current folder
# 2. folders in PYTHONPATH
# 3. installation folders

for folder in sys.path:
    print(folder)

print()
print(sys.executable)

