#Uppgift 4.1
"""
print ("[", end="")
k=0
while k < 6:
    print(f"{k:2}", end="")
k = k + 2
print("]")
"""
#-----------------------------------------------------------------------------------------------------------------
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
"""

#-------------------------------------------------------------------------------------------------------------

#Uppgift 4.2 
"""
tal = int(input("Skriv ett tal: "))

summa = 0

for i in range(1, tal + 1):
    summa += i**2

print(f"Summan är: {summa}")
"""

#----------------------------------------------------------------------------------------------------------

#Uppgift 4.4 och 4.5

"""
hight_droped = float(input("Hur högt upp droppar du bollen(meter): "))

while True:
    end = 0.01
    antal_studs = 0 
    while True:
        if hight_droped > end:
            hight_droped  = hight_droped * 0.7
            antal_studs += 1 
        elif hight_droped <= 0.01:
            print(f"Bollen studsade {antal_studs} gånger. ")
            break
    hight_droped = float(input("Hur högt upp droppar du bollen(meter): "))
    if hight_droped < 0:
        break
    print("Programmet avslutas")
"""

storsta = 0
minsta = 1.e300 # ett stort tal
while True:
    tal = float(input('> '))
    if tal < 0:
        break
    if tal > storsta:
        storsta = tal
        if tal < minsta:
            minsta = tal
    print(f'Största talet: {storsta}')
    print(f'Minsta talet: {minsta}')
