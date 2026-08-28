#Uppgift 3.1

"""price_per_minut = 1.20
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

