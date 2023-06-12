#productos: id, nombre, categoria, nivel, pack, stock, precio

#nivel(Profesional,Standar,Amateur)
#categoria(Armas, Municiones, Interno, Proteccion, Accesorio, Insumos)
#pack(Unidad, Pack)
#usuario es quien vende
#python -m pip install colorama

from colorama import Fore, init
init(autoreset= True)
#print(Fore.GREEN)
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
folio = 101
user = ""
fecha = datetime.now().strftime("%d-%m-%Y")

os.system("cls")
print(Fore.GREEN+"BIENVENIDO AL PUNTO DE VENTA")
print(Fore.GREEN+"-"*30)
flag = 0
flag2 = True

#login
while True:
    user = input(Fore.GREEN+"Ingrese Usuario: ")
    password = input(Fore.GREEN+"Ingrese Contraseña: ")
    for i in range(len(usuarios)):
        if user == usuarios[i] and password == usuarios[i+1]:
            print(Fore.GREEN+"Usuario Correcto")
            flag += 1
            break
    else:
        print(Fore.RED+"Usuario o Contraseña Invalido")
    if flag != 0:
        break
    a = input(Fore.GREEN+"volver a intentar s/n ")
    if a == "n":
        flag2 = False
        break

#Menu principal
opcion = 0
while flag2:
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
            print("")
        elif opcion == 2:
            print("")
        elif opcion == 3:
            print("")
        elif opcion == 4:
            print("")
        elif opcion == 5:
            print("")
        elif opcion == 6:
            print("")
        elif opcion == 7:
            break
        else:
            print(Fore.RED+"Opcion invalida")
    except:
        print(Fore.RED+"Opcion invalida")
