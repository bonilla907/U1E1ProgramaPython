frase_original = 'Hola Mundo Desde Python'
frase_original = frase_original.split()

direccion = open('C:/Users/oscar/Desktop/prueba.txt', 'r')
oracion = direccion.read()

print("La frase del txt es: "+oracion)
print("\n\nOrdenamiento: ")

oracion = oracion.split()
direccion.close()
numero_cadenas = len(frase_original)


aux = [None]*numero_cadenas
corregida = ""

for i in range(0, len(oracion)):
    for j in range(0, len(oracion)):
        if (oracion[i]) == (frase_original[j]):
            aux[j] = oracion[i]

for i in range(0, len(aux)):
    corregida += aux[i]+" "
    print(corregida)
