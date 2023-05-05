import math
a = input("Enter number 'a'")
b = input("Enter number 'b'")
c = input("Enter number 'c'")

x1 = (float('-b') + math.sqrt((float(b)**2 - 4 * float(a) * float(c))))/ (2 * float(a))
x2 = (float('-b') - math.sqrt((float(b)**2 - 4 * float(a) * float(c))))/ (2 * float(a))

print(x1)
print(x2)