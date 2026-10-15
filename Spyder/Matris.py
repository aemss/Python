"""
matris = [
    [1,2,3],
    [4,5,6]
]

# print(matris[0] [2])

print(type(matris))

list = []
list.append([1,2,3])
list.append([4,5,6])

print(list)


numbers = list(range(1,7))

matris = [[0,0,0],[0,0,0]]
p = 0
i = 0

for i in range(2):
    for j in range(3):
        matris[i][j] = numbers[p]
        p+= 1
        
    
for i in range(2): # satır
    for j in range(3): # sütun
        print(f"{matris[i][j]:4}", end = '')
    print("")
    
"""

c = 1
n,m = 3,5
matris  = []
for  i in range(n):
    temp = []
    for j in range(m):
        temp.append(c)
        c+=1
    matris.append(temp)
    
# print(matris)
    
row = [0 for i in range(n)]
    
# print(row)
    
matris = [row for i in range(m)]
    
# print(matris)
    
matris = [[i for i in range(n)] for i in range(m)]
    
# print(matris)
        
numbers = [10,20,30]


matris = [[0] * m]*n
matris[0 ][0] = 55

print(matris) 

l1 = [1,2,3]
l1.append(23)
l2 = l1
l2.append(55)

print(l1)

print()

print(l2)

print()

matris = []
for i in range(n):
    matris.append([i]*m)
print(matris)

print()

matris = [[i]*m for i in range(n)]

print(matris)
    
    
    
    
    
    
    
