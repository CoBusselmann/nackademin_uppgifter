class buss:
    def __init__(self):
        self.passenger = []  # Här lagras alla passagerares ålder i en lista.
# Lägger till en passagerare i bussen


def add_passenger(buss):
    while True:
        try:
            age = int(input("Ange passagerarens ålder: "))
            buss.passenger.append(age)
            print("Passagerare lades till")
            return
        except ValueError:
            print("Du måste skriva ett heltal, försök igen. ")
# Tar bort passagerare från bussen baserat på vilket plats dem sitter på


def remove_passenger(buss):
    while True:
        try:
            spot = int(
                input(f"Vilken Passagerare vill du ta bort? 1-{len(buss.passenger)}: "))
            if not buss.passenger:
                print("Bussen är tom")
                return
            if 1 <= spot <= len(buss.passenger):
                remove = buss.passenger.pop(spot - 1)
                print(f"Passagrerare {remove} har tagits bort")
                return
            else:
                print("Platsen finns inte")
                return
        except ValueError:
            print("Du måste ange ett heltal, försök igen.")

# Vissar en lista på alla passagerare på bussen, startar från 1.


def show_passenger(buss):
    if not buss.passenger:
        print("Bussen är tom")
        return
    for i, age in enumerate(buss.passenger, start=1):
        print(f"{i}: {age} år.")

# Räknar ut meddelåldern på passagerarna.


def avrage_age(buss):
    if not buss.passenger:
        print("Bussen är tom")
        return
    avg_age = sum(buss.passenger) / len(buss.passenger)
    print(f"Medelåldern är {round(avg_age)} år")

# Hittar passageraren som är äldst, skriver ut åldern samt platsen passageraren sitter på.


def max_age(buss):
    if not buss.passenger:
        print("Bussen är tom")
        return
    max_age = max(buss.passenger)
    spot = buss.passenger.index(max_age) + 1
    print(f"Den äldsta på bussen är {max_age} år och sitter på plats {spot}")

# Hittar passagerare om man söker på åldern.


def find_passenger(buss):
    while True:
        try:
            if not buss.passenger:
                print("Bussen är tom")
                return
            search = int(input("Ange ålder på passageraren du söker: "))
            if search in buss.passenger:
                spot = buss.passenger.index(search) + 1
                print(
                    f"Passageraren med åldern {search} finns på plats {spot}.")
                return
            else:
                print(
                    f"Passageraren med åldern {search} finns inte på bussen.")
                return
        except ValueError:
            print("Du måste ange ett heltal, försök igen.")

# Sorterar bussen på ålder, yngst till äldst


def sort_buss(buss):
    if not buss.passenger:
        print("Bussen är tom")
        return
    buss.passenger.sort()
    print("Passagerarna har sorterats efter ålder.")
    show_passenger(buss)


def meny():  # Skapat en meny som kallar på respektive funktioner vid val i menyn man gör.
    while True:
        print("\n----------MENY----------")
        print("1. Lägg till passagerare")
        print("2. Ta bort passagerare")
        print("3. Visa alla passagerare")
        print("4. Beräkna medelålder på passagerarna")
        print("5. Hitta äldsta passageraren")
        print("6. Sök efter passagerare")
        print("7. Sortera passagerare efter ålder")
        print("8. Avsluta")
        val = input("Välj ett alternativ: ")
        if val == "1":
            add_passenger(my_buss)
        elif val == "2":
            remove_passenger(my_buss)
        elif val == "3":
            show_passenger(my_buss)
        elif val == "4":
            avrage_age(my_buss)
        elif val == "5":
            max_age(my_buss)
        elif val == "6":
            find_passenger(my_buss)
        elif val == "7":
            sort_buss(my_buss)
        elif val == "8":
            print("Tack för buss resan, avslutar programmet.")
            break
        else:
            print("Fel: Du måste skriva ett heltal mellan 1-8, försök igen  ")
            # om användaren inte använder ett heltal så ska den fortsätta loopen.
            continue


my_buss = buss()  # Buss objekt som används av alla fuktioner.
meny()  # används för att anropa menyn när programmet startar.
