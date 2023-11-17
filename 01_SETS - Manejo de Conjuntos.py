# SETS:
# Se pueden modificar
# No tienen un orden
# No pueden tener elementos duplicados
conutries = {'col','mex','bol','usa','arg','col'}
print(conutries)
print(type(conutries))

numbers = {1,2,3,44,2,67,77,77,88,90}
print(numbers)
print(type(numbers))

types = {1,'hola',3,'Science', False, True, 'Almacena de todo'}
print(types)
print(type(types))

#b Crear un conjunto a travez de un String
set_string = set('Holal mi perro')
print(set_string)

# Crear conjunto a partir de una tupla
set_tuple = set(('abc',1,False,'b',2))
print(set_tuple)

# A partir de una Lista
numbers = [1,2,3,3,2,1,2,3,1]
set_numbers = set(numbers)
print(set_numbers)

unique_numbers = list(set_numbers)
print(unique_numbers)
