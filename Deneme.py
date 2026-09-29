"""
print("Rus elçisi Kırım'da hak iddia ediyor.")

print("Ne emredersiniz?")


karar = input("1: Savaş ilan et. 2: Göz yum. 3: Suikast düzenle." )

if karar == "1":
    print("Elçiye kılıçların çekildiğini söylediniz")
    
elif karar == "2":
    print("Kırım Ruslar tarafından ilhak edildi")

elif karar == "3":
    print("Büyük Petro haşhaşilerimiz tarafından katledildi")

else:
    print("Kararsızlığınız bize kötü tezahür edecek hünkarım!")
    

import random



kale_savunmasi = 100

while kale_savunmasi > 0:
    karar = input("1: Top atışı [-20 hasar], 2:Humbaracı gönder [40 Hasar]")
    if karar == "1":
        kale_savunmasi -= 20
        print("Yıkıma kalan can:", kale_savunmasi)
    elif karar == "2":
        zar = random.randint(1, 100) 
        
        if zar > 50:    
            kale_savunmasi -= 40
            print("Humbaracılar kaleye ulaştı! Kalan can:", kale_savunmasi)
        else:
            print("Askerler vuruldu")
        
            print("Humbaracılar kaleye ulaşamadan vuruldu")
            print("Yıkıma kalan can:",kale_savunmasi)
    else:
        print("Hasar veremediniz")
        
        
        
print("Surlar gümbürdedi")

"""
# x = 40


# mat_net1 = (x - mat_dogru) / 4

# mat_net2 = mat_dogru - mat_net1

# print(mat_net2)

# print(x - mat_net)


# turkce_dogru = int(input("Türkçe doğru sayısını girin: "))

# turkce_net = (x - turkce_dogru) / 4

# print(x- turkce_dogru)


mat_dogru = int(input("Matematik doğru sayısını girin: "))


mat_yanlis = int(input("Matematik yanlış sayısını girin: "))
 
mat_net = mat_dogru - (mat_yanlis / 4) 


print (f' matematik netin: {mat_net}')
    
turkce_dogru = int(input("Türkçe doğru sayısını girin: "))

turkce_yanlis = int(input("Türrkçe yanlış sayısını girin: " ))

turkce_net = turkce_dogru - (turkce_yanlis / 4) 

print(f'Türkçe netin: {turkce_net}')

sos_dogru = int(input("Sosyal doğru sayısını girin : "))

sos_yanlis = int(input("Sosyal yanlış sayısını girin : "))

sos_net = sos_dogru - (sos_yanlis / 4)

print(sos_net)

fen_dogru = int(input("Fen doğru sayısını girin: "))

fen_yanlis = int(input("Fen yanlış sayısını girin : " ))

fen_net = fen_dogru - (fen_yanlis / 4)

print(fen_net)


top_net = mat_net + turkce_net +  fen_net + sos_net


print(top_net)
    
if top_net > 60:
    print("an excellent result")
else:
    print("pc programmer has been slayed")


