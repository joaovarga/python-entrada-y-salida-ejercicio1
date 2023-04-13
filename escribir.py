# Creamos el archivo en modo escritura
archivoPrueba = open("prueba.txt", "w")

# Escribimos el contenido en el archivo

archivoPrueba.write("hola, este texto esta creado desde el archivo escribir.py")

# Cerramos el archivo
archivoPrueba

# Abrimos el archivo en modo lectura

archivoPrueba = open("prueba.txt", "r")
print (archivoPrueba.read())
