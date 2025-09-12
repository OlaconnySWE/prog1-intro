import math
import random

igen = True
d_slump = random.randint(1,10)
försök = 0

print("Datorn kommer slumpa ett tal och du ska försöka gissa det")

while igen:
        


        a_slump = int(input("Skriv ett tal mellan 1-10 som du tror datorn kommer slumpa fram"))
        försök += 1
        
        if a_slump > d_slump :
            print("Du gissade lite för högt")

        if d_slump > a_slump :
            print("Du gissade för lågt")

        if a_slump == d_slump :
          print("Du fick fram rätt svar")
          gissa_igen = input("Vill du spela igen? J/N:")
          if gissa_igen == "J":
            igen = True
            print(f"Du behövde:{försök} försök")
       
            break
       
       


       
        
  
