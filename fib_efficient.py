n = 42
x, y = 1, 1
for i in range(3, n):
  x, y = y, y + x
print(x)
