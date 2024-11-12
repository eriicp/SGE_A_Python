nota = 6.25

if nota < 5:
    resultat = "L’alumne ha suspès."
elif 5 <= nota < 6.6:
    resultat = "L’alumne ha aprovat."
elif 6.6 <= nota < 8:
    resultat = "L’alumne ha tret un notable."
elif nota > 8:
    resultat = "L’alumne ha tret un excel·lent."

print(resultat)