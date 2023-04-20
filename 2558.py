a, b = map(int, input().split())

x = b % 10
y = b // 10 % 10
z = b // 100 % 10

print(a * x)
print(a * y)
print(a * z)
print(a * b)



