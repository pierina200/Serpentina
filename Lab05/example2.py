try:
    entrada=input("ingrese el nombre del archivo:")
    archivo=open(entrada,"r",enconding="UTF-8")
    for linea in archivo:
        print(linea.upper())
except: 
    print("Error,no existe el archivo")