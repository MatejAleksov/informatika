# V program naložimo modul sys
import sys
# Vnesemo "tabelo"
array = [ -6, 10, 7, -11, 0]
# Določimo kaj naj program pregleduje
for num in array:
    # Če je številka v tabeli manjša od 0 se izvede ta del
    if num < 0:
        # Index številke določimo s fuknicjo index()
        index = array.index(num)
    # Če je številka večja kot 0 se izvede sledeči del
    else:
        #Izpiše se -1 in program se zaustavi
        print(-1)
        sys.exit()
# Program izpiše index zadnjega negativnega števila
print(index)