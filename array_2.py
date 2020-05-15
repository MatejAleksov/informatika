# Vnesemo "tabelo"
array = [18, 16, 9, 18, 31, 30, 16, 15]
# Določimo kaj naj program pregleduje
for num in array:
    # Če je ostanek pri deljenju s 3 enak 0 se izvede sledeči del
    if num % 3 == 0:
        # Program izpiše števila, ki so deljiva s 3.
        print(num)