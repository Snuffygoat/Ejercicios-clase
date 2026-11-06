total_space = float(input("cuanto espacio tiene el disco"))
disk_usage = float(input("Cuanto espacio ocupado"))

if total_space > disk_usage:
     print("Guardadndo el archivo")
elif total_space == disk_usage:
     print("no entra el archivo")
else:
     print("ERROR¡¡¡")