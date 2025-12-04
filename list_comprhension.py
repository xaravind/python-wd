l = []

for i in range(10):
    l.append(i)

print(l)

# reducing above lines
l1 = [x for x in range(10)]
print(l1)
l2 = [x**2 for x in range(10)]
print(l2)
 
d3 = {l1[i]:l2[i] for i in range(len(l1))}

print(d3)

d2 = {x:x**2 for x in range(10)}

print(d2)