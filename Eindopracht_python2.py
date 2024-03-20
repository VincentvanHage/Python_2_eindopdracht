import os
from time import sleep

foutmelding = True
gehaald = False
detected = False
geraden1 = False
print("Leuk dat je galgje wil spelen!")
print()
lives = int(input("Hoeveel kansen om het woord te raden moeten er zijn?"))
# lives verandert, lives startgetal niet
lives_start = lives
  
secret = input("wat moet het woord worden?")
 # lengte van het woord   
secret_1 = len(secret)
sleep(1)
print("Oke, goede keuze")
os.system("clear")
print('Tijd om te raden Als je het woord denkt te weten klik dan "?" en als je wilt stoppen typ dan "SS"')
print ('Als je het woord denk te weten type dan: "?"')
print("Je hebt", lives, "kansen/levens")
print()
#checkt hoeveel letters er in het woord zitten
print("Het woord heeft", secret_1, "letters")
  
#geraden letters
gerletters =[]
  
#Spel
# detected word True als letter in woord zit
while not lives == 0 and not gehaald == True:
  detected = False
  letter = input ("geef een letter ")
  check = str.isalpha (letter)
  check2 = len (letter)
  #Als iemand woord raad
  if letter == "?":
    Poging  = input("Dus je denkt het woord te weten? Voer het woord maar in!")
    if Poging == secret:
      print()
      print("Goed zo je hebt het woord geraden! Hier is je informatie")
      print()
      print("je deed het in ",lives_start - lives ,"pogingen")
      print("Je had letters",gerletters,"geraden")
      gehaald = True
    else:
      print ("Jammerrrrrr volgende keer beter.")
       
  
  
  
  #stoppen
  if letter == "SS":
    print()
    print("Stopppppppppp kom terug!!!!!!")
    
  if geraden1 == True and not letter == "?":
    print()
    print()
    print("Gast stop je weet het woord al")
    print()
    print()
    
    #vraag het woord en checkt of het een string is.
  if check == False:
    if not gehaald == True:
      print(foutmelding)
  elif not check2 == 1:
    if not gehaald == True:
      print(foutmelding)
  elif letter in gerletters:
    if not gehaald == True:
      print("Die had je al geraden")
      print()
      print()
      print("Je hebt nog", lives, "kansen")
      print("je hebt de letters", gerletters, "al geraden")
    
    
    
  #Kijkt of letter in woord zit
    
  if not gehaald == True:
    for woord in range (0, secret_1, 1):
      secret_p = (secret[woord])
      if secret_p == letter:
        detected = True
    
    
    
        #als het letter er in zit
        #ger_check checkt geraden letters
        if not letter in gerletters:
          gerletters.append(letter)
          print("letter zit in woord")
          print()
          print()
          print("De al geraden letters zijn:", gerletters)
          ger_check = len(gerletters)
          if ger_check == secret_1:
            print("Je hebt alle letters, type:'?' om het woord te raden")
            geraden1 = True
    
    
    
    
      #Als letter er niet in zit
      if woord + 1 == secret_1:
        if detected == False:
          print("Die letter zit er niet in!")
          lives = lives -1
          print()
          print()
          print("je hebt nog", lives,"kansen")
          if lives == 0:
            print("Je hebt verloren")
            print("De letters die je geraden het zijn:",gerletters)
            print("Het woord was",secret)
              