fn = lambda  x: x**2

print(fn(10))
print(fn(20))
l1 =[10,20,30,40,50]
l2 = [(x)**2 for x in (l1)]

print(l2)

l3 = [fn(x) for x in (l1)]
print(l3)

data= [
    ('Arjun', 95),
    ('Hari', 88),
    ('Seema', 96),
    ('Raju', 75)
]

sorted_by_score= sorted(data, key= lambda x: x[1])

print(sorted_by_score)