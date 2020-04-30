hosts = open(r"C:\Users\cesar.z\text1.txt")
contenido = hosts.read()

print(contenido)

print("probando")

hosts.close()

####################################

with open(r"C:\Users\cesar.z\text2.txt", "a") as the_file:  ### se cierra automaticamente 
    the_file.write("some text to the file \nand more text")
with open(r"C:\Users\cesar.z\text2.txt", "r") as the_file:
    for x in the_file:
        print(x.rstrip())
