import random

n = 3
m = 3

matris = []
for i in range(n):
    satir_listesi =  []
    for j in range(m):
        satir_listesi.append(random.randint(0,10))
    matris.append(satir_listesi)
    
# print(matris)

for satir in range(len(matris)):
    for sutun in range(len(matris[0])):
          print(f"{matris[satir][sutun]:4d}", end= '')
    # print("")
    
for satir in range(len(matris)):
    for sutun in range(len(matris[0])):
        print(f"{matris[satir][sutun]}")
        
# transpoz

transpoze = []

# matris[0] = kolon bilgisi
# matris = satır bilgisi

for j in range(len(matris[0])):  
    yeni_satir = []
    for i in range(len(matris)):
         yeni_satir.append(matris[i][j])
    transpoze.append(yeni_satir)
    
for i in range(len(transpoze)):
    for j in range(len(transpoze[0])):
          print(f"{transpoze[i][j]:4d}", end= '')
    print("")
    
    
    

        