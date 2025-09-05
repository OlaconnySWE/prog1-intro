from random import randint

pl = input("Skriv ditt användarnamn: ") # här är en string där du skriver ditt namn
#här är "utamnarnas hp, det är en integer"
pl_life = 100
zo_life = 100

while pl_life > 0 and zo_life > 0:
  #här är spealeren skada som är random
    pl_life_hit = randint(1, 20) #integer
    zo_life -= pl_life_hit
    print(f"{pl} attackerar {pl_life_hit} skada! Zombiens liv är nu {zo_life}.") #string
 
    if zo_life <= 0:
        print(f"{pl} van matchen!!!")  #här är cokså en string
        break
#här är zombiens slag
    zo_life_hit = randint(1, 20) #integer
    pl_life -= zo_life_hit
    print(f"Zombien attackerar {pl} gör {zo_life_hit} skada! Ditt liv är nu {pl_life}.") #string

    if pl_life <= 0:
        print("Zombien vann matchen!") #string
        break