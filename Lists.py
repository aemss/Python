'''
sayilar = [10,3,8,23,99]

sayilar.insert(1,44)
# print(sayilar)

cikarilan_eleman = sayilar.pop()

# print(cikarilan_eleman)

# print(sayilar)

sayilar.pop(0)

# print(sayilar)

sayilar.reverse()

# len(sayilar)

sayilar = sorted(sayilar)
print(sayilar)

isimler = ["Ahmet","Mehmet","Ali","Berke"]

for isim in isimler :
    print(isim)

for i in range(len(isimler)):
    print(f"{i}. Eleman: {isimler[i].title()}")

print("\n===Tersten İsimler===\n")
for i in range(len(isimler)-1,-1,-1):
    print(f"{i}. Eleman {isimler[i]}")

print("\n===Düzden İsimler===\n")
i = 0

while i < len(isimler):
    print(f"{i}. İsim: {isimler[i].title()}")
    i += 1
print("\n===Tersten İsimler===\n")

i = len(isimler)-1
while i >=0:
    print(f"{i}. İsim: {isimler[i].title()}")
    i -= 1

print()
for index, isim in enumerate(isimler):
    print(f"{index}. isim: {isim.title()} ")

print()
for index,isim in enumerate(reversed(isimler)):
    print(f"{index}. isim: {isim.title()} ")


numbers = list(range(10))

# dizi[start:stop:step]
 
print(numbers[::3])

sayilar = []

for i in range(5):
    s = int(input("Bir sayi giriniz:"))
    sayilar.append(s)
    
    
toplam = 0
for sayi in sayilar:
    toplam += sayi
    
ortalama = toplam / len(sayilar)

print(ortalama)
'''

sayilar = [12,5,9,27,14]

buyuk = sayilar[0]

for s in sayilar:
    if s > buyuk:
        buyuk = s
    else:
        buyuk = buyuk


print("En büyük sayi : ",buyuk)






















