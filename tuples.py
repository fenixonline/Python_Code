"""
res_encuesta = (21, 'Venezuela', 'Ingeniero') # tupla
edad, pais, profesion = res_encuesta # se crean variables edad, pais, profesion con los datos de la tupla

print(edad, pais, profesion)

"""
###########################################################

airports = [('O’Hare Airport', 'ORD', 21), ('Los Angeles Airport', 'LAX', 22), ('Dallas/Fort Worth Airport', 'DFW', 23)]

opt=input("Selec the Airport to see the codes: A for O’Hare, B for LA C for Dallas:\n ")
if opt == "A":
    Airport, Code1, Code2, = airports[0]
    print("The codes are: \n", Code1,Code2)

if opt == "B":
    Airport, Code1, Code2, = airports[1]
    print("The codes are: \n", Code1,Code2)

if opt == "C":
    Airport, Code1, Code2, = airports[2]
    print("The codes are: \n", Code1,Code2)
