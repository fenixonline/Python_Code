"""def saludo(x):
    print("hola",x)
saludo("jose") """

list1 = ["UNO","DOS","TRES"]
list2 = ["CUATRO","CINCO"]

list1.extend(list2)

print(list1)

list1.insert(5,"SIX") ### posicion y valor

print(list1)

list3 = list1[0:2]

print(list3)


#################################


animals = ['perro','gato','lobo','raton']
try:
    busqueda = animals.index('camaron')
except:
    busqueda = 'Animal no encontrado'

print(busqueda)


for x in animals:
    print(x.upper())

animals = ['perro','gato','lobo','raton']
places = ['casa','campo','ciudad']

lista2 = animals + places

print(list2)
