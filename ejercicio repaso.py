total_space = float(input("cuanto espacio tiene el disco"))
disk_usage = float(input("Cuanto espacio ocupado"))

def disk_space(total , disk):
     if total > disk:
          result("Guardadndo el archivo")
     elif total == disk:
          result("no entra el archivo")
     else:
          result("ERROR¡¡¡")
     return result

print(disk_space(total_space, disk_usage))
