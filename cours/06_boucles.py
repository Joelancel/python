compteur = 0

while (compteur <= 1000):
    if (compteur % 2 == 0):
        print(compteur)
    compteur = compteur + 1
    
eleves = ["Thomas", "Lisa", "Helene", "Patrick", "Paul"]

i = 0
while (i < len(eleves)):
    print(eleves[i])
    i += 1
    
    
# choix = "o"
# liste_note = []
# moyenne = 0

# while (choix == "o"):
#     note = float(input("Saisissez une nouvelle note : "))
    
#     liste_note.append(note)
#     moyenne = moyenne + note
    
#     choix = input("Voulez-vous saisir une nouvelle note ? (o/n)")
    
# print(f"La moyenne de la classe est {moyenne / len(liste_note)}")

# For

eleves = ["Thomas", "Lisa", "Helene", "Patrick", "Paul"]

for eleve in eleves:
    print(eleve)
    
for car in "Coucou":
    print(car)
    
print("o" in "Python")
print("Thomas" in eleves)
print("Lise" in eleves)

# range()

nb_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
nb_list=list(range(0,100,1))
print(nb_list)


for (i) in range(0, 102, 2):
    print(i)

    for i in range(100, -1, -2):
        print(f"mouton n°{i}")

eleves = ["Thomas", "Lisa", "Helene", "Patrick", "Paul"]

for eleves in eleves:
   # eleves[i] = f"Eleve n°{i}: {eleves}"
    
    print(eleves[i])


eleves = ["Thomas", "Lisa", "Helene", "Patrick", "Paul"]
for (i, prenom) in enumerate(eleves):
   # eleves[i] = f"Eleve n°{i + 1}: {Value}"
   
    print(i)
    print(prenom)

    
    id_dbb = ["localhost", "root", "password"]
    print(id_dbb[-1])
    id_dbb=12345
