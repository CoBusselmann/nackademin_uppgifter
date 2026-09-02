"""
ord = input("Skriv din meniing här: ")
print(f"Ditt ord har {len(ord)} antal bokstäver.")
print(f"Första bokstaven är {ord[0]} och sista bokstaven är {ord[-1]} i ordet {ord}. Hej \N{SNOWMAN}")
"""
"""
import datetime
now = datetime.datetime.now()
print(now)

dag = input("Vilken dag: ")

match(dag):
    case"Måndag":
        print("Det är Måndag ")
    case"Tisdag":
        print("Det är Tisdag")
        """
"""
a = input("Skriv in ett amerikanskt datum MM/DD/ÅÅ: ")
månad = a[:2]
dag = a[2:4]
år = a[4:]
s = "20"+ år + "-" + månad +"-" + dag
print(f"{s}")
"""
"""
mening = input("Skriv din mening här:")
m = 0
for c in mening:
    if c == " " or c == "\t":
        break
    m = m + 1
if m < len(mening):
    print(f"Först vita är på {m} ")
else:
    print("Inget vitt tecken")
    """ 

print("Välkommen till mitt spel!")
list = []
svar = ["2", "1", "2"]
fråga1 = input( "Hur gammal är Oliver?\n1. 23 år\nX. 21år\n2. 25 år\n>")
list.append(fråga1)
fråga2 = input("Var bor Oliver?\n1. Hjorthagen\nX. Lidingö\n2. Sydamerika\n>")
list.append(fråga2)
fråga3 = input("Vad heter Olivers mamma?\n1. Carin\nX. Helena\n2. Karin\n>")
list.append(fråga3)
print(f"Rätta svar: {svar}")
print(f"Dina svar:  {list}")


