import random 

secenekler = ["tas", "kagit", "makas"]
secim = input("taş mı, kagit mı, makas mı?\n")
bilgisayar = random.choice(secenekler)

print("Bilgisayarın seçimi:", bilgisayar)

if secim == bilgisayar:
    print("Berabere!")
elif (secim == "tas" and bilgisayar == "makas") or (secim == "kagit" and bilgisayar == "tas" ) or (secim =="makas" and bilgisayar == "kagit"):
    print("Tebrikler, kazandiniz!")
else: 
    print("Bilgisayar kazandı.")

      

      
   