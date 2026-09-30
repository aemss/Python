"""
n = int(input("Pozitif Tam Sayı Giriniz: "))

if n < 0: 
    print("Negatif sayıların faktöriyeli yoktur.")
else:
    faktoriyel = 1
    for i in range(1, n+1):
        faktoriyel *= i
    print(f"{n}! = {faktoriyel}")


while True:
    try:
        n = int(input("Pozitif Tam Sayı Giriniz: "))
        if n>0:
            break
        else:
            print("lütfen pozitif bir tam sayı giriniz.")
    except ValueError:
        print("Hata: Lütfen bir tam sayı giriniz.")


toplam = 0
for i in range(1, n+1):
    toplam += i

print(f"1'den {n}'e kadar olan sayıların toplamı: {toplam}")


import random
deneme_sayisi = 0

gizli_sayi  = random.randint(1, 100)

while True:
            tahmin = int(input("1 ile 100 arasında bir sayı tahmin edin: "))
            deneme_sayisi += 1
            if tahmin > 100 or tahmin <1:
                print("Lütfen 1 ile 100 arasında bir sayı giriniz.")

            elif tahmin < gizli_sayi:
                print("Daha büyük bir sayı tahmin edin.")
            elif tahmin >gizli_sayi:
                print("Daha küçük bir sayı tahmin edin.")
            elif tahmin == gizli_sayi:
                print(f"Tebrikler! {deneme_sayisi} denemede doğru tahmin ettiniz.")
                break


for i in range(1,11):
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
    print()


toplam = 0

print("Sayi giriniz. ")

while True:
    sayi = int(input("Sayı: "))
    if sayi == 0:
        break

    elif sayi > 0:
            toplam += sayi
    else:
        print("Negatif sayı yok sayıldı.")

print(f"Girilen pozitif sayıların toplamı: {toplam}")
"""
####
"""

print("Kaç terimlik fibonacci dizisi oluşturulsun?")

n = int(input())
if n <= 0:
    print("Hata: Lütfen pozitif bir tam sayı giriniz: ")
else:
    print("Fibonacci dizisi yazdır: ")
    if n == 1:
        print("0")
    elif n == 2:
        print("0 1")
    else:
        a, b = 0, 1
        print("0 1", end=" ")
        for i in range(3, n+1):
            c = a + b
            print(c, end=" ")
            a, b = b, c
"""         
# Asal Sayılar

n = int(input("Sayi giriniz: "))

if n<= 1:
    print("Asal sayı yoktur.")
else:
    asal = True
    for i in range(2,n):
        if n % i == 0:
            asal = False
            break
    if asal:
        print(f"{n} bir asal sayıdır.")

    else:
        print(f"{n} bir asal sayı değildir.")


