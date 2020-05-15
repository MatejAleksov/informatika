# Vnesemo "tabelo"
array = [-6, 10, 7, -11, 0, 3, 10, -5]
# Določimo novo spremenljivko, ki bo v novo tabelo z imenom list sprejemala števila
list = list()
# Določimo kaj naj program pregleduje
for num in array:
    # Če je številka manjša kot 0 se izvede sledeči del
    if num < 0:
        # Če je številka manjša od 0 ji nastavimo vrednost 0
        num = 0
        # Številka 0 se doda v "tabelo" list
        list.append(num)
    # Če je številka večja kot 0 se izvede sledeči del
    else:
        # Če je številka večja kot 0 vrednost ostane enaka
        num = num
        # Številka se doda v "tabelo" list
        list.append(num)
# "Tabela" list z novimo vrednostmi številk se izpiše
print(list)
