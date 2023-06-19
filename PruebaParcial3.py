#productos: id, nombre, categoria, nivel, pack, stock, precio

#nivel(Profesional,Standar,Amateur)
#categoria(Armas, Municiones, Interno, Proteccion, Accesorio, Insumos)
#pack(Unidad, Pack)

#usuario es quien vende

#python -m pip install colorama
#pip install pylance

from colorama import Fore, init
init(autoreset= True)
#print(Fore.CYAN) 
import os
from datetime import datetime
import numpy as np

productos = ["001","Réplica Airsoft PDW 5.56 SBR","Arma","Profesional","Unidad",50,200000,
             "002","Replica ROSSI SENTINEL 9' DELTA","Armas","Standar","Unidad",45,105000,
             "003","Goma de Hop Up Improved","Interno","Profesional","Unidad",60,6000,
             "004","Batería Victory Battery LIPO 7,4V","Insumos","Profesional","Unidad",25,160000,
             "005","CO2 Umarex 12 grs.","Insumos","Standar","Pack",50,1000,
             "006","Cargador Mid-Cap","Insumos","Standar","Unidad",47,30000,
             "007","Replica SRC SR4 A1 CARBINE","Armas","Amateur","Unidad",38,75000,
             "008","Replica ROSSI SENTINEL 5.5' OMEGA","Armas","Profesional","Unidad",41,160000,
             "009","Pistón de policarbonato","Interno","Standar","Unidad",25,15000,
             "010","Motor de torque MPI 22T - Eje largo x2","Interno","Amateur","Pack",30,100000,
             "011","EMERSON Casco FAST MH","Proteccion","Profesional","Unidad",57,50000,
             "012","Mira Walther EPS 3","Accesorio","Profesional","Unidad",26,250000,
             "013","Replica Licenciada GLOCK 22","Armas","Profesional","Unidad",19,100000,
             "014","Replica Berreta M9A3","Armas","Standar","Unidad",40,99000,
             "015","EMERSON Chaleco CP Style Adaptive Vest","Proteccion","Standar","Unidad",52,130000,
             "016","Wiley X Chile Saber Advance x3","Proteccion","Profesional","Pack",40,90000,
             "017","ACM Chaleco Tactico Porta Placa","Proteccion","Amateur","Unidad",30,30000,
             "018","Replica HK 416 A5","Armas","Profesional","Unidad",28,115000,
             "019","Replica SRC SR5-PDW","Armas","Standar","Unidad",42,250000,
             "020","Mira Umarex RDS 6","Accesorio","Amateur","Unidad",33,90000,
             "021","Emerson Grip Bipode x2","Accesorio","Profesional","Pack",60,30000,
             "022","BALINES Rossi 6mm 0,25","Municiones","Standar","Unidad",105,7000,
             "023","Balines Oberland 0,12 x3","Municiones","Amateur","Pack",229,15000,
             "024","Balines King Arms 0,20 gr","Municiones","Profesional","Unidad",147,10000,
             "025","Mira Red Dot M2","Accesorio","Standar","Unidad",21,150000]
usuarios = ["1-1","Susana","Scorrea","123",
            "2-2","Juan","Jcastro","321",
            "3-3","David","Dcordova","567",
            "4-4","Maria","Msepulveda","741",
            "5-5","Andres","Aperez","951"]
#                  folio vendedor fecha id cant subtotal
boleta = np.array([[ 0,      "",   "",   "", 0,   0],
                   [ 0,      "",   "",   "", 0,   0],
                   [ 0,      "",   "",   "", 0,   0],
                   [ 0,      "",   "",   "", 0,   0],
                   [ 0,      "",   "",   "", 0,   0],
                   [ 0,      "",   "",   "", 0,   0],
                   [ 0,      "",   "",   "", 0,   0],
                   [ 0,      "",   "",   "", 0,   0],
                   [ 0,      "",   "",   "", 0,   0],
                   [ 0,      "",   "",   "", 0,   0]])
ventas = [100,"Dcordova","20-05-2023","001",1,200000,
          101,"Aperez","21-05-2023","017",2,60000,
          102,"Msepulveda","22-05-2023","018",3,345000,
          103,"Dcordova","23-05-2023","019",4,1000000,
          104,"Msepulveda","24-05-2023","020",5,4500000,
          105,"Aperez","25-05-2023","021",6,180000,
          106,"Dcordova","26-05-2023","022",7,49000,
          107,"Msepulveda","27-05-2023","023",8,120000,
          108,"Aperez","28-05-2023","024",9,90000,
          109,"Dcordova","29-05-2023","025",10,1500000,
          90,"Dcordova","01-02-2022","015",2,260000,
          91,"Scorrea","03-03-2022","016",2,180000,
          92,"Aperez","27-04-2022","018",1,115000,
          93,"Msepulveda","30-04-2022","006",2,60000,
          94,"Aperez","16-06-2022","021",3,90000,
          95,"Jcastro","28-06-2022","006",4,120000,
          96,"Msepulveda","15-10-2022","001",4,800000,
          97,"Scorrea","01-11-2022","005",2,2000,
          98,"Dcordova","12-11-2022","015",1,130000,
          99,"Scorrea","19-12-2022","016",5,450000,
          80,"Aperez","05-01-2021","016",10,900000,
          81,"Scorrea","16-02-2021","020",7,630000,
          82,"Dcordova","19-05-2021","025",6,900000,
          83,"Jcastro","21-05-2021","024",2,20000,
          84,"Aperez","17-07-2021","010",1,100000,
          85,"Scorrea","19-08-2021","011",1,50000,
          86,"Aperez","16-09-2021","009",2,30000,
          87,"Msepulveda","10-10-2021","019",3,750000,
          88,"Aperez","30-10-2021","016",7,630000,
          89,"Dcordova","--2021","018",5,575000]
#          id       fecha    valor
mermas = ["006","20-03-2021",30000,
          "005","15-09-2021",1000,
          "006","14-12-2021",30000,
          "020","16-03-2022",90000,
          "001","02-08-2022",200000,
          "023","10-10-2022",15000,
          "019","16-01-2023",250000,
          "016","22-02-2023",90000,
          "006","30-04-2023",30000,
          "008","10-06-2023",160000]
folio = 109
user = ""
password = ""
fecha = datetime.now().strftime("%d-%m-%Y")

os.system("cls")
print(Fore.GREEN+"BIENVENIDO AL PUNTO DE VENTA")
print(Fore.GREEN+"-"*30)
flag = True

#funciones
def login():
    while True:
        os.system("cls")
        cont = ""
        print(Fore.GREEN+"BIENVENIDO AL PUNTO DE VENTA")
        print(Fore.GREEN+"-"*30)
        user = input(Fore.GREEN+"Ingrese usuario: ")
        password = input(Fore.GREEN+"Ingrese contraseña: ")
        for n in range(len(usuarios)):
            if user == usuarios[n] and password == usuarios[n+1]:
                return user
        else:
            print(Fore.RED+"ERROR! Usuario o contraseña incorrecta")
        cont = input(Fore.GREEN+"Desea volver a intentarlo s/n: ")
        if cont == "n":
            return ""

def venta(ventas, productos, boleta,folio):
    folio += 1

    for i in range(10):
        id = input(Fore.CYAN+"Ingrese el ID del producto a comprar: ")

        i = 0
        sw = 0
        while i < len(productos):
            if productos[i] == id:
                sw = 1  # encontrado
                print(
                    productos[i],
                    " ",
                    productos[i + 1],
                    " ",
                    productos[i + 2],
                    " ",
                    productos[i + 3],
                )
                break
            i += 7

        if sw == 0:
            print(Fore.Red+"Error, el ID no existe")
            continue
        else:
            cantidad = int(input(Fore.CYAN+"Ingrese la cantidad que desea: "))
            subtotal = cantidad * productos[i + 6]

            for i in range(len(boleta)):
                if boleta[i][0] == 0:
                    boleta[i][0] = folio
                    boleta[i][1] = fecha
                    boleta[i][2] = id
                    boleta[i][3] = cantidad
                    boleta[i][4] = subtotal
                    break

            respuesta = input(Fore.CYAN+"¿Desea agregar otro producto? (s/n): ")

            if respuesta == "n":
                respuesta2 = input(Fore.CYAN+"¿Desea comprar los productos de la lista? (s/n): ")
                if respuesta2 == "s":
                    for i in range(len(boleta)):
                        if boleta[i][0] != 0:
                            ventas.append(boleta[i][:])

                    print(Fore.GREEN+"Venta realizada con exito")
                    return ventas
                else:
                    print(Fore.RED+"Ok, boleta anulada")
                    return ventas

    return ventas
    
def devolucion():
    os.system("cls")
    print(Fore.CYAN+"DEBOLUCIONES")
    print(Fore.CYAN+"-"*30)
    bol = int(input(Fore.CYAN+"Ingrese numero de folio: "))
    cont = 0
    op = 0; op2 = 0; op3 = 0
    borrar = []
    for i in range(len(ventas)):
        if ventas[i] == bol:
            boleta[cont][0]=ventas[i]
            boleta[cont][1]=ventas[i+1]
            boleta[cont][2]=ventas[i+2]
            boleta[cont][3]=ventas[i+3]
            boleta[cont][4]=ventas[i+4]
            boleta[cont][5]=ventas[i+5]
            cont += 1
            borrar.insert(0,i)
    for i in borrar:
        for n in range(6):
            ventas.pop(i)
    if cont == 0:
        print(Fore.RED+"No hay boletas con ese folio")
    
    print(f'''Devolver folio {bol}
          1) Percial
          2) Todo''')
    op = int(input(Fore.CYAN+"Ingrese opcion: "))
    if op == 1:#devolver parcial
        for n in range(4):#despues cambialo a 10 #toma el primer producto a devolver
            for r in range(len(productos)):#lo busca en los productos
                if boleta[n][3] == productos[r]:
                    os.system("cls")
                    print(Fore.CYAN+f'''Devoler {productos[r+1]}:
            1)si
            2)no''')
                    op2 = int(input(Fore.CYAN+"Ingrese una opcion: "))#si se devuelve o no
                    if op2 == 1:
                        print(Fore.CYAN+'''\nEs merma s/n
            1) si
            2) no''')#si es merma
                        op3 = int(input(Fore.CYAN+"Ingrese una opcion: "))
                        if op3 == 1:
                            mermas.extend([boleta[n][3],fecha,boleta[n][5]])
                        elif op3 == 2:
                            cantidad = int(boleta[n][4])
                            productos[r+5] = productos[r+5]+cantidad
                    elif op2 == 2:
                        ventas.extend([boleta[n][0],boleta[n][1],boleta[n][2],boleta[n][3],boleta[n][4],boleta[n][5]])
    elif op == 2:
        for n in range(4):#despues cambialo a 10
            for r in range(len(productos)):
                if boleta[n][3] == productos[r]:
                    print(Fore.CYAN+f'''Producto {productos[r+1]}, es merma:
            1) si
            2) no''')
                    op2 = int(input(Fore.CYAN+"Ingrese una opcion: "))
                    if op2 == 1:
                        mermas.extend([boleta[n][3],fecha,boleta[n][5]])
                    elif op2 == 2:
                        ventas.extend([boleta[n][0],boleta[n][1],boleta[n][2],boleta[n][3],boleta[n][4],boleta[n][5]])
    for l in range(4):#cambiar a 10
        boleta[l][0] = 0
        boleta[l][1] = ""
        boleta[l][2] = ""
        boleta[l][3] = ""
        boleta[l][4] = 0
        boleta[l][5] = 0
    print(Fore.CYAN+"\nFin de devoluciones")
    os.system("pause")
        
def mantenimiento(productos):
    opcion = 0
    while opcion != 5:
        os.system("cls")
        print(Fore.CYAN + "MANTENIMIENTO DE PRODUCTOS")
        print(Fore.CYAN + "-" * 30)
        print("1. Agregar un nuevo producto")
        print("2. Modificar el stock")
        print("3. Modificar el precio")
        print("4. Imprimir todos los productos")
        print("5. Volver al menú principal")
        opcion = int(input(Fore.CYAN + "Ingrese una opción: "))

        if opcion == "1":
            id = input(Fore.CYAN+"Ingrese el ID del nuevo producto: ")
            nombre = input(Fore.CYAN+"Ingrese el nombre del nuevo producto: ")
            categoria = input(Fore.CYAN+"Ingrese la categoría del nuevo producto: ")
            nivel = input(Fore.CYAN+"Ingrese el nivel del nuevo producto: ")
            pack = input(Fore.CYAN+"Ingrese el tipo de empaque del nuevo producto: ")
            stock = int(input(Fore.CYAN+"Ingrese el stock del nuevo producto: "))
            precio = float(input(Fore.CYAN+"Ingrese el precio del nuevo producto: "))
            productos.extend([id, nombre, categoria, nivel, pack, stock, precio])
            print(Fore.GREEN+"Producto agregado con éxito")

        elif opcion == "2":
            id = input(Fore.CYAN+"Ingrese el ID del producto a modificar el stock: ")
            sw = False
            for i in range(0, len(productos), 7):
                if productos[i] == id:
                    stock = int(input(Fore.CYAN+"Ingrese el nuevo stock del producto: "))
                    productos[i + 5] = stock
                    sw = True
                    print(Fore.GREEN+"Stock modificado con éxito")
                    break
            if not sw:
                print(Fore.RED+"Error, el ID del producto no existe")

        elif opcion == "3":
            id = input(Fore.CYAN+"Ingrese el ID del producto a modificar el precio: ")
            sw = False
            for i in range(0, len(productos), 7):
                if productos[i] == id:
                    precio = float(input(Fore.CYAN+"Ingrese el nuevo precio del producto: "))
                    productos[i + 6] = precio
                    sw = True
                    print(Fore.GREEN+"Precio modificado con éxito")
                    break
            if not sw:
                print(Fore.RED+"Error, el ID del producto no existe")

        elif opcion == "4":
            print(Fore.CYAN+"Lista de productos:")
            for i in range(0, len(productos), 7):
                print("ID:", productos[i], "Nombre:", productos[i + 1], "Categoría:", productos[i + 2], "Nivel:", productos[i + 3], "Pack:", productos[i + 4], "Stock:", productos[i + 5], "Precio:", productos[i + 6])
            input(Fore.CYAN+"Presione Enter para continuar...")

        elif opcion == "5":
            break

        else:
            print(Fore.RED + "Opción inválida")
            input(Fore.CYAN+"Presione Enter para continuar...")

    return productos
    
def reporte(ventas, user):
    opcion = 0
    while opcion != 5:
        os.system("cls")
        print(Fore.CYAN + "REPORTE DE VENTAS")
        print(Fore.CYAN + "-" * 30)
        print(Fore.CYAN +"1. Reporte de totales por mes")
        print(Fore.CYAN +"2. Reporte de totales por año")
        print(Fore.CYAN +"3. Reporte de totales por mes del vendedor")
        print(Fore.CYAN +"4. Reporte de totales por año del vendedor")
        print(Fore.CYAN +"5. Volver al menú principal")
        opcion = input(Fore.CYAN + "Ingrese una opción: ")

        if opcion == "1":
            mes = input(Fore.CYAN +"Ingrese el mes y año (mm-aaaa) para el reporte: ")
            total = 0
            for v in range(0,len(ventas),6):
                fec = ventas[v+2]
                if fec.endswith(mes):
                    total += ventas[v+5]
            print(Fore.GREEN +"Total de ventas para el mes " + mes + ": $" + str(total))
            os.system("pause")

        elif opcion == "2":
            year = input(Fore.CYAN +"Ingrese el año para el reporte: ")
            total = 0
            for v in range(0,len(ventas),6):
                fec = ventas[v+2]
                if fec[-4:] == year:
                    total += ventas[v+5]
            print(Fore.GREEN +"Total de ventas para el año " + year + ": $" + str(total))
            os.system("pause")

        elif opcion == "3":
            mes = input(Fore.CYAN +"Ingrese el mes y año (mm-aaaa) para el reporte: ")
            total = 0
            for v in range(0,len(ventas),6):
                if ventas[v+1] == user and ventas[v+2].endswith(mes):
                    total += ventas[v+5]
            print(Fore.GREEN +"Total de ventas para el vendedor " + user + " en el mes " + mes + ": $" + str(total))
            os.system("pause")

        elif opcion == "4":
            year = input(Fore.CYAN +"Ingrese el año para el reporte: ")
            total = 0
            for v in range(0,len(ventas),6):
                if ventas[v+1] == user and ventas[v+2][-4:] == year:
                    total += ventas[v+5]
            print(Fore.GREEN +"Total de ventas para el vendedor " + user + " en el año " + year + ": $" + str(total))
            os.system("pause")

        elif opcion == "5":
            break

        else:
            print(Fore.RED + "Opción inválida")
            os.system("pause")
  
def merma():
    op = 0; f = ""; cont = 1; flag2 = False; fe = ""
    os.system("cls")
    print(Fore.CYAN+'''Menu de Mermas
    Que sistema de busqueda desea:
        1) por fecha
        2) por mes
        3) por año''')
    op = int(input(Fore.CYAN+"Ingrese una opcion: "))
    if op == 1:
        f = input(Fore.CYAN+"Ingrese la fecha en formato 'dd-mm-aaaa': ")
        print(Fore.CYAN+f"\nMermas del la fecha {f}:")
        for n in range(1,len(mermas),3):
            if mermas[n] == f:
                flag2 = True
                print(Fore.CYAN+f"    {cont})",mermas[n-1],mermas[n],mermas[n+1])
                cont += 1
        if flag2 == False:
            print(Fore.CYAN+"No existen mermas en esa fecha")
    elif op == 2:
        f = input(Fore.CYAN+"Ingrese la fecha en formato 'mm-aaaa': ")
        print(Fore.CYAN+f"\nMermas del mes {f}:")
        for n in range(1,len(mermas),3):
            fe = mermas[n]
            if fe[3:] == f:
                flag2 = True
                print(Fore.CYAN+f"    {cont})",mermas[n-1],mermas[n],mermas[n+1])
                cont += 1
        if flag2 == False:
            print(Fore.CYAN+"No existen mermas en esa fecha")
    elif op == 3:
        f = input(Fore.CYAN+"Ingrese la fecha en formato 'aaaa': ")
        print(Fore.CYAN+f"\nMermas del año {f}:")
        for n in range(1,len(mermas),3):
            fe = mermas[n]
            if fe[6:] == f:
                flag2 = True
                print(Fore.CYAN+f"    {cont})",mermas[n-1],mermas[n],mermas[n+1])
                cont += 1
        if flag2 == False:
            print(Fore.CYAN+"No existen mermas en esa fecha")
    os.system("pause")
    
def usuario_sis():
    while True:
        op = 0; op2 = ""; op3 = 0; rut = ""; nombre = ""; usu = ""; passw = ""
        os.system("cls")
        print(Fore.CYAN+"MENU DE USUARIOS\n","-"*30)
        print(Fore.CYAN+'''Seleccione una opcion:
        1) Crear usuario
        2) Buscar usuario
        3) Listar usuarios
        4) Modificar usuario
        5) Eliminar usuario
        6) Salir''')
        op = int(input(Fore.CYAN+"Ingrese una opcion: "))
        print("")
        if op == 1:
            print(Fore.CYAN+"Crear usuario\n","-"*15)
            while True:
                fl = 0
                rut = input(Fore.CYAN+"Ingrese rut del nuevo usuario: ")
                for n in range(0,len(usuarios),4):
                    if usuarios[n]==rut:
                        fl += 1
                if fl > 0:
                    print(Fore.CYAN+"El rut ya esta registrado, intente con otro")
                else:
                    break
            nombre = input(Fore.CYAN+"Ingrese nombre del nuevo usuario: ")
            while True:
                fl = 0
                usu = input(Fore.CYAN+"Ingrese nombre de usuario del nuevo usuario: ")
                for n in range(2,len(usuarios),4):
                    if usuarios[n]==usu:
                        fl += 1
                if fl > 0:
                    print(Fore.CYAN+"El nombre de usuario ya esta registrado, intente con otro")
                else:
                    break
            passw = input(Fore.CYAN+"Ingrese contraseña del nuevo usuario: ")
            op2 = input(Fore.CYAN+"\nDesea ingresar al nuevo usuario s/n: ")
            if op2 == "s" or op2 == "S":
                usuarios.extend([rut,nombre,usu,passw])
                print(Fore.CYAN+"Usuario creado exitosamente")
                os.system("pause")
            else:
                print(Fore.CYAN+"El usuario no se agrego")
                os.system("pause")
        elif op == 2:
            print(Fore.CYAN+"Buscar usuario\n","-"*15)
            print(Fore.CYAN+'''Escoja por cual metodo buscar:
        1) Rut
        2) Nombre
        3) Nombre de usuario''')
            op3 = int(input(Fore.CYAN+"Ingrese una opcion: "))
            if op3 == 1:
                op2 = input(Fore.CYAN+"Ingrese rut: ")
                for n in range(0,len(usuarios),4):
                    if usuarios[n] == op2:
                        print(Fore.CYAN+f'''    Rut encontrado:
            Rut: {usuarios[n]}
            Nombre: {usuarios[n+1]}
            Nombre de usuario: {usuarios[n+2]}
            Contraseña: {usuarios[n+3]}''')
                os.system("pause")
            elif op3 == 2:
                op2 = input(Fore.CYAN+"Ingrese nombre: ")
                for n in range(1,len(usuarios),4):
                    if usuarios[n] == op2:
                        print(Fore.CYAN+f'''    Nombre encontrado:
            Rut: {usuarios[n-1]}
            Nombre: {usuarios[n]}
            Nombre de usuario: {usuarios[n+1]}
            Contraseña: {usuarios[n+2]}''')
                os.system("pause")
            elif op3 == 3:
                op2 = input(Fore.CYAN+"Ingrese nombre de usuario: ")
                for n in range(2,len(usuarios),4):
                    if usuarios[n] == op2:
                        print(Fore.CYAN+f'''    Nombre de usuario encontrado:
            Rut: {usuarios[n-2]}
            Nombre: {usuarios[n-1]}
            Nombre de usuario: {usuarios[n]}
            Contraseña: {usuarios[n+1]}''')
                os.system("pause")
        elif op == 3:
            cont = 1
            print(Fore.CYAN+"Listado de usuarios\n","-"*15)
            for n in range(0,len(usuarios),4):
                print(Fore.CYAN+f"        {cont}) {usuarios[n]} / {usuarios[n+1]} / {usuarios[n+2]} / {usuarios[n+3]}")
                cont += 1
            os.system("pause")
        elif op == 4:
            print(Fore.CYAN+"Modificar usuario\n","-"*15)
            rut = input(Fore.CYAN+"Ingrese rut del usuario a modificar: ")
            cont = 0
            for c in range(0,len(usuarios),4):
                if usuarios[c] == rut:
                    cont += 1
                    print(Fore.CYAN+'''\nIngrese que opcion quiere modificar:
        1) Rut
        2) Nombre
        3) Nombre de usuario
        4) Contraseña
        5) Todo''')
                    op3 = int(input(Fore.CYAN+"Ingrese una opcion: "))
                    if op3 == 1:
                        while True:
                            fl = 0
                            rut = input(Fore.CYAN+"Ingrese nuevo rut: ")
                            for n in range(0,len(usuarios),4):
                                if usuarios[n] == rut:
                                    fl += 1
                            if fl > 0:
                                print(Fore.CYAN+"El rut ya esta registrado, intente con otro")
                            else:
                                usuarios[c] = rut
                                break
                        os.system("pause")
                    elif op3 == 2:
                        nombre = input(Fore.CYAN+"Ingrese nuevo nombre: ")
                        usuarios[c+1] = nombre
                        os.system("pause")
                    elif op3 == 3:
                        while True:
                            fl = 0
                            usu = input(Fore.CYAN+"Ingrese nuevo nombre de usuario: ")
                            for n in range(0,len(usuarios),4):
                                if usuarios[n+2] == usu:
                                    fl += 1
                            if fl > 0:
                                print(Fore.CYAN+"El nombre de usuario ya esta registrado, intente con otro")
                            else:
                                usuarios[c+2] = usu
                                break
                        os.system("pause")
                    elif op3 == 4:
                        passw = input(Fore.CYAN+"Ingrese nueva contraseña: ")
                        usuarios[c+3] = passw
                        os.system("pause")
                    elif op3 == 5:
                        while True:
                            fl = 0
                            rut = input(Fore.CYAN+"Ingrese nuevo rut: ")
                            for n in range(0,len(usuarios),4):
                                if usuarios[n] == rut:
                                    fl += 1
                            if fl > 0:
                                print(Fore.CYAN+"El rut ya esta registrado, intente con otro")
                            else:
                                usuarios[c] = rut
                                break
                        nombre = input(Fore.CYAN+"Ingrese nuevo nombre: ")
                        usuarios[c+1] = nombre
                        while True:
                            fl = 0
                            usu = input(Fore.CYAN+"Ingrese nuevo nombre de usuario: ")
                            for n in range(0,len(usuarios),4):
                                if usuarios[n+2] == usu:
                                    fl += 1
                            if fl > 0:
                                print(Fore.CYAN+"El nombre de usuario ya esta registrado, intente con otro")
                            else:
                                usuarios[c+2] = usu
                                break
                        passw = input(Fore.CYAN+"Ingrese nueva contraseña: ")
                        usuarios[c+3] = passw
                        os.system("pause")
            if cont == 0:
                print(Fore.CYAN+"Rut no encontrado")
                os.system("pause")
        elif op == 5:
            cont = 0; op2 = ""
            print(Fore.CYAN+"Eliminar usuario\n","-"*15)
            rut = input(Fore.CYAN+"\nIngrese rut que desea elimiar: ")
            for g in range(0,len(usuarios),4):
                if usuarios[g] == rut:
                    cont += 1
                    print(f'''\nUsuario:
                {usuarios[g]} / {usuarios[g+1]} / {usuarios[g+2]} / {usuarios[g+3]}''')
                    op2 = input(Fore.CYAN+"Desea eliminar este usuario s/n: ")
                    if op2 == "s":
                        for n in range(4):
                            usuarios.pop(g)
                        print(Fore.CYAN+"Usuario eliminado")
                        os.system("pause")
                    else:
                        print(Fore.CYAN+"Eliminacion cancelada")
                        os.system("pause")
                    break
        elif op == 6:
            break

#login
user = login()
if user != "":
    flag = True


#Menu principal
opcion = 0
while flag:
    os.system("cls")
    print(Fore.CYAN+'''    BIENVENIDO AL PUNTO DE VENTA
    --------------------------------------------
          1) Venta
          2) Devolucion
          3) Mantencion de productos
          4) Reporte de ventas
          5) Mermas
          6) Usuarios del sistema
          7) Salir''')    
    opcion = int(input(Fore.CYAN+"Ingrese una opcion: "))
    try:
        if opcion == 1:
            ventas = venta(ventas, productos, boleta,folio)
        elif opcion == 2:
            devolucion()
        elif opcion == 3:
            productos = mantenimiento(productos)
        elif opcion == 4:
            reporte(ventas, user)
        elif opcion == 5:
            merma()
        elif opcion == 6:
            usuario_sis()
        elif opcion == 7:
            break
        else:
            print(Fore.RED+"Opcion invalida")
    except:
        print(Fore.RED+"Opcion invalida")
