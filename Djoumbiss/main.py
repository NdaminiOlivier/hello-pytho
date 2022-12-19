import os

def SuiteNumérique(n):
    if n == 0:
        return 0
    else:
        r = input ("veuillez entrer la valeur de la raison de votre suite arithmétique\n ")
        r = int(r)
        for i in range (n+1):
            b = SuiteNumérique(0) + i*r
        return b

if __name__ == "__main__":
   print("la suite numérique au rang 5 est",SuiteNumérique(5))

os.system("pause")