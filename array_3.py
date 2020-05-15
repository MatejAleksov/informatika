# Vnesemo "tabelo"
array = [-6, 10, 7, -11, 0, 3, 10, -5]
# Določimo števec in mu damo vrednost 0
amount = 0
# Določimo kaj naj program pregleduje
for num in array:
    # Če je število manjše od 0 se izvede sledeči del.
    if num < 0:
        # Števec se poveča za 1.
        amount = amount + 1
# Izpišemo števec
print(amount)