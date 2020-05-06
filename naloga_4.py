import sys

vnos = float(input("Vnesi število, katerega kvadrat želiš izračunati: "))
kvadrat = vnos*vnos

while vnos > 0:
    print("\nKvadrat števila je " + str(round(kvadrat,2)) + ".")
    break
else:
    sys.exit()