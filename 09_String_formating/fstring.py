# String formatting

template = "Dear {}, You are awesome. Take this {}$ bag"
a = "John"
a1 = 10000
b = "Jack"
b1 = 1000
c = "Marie"
c2 = 300

s2 = template.format(a, b1)
print(s2)
print("\n")
s1 = template.format(b, a1)
print(s1)
print("\n")
s1 = template.format(a, b)
print(s1)
print("\n")
s1 = template.format(a1, a1)
print(s1)
print("\n")
s1 = template.format(a, c)
print(s1)
print("\n")
s1 = template.format(c2, a1)
print(s1)
print("\n")
print(f"{a} you are awesome and take this {a1}$ bag")
print("\n")
print(f"{a} you are awesome and take this {a}$ bag")
print("\n")
print(f"{b} you are awesome and take this {a1}$ bag")
print("\n")
print(f"{b1} you are awesome and take this {a1}$ bag")
print("\n")
print(f"{c} you are awesome and take this {c}$ bag")
print("\n")
print(f"{a} you are awesome and take this {c2}$ bag")
print("\n")
print(f"{c2} you are awesome and take this {a1}$ bag")
