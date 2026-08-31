#Uppgift 3.1
"""
price_per_minut = 1.20
speaking_time_minut = float(input("Ange hur många minter du har pratat i telefon senaste månaden: "))
cost_per_month = speaking_time_minut * price_per_minut

if cost_per_month < 300:
    print(f"Du har pratat i telefon för {cost_per_month} kr denna månad.")
else:
    cost_per_month = cost_per_month * 0.9
    print(f"Du har pratat för mer än 300kr vilket betyder att du får 10% rabatt och totalkostnaden blir {cost_per_month}kr")
"""

#---------------------------------------------------------------------------------------------------------------
#Uppgift 3.2

"""
print("---Räkna ut ifall det gynnar dig att köpa årskort eller engångsbiljetter---")

gym_membership = int(input("Hur mycket kostar ett årskort? "))
gym_cost_day = int(input("Hur mycket kostar en biljett? "))
amount_training_per_week = int(input("Hur många gånger i veckan planerar du att träna? "))
amount_training_per_year = amount_training_per_week * 52 
cost_for_tickets_one_year = gym_cost_day * amount_training_per_year
if cost_for_tickets_one_year < gym_membership:
    print(f"Du kommer inte att träna för en kostnad av ett års kort, så köp engångsbiljetter istället.\n Din kostnad kommer att ligga på {cost_for_tickets_one_year}kr per år")
elif cost_for_tickets_one_year > gym_membership:
    print(f"Du kommer gynnas av ett årskort, du kommer spara pengar på det.\nKostnad {gym_membership}kr och kostnad för biljetter {cost_for_tickets_one_year}kr i ett år.")
"""
#-----------------------------------------------------------------------------------------------------------------

#Uppgift 3.3

"""
print("-----Kolla vilket betyd du fick på provet-----")
points = int(input("Hur många poäng fick du på provet? "))
if points > 50:
    print("Du har angivit fel antal poäng")
elif points >= 45:
    print("Du har fått A på provet, Grattis!")
elif points >= 40:
    print("Du fick B i betyg")
elif points >= 35:
    print("Du har betyg C")
elif points >= 30:
    print("Du har betyg D")
elif points >= 25: 
    print("Du har betyg E")
elif points >= 0:
    print("Du har betyd F tyvärr")
else:
    print("Det fanns inte så många poäng att få")
    """

#---------------------------------------------------------------------------------------------------------

#Uppgift 3.4

"""
temp = float(input("Vad är Temperaturen i ditt hem? "))
if temp < 18:
    print("Nu börjar det bli kallt.")
    print("Sätt på värmen.")
    if temp < 12:
        print("Ta på dig jackan")
else: 
    print("Det är varmt!")
    if temp >= 22:
        print("Sänk värmen!")
print(f"Temperaturen är {temp}")
"""

#-------------------------------------------------------------------------------------------------------------

#Uppgift 3.5

"""
max_length = 600
max_width = 200
max_thick = 100

min_length = 140
min_width = 90
min_thick = 90  

print("Skriv in Längd, Bredd och tjocklek på ditt paket.")
langd = int(input("Längd: "))
bredd = int(input("Bredd: "))
tjock = int(input("Tjocklek: "))

if (min_length <= langd <= max_length and
    min_width <= bredd <= max_width and
    min_thick <= tjock <= max_thick):
    print("Paketet PASSAR")
else:
    print("Paketet passar INTE.")
    """

