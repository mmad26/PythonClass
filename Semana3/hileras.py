#Tema Hileras

message = input("Digite lo que quiera: ")

print(message)

#len() -> Encontrar la cantidad de caracteres en una hilera

print(len(message))

# Indices

print(message[0]) # Obtenemos el primer caracter de una hilera
print(message[len(message) -1]) # Obtenemos el ultimo caracter de una hilera

# Concatenacion de hileras

hilera = "Hilera inicial"

# Concatenacion simple

print(hilera + " otra hilera")
print(hilera)

# Concatenacion modificando la variable

hilera += ". Esto si modifica la variable hilera"
print(hilera)

# Inyectando texto

otra_hilera = "Hola {}! Como esta?".format("Maria")
print(otra_hilera)

print(otra_hilera[3:10])
print(otra_hilera[:10])
print(otra_hilera[8:])


