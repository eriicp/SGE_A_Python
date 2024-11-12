salari = 5000

if salari < 15000:
    iva = 0
elif salari < 30000:
    iva = 10
elif salari < 60000:
    iva = 21
else:
    iva = 21

import_iva = salari * iva / 100

print(f"Salari: {salari}€")
print(f"IVA aplicat: {iva}%")
print(f"Import IVA: {import_iva}€")