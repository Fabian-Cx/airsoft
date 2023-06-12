#productos: id, nombre, categoria, nivel, pack, stock, precio

#nivel(Profesional,Standar,Amateur)
#categoria(Armas, Municiones, Interno, Proteccion, Accesorio, Insumos)
#pack(Unidad, Pack)aaaaa
#usuario es quien vende
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
          101,"Aperez","21-05-2023","017",2,60000]
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
