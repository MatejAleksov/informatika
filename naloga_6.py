#naložimo modul sys
import sys

# Program pozdravi uporabnika!
print("Pozdravljen!"
      "\nNahajaš se v programu, ki po tvoji izbiri sešteje ali odšteje dve števili."
      "\nČe vpisuješ decimalna števila jih vpisuj s piko(.) in ne z vejico(,), npr. 13.2 in ne 13,2.")

# Program od uporabnika zahteva vnos dveh števil
num1 = float(input("\nVnesi število 1: "))
num2 = float(input("Vnesi število 2: "))

while True:
    #Program uporabniku predstavi kaj lahko naredi
    print("\nZa seštevanje vnesenih števil izberi 1."
          "\nZa odštevanje vnesenih števil izberi 2.")

    # Uporabnik se odloči kaj želi storiti
    izbira = int(input("Kaj želiš izračunati? "))

    # Če uporabnik izbere 1 se izvede ta del
    if izbira == 1:
        sum = num1 + num2
        print("\nSeštevek " + str(num1) + " in " + str(num2) + " je " + str(sum) + ".")
        break

    # Če uporabnik izbere 2 se izvede ta del
    elif izbira == 2:
        razlika = num1 - num2
        print("\nRazlika " + str(num1) + " in " + str(num2) + " je " + str(razlika) + ".")
        break

    # Če uporabnik izbere karkoli drugega kot 1 ali 2, ga program opozori!
    else:
        print("\nDovoljena izbira je 1 za seštevanje in 2 za odštevanje. Zaženi program ponovno in poiskusi znova")
        sys.exit()