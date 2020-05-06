# Naložimo sys modul
import sys

# Program uporabnika pozdravi
print("Pozdravljen!"
      "\nPred teboj se nahaja program za izračun ploščine."
      "\nČe vpisuješ decimalna števila jih vpisuj s piko(.) in ne z vejico(,), npr. 13.2 in ne 13,2.")

# Program uporabniku ponudi možnosti med katerimi lahko izbira
while True:
    print("\nČe želiš izračunati ploščina kvadrata izberi 1."
          "\nČe želiš iračunati ploščino pravokotnika izberi 2."
          "\nČe želiš izračunati ploščino pravokotnega trikotnika izberi 3."
          "\nZa izhod iz programa izberi 4.")

    # Uporabnik vnese kaj želi narediti
    izbira = int(input("\nIzberi kaj želiš izračunati! "))

# Če uporabnik izbere 1, t.j. ploščina kvadrata se izvede ta del
    if izbira == 1:
        # Program uporabnika vpraša po vnosu dolžine stranice a
        a = float(input("\nVnesi dolžino stranice a: "))
        ploscina = a*a
        # Program izpiše ploščino kvadrata.
        print("Ploščina kvadrata je " + str(ploscina) + " cm2.")
        break

    # Če uporabnik izbere 2, t.j. ploščina pravokotnika se izvede ta del.
    elif izbira == 2:
        # Program uporabnika vpraša po vnosu dolžine stranice a in b
        a = float(input("\nVnesi dolžino stranice a: "))
        b = float(input("Vnesi dolžino stranice b: "))
        ploscina = a*b
        # Program izpiše ploščino pravokotnika
        print("Ploščina pravokotnika je " + str(ploscina) + " cm2.")
        break

    # Če uporabnik izbere 3, t.j. ploščina pravokotnega trikotnika se izvede ta del.
    elif izbira == 3:
        # Program uporabnika vpraša po vnosu dolžine katet a in b
        a = float(input("\nVnesi dolžino katete a: "))
        b = float(input("Vnesi dolžino katete b: "))
        ploscina = (a*b)/2
        # Program izpiše ploščino pravokotnega trikotnika
        print("Ploščina pravokotnega trikotnika je " + str(ploscina) + " cm2.")
        break

    # Če uporabnik izbere 4. t.j. izhod se program zapre
    else:
        print("Adijo! (umirjeno)")
        sys.exit()


