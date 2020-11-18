student1 = ('00008883', '19', 'Tashkent')
student2 = ('00009623', '20', 'Andijan')

id1 = tuple(student1[0])
id2 = tuple(student2[0])

age1 = tuple(student1[1])
age2 = tuple(student2[1])

place1 = tuple(student1[2])
place2 = tuple(student2[2])

print(id1>id2)
print(age1>age2)
print(place1>place2)