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
"""

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