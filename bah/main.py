import pywhatkit as Oli
try:
    Oli.sendwhatmsg_to_group_instantly("Loading Programmers;","Hello jeunes programmeurs",15,True,3)

    print("message envoyé avec succes")

except:
    print("le message n a pas ete envoyé")