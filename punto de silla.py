import random

m = [
	[2, 35, 64, 67, 100],
	[54, 21, 5, 25, 70],
	[3, 79, 82, 93, 29],
	[32, 0, 91, 23, 42],
	[51, 92, 38, 27, 7]	
]

#Itera comparando los valores maximos en sus columnas
def ComparaMaxColumna(numero, matriz, root):

	indice = matriz.index(numero)
	nivel=0
	col=[]
	
	while nivel <= len(root)-1:
		col.append(root[nivel][indice])
		if len(col) == len(root) and numero != max(col):
			print("numero: %d" % numero + " es el punto de silla en el indice %d" % matriz.index(numero))
		else:
			nivel+=1

#Itera la matriz raiz buscando los valores maximos en su filas
for i in m:
	for j in i:
		if j == max(i):
			ComparaMaxColumna(j, i, m)



			

