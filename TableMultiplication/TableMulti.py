import os
def TableMulti(valeur,max):
  i=0
  while i <= max:
     print(valeur,"*",i,"=",valeur*i)
     i+=1

if __name__ == "__main__":
    TableMulti(3,10)
    os.system("pause")