price_per_minut = float(input("Vad är kostnaden per minut? "))
speaking_time_minut = float(input("Ange hur många minter du har pratat i telefon senaste månaden: "))
cost_per_month = speaking_time_minut * price_per_minut

if cost_per_month < 300:
    print(f"Du har pratat i telefon för {cost_per_month} kr denna månad.")
else:
    cost_per_month = cost_per_month * 0.9
    print(f"Du har pratat för mer än 300kr vilket betyder att du får 10% rabatt och totalkostnaden blir {cost_per_month}kr")    
    