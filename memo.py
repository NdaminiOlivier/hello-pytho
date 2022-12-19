# Importing the pywhatkit library and then using the sendwhatmsg function to send a message to a phone
# number.
import pywhatkit as Olii
i = 1
with open("NumeroDB.txt") as Num:
    Numero = Num.readline()
    while Numero != "" and i < 4:
        Olii.sendwhatmsg_instantly(Numero,"Bonsoir, nous avons une visioconférence en ligne ce soir",10,True,3)
        print(i, "messages envoyés")
        i+=1
        Numero = Num.readline()

Num.close()




   #try:
    #    Olii.sendwhatmsg_instantly("+237695249996"," *Euhhhh, j adore memo* \n",10,True,3)
     #   Olii.sendwhatmsg_instantly("+237655666473", " *Euhhhh, adorez vous également mémo ?* \n", 10, True, 3)
      #  print("message envoyé avec succes")

    #except:
     #   print("le message n'a pas été envoyé")'''
