conutries = {'col','mex','bol','usa','arg','col'}

# Tamaño de un conjunto 
size = len(conutries)
print(size)

# Si tiene un elemento especifico dentro del conjunto
print('col' in conutries)  # Devuelve True
print('bra' in conutries)  # Devuelve False

# Agregemos el elemento: add
conutries.add('bra')
print(conutries)
print('bra' in conutries)  # Devuelve True

# Update / actualizar conjunto  Se pueden agregar conjuntos al set
conutries.update({'ecu','chi'})    #Importante poner los corchetes
print(conutries)

# Remove / Eliminar elementos del conjunto
conutries.remove('col')
conutries.remove('arg')

# Se puede descartar el elemnto sin causar errores
conutries.discard('ar')
print(conutries)

# Limpiar el conjunto 
conutries.clear()
print(conutries)
