print("/n")
choix = "o"
moyenne = 0
liste_note = []

while (choix == "o"):
    note = float(input("Saisissez une nouvelle note : "))
    moyenne += note
    liste_note.append(note)
    choix = input("Voulez-vous saisir une nouvelle note ? (o/n)")

    if (note != 0):
        moyenne1 = moyenne + note
        notes1 = liste_note.append(note)

print(f"La moyenne de la classe est {round(moyenne / len(liste_note), 2)}")
print(f"la moyenne optimisée de la classe:  {round(moyenne1 / len(notes1), 2)}")
