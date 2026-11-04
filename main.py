namn = input("Vad heter du? ")
print("Hej " + namn + " och välkommen till spelet!")
import random as rand
while True:
    giss = 0
    check = 0
    try:
        giss = int(input("Gissa ett tal mellan 1 och 10: "))
    except ValueError:
        print("Gissa ett nummer!")
        check += 1
    if check == 0:
        if giss == rand.randint(1, 11):
            print("Det var rätt!")
            break
        elif giss < 1 or giss > 10:
            print("Mellan 1 och 10 tack!")
        else:
            print("Tyvärr, det var fel!")
