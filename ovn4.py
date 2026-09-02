#Uppgift 4.1
"""
print ("[", end="")
k=0
while k < 6:
    print(f"{k:2}", end="")
k = k + 2
print("]")
"""

print("---Har Emilie halsfluss eller inte---")

while True:
    ont_i_halsen = input("Har du ont i halsen? (Ja/Nej): ")
    vita_prickar = input("Har du vita prickar på mandlarna? (Ja/Nej): ")
    feber = input("Har du feber? (Ja/Nej):  ")
    if ont_i_halsen == "ja" and vita_prickar == "ja":
        print("Du har med störst sannolikhet Halsfluss. ")  
    elif ont_i_halsen == "ja" and vita_prickar == "nej" and feber == "ja":
        print("Med störst sannolikhet förkyllning. ")
    elif ont_i_halsen == "nej" and vita_prickar == "ja":
        print("Med störst sannolikhet halsfluss, men kan vara annat. ")
    else:
        print("Du är frisk, vad skönt!!")
        break

        
