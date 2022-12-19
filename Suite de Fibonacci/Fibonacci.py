import os
def SuiteFibo(n,memo):
	if n==0 or n==1:
	  memo[n]=n
	if n not in memo:
	  memo[n]= SuiteFibo(n-1,memo) + SuiteFibo (n-2,memo)
	return memo[n]
print("notre programme calcule la suite de fibonacci")
# methode de mémo°isation

if __name__ == "__main__":
	memo=[0]*150
	n=input("entrer le nombre pour le quel vous voulez calculer la suite de Fibo ")
	n=int(n)
	while n<0 or n>151:
		n=input("entrer une valeur comprise entre 0 et 151 ")
		n=int(n)
	print("la suite de Fibonacci au rang",n,"est",SuiteFibo(n,memo))
	os.system("pause")
 	