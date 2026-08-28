current_meter = int(input("Ange nuvarande mätarställning: "))
meters_1_year_ago = int(input("Ange mätarställning för ett år sedan: "))
liter_tankat = int(input("Ange liter bensin tankat på ett år: "))

korstracka = (current_meter - meters_1_year_ago)
forbrukning = (liter_tankat / korstracka) 
print(f"Antal körda mil {korstracka}")
print(f" Din bil drar ca {forbrukning:.2f} liter per mil")
