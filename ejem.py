listac = ["15", "01", "02", "03", "04", "05", "13", "06", "07", "16", "08", "09", "14", "10", "11", "12"]

listar = ["Region de Arica y Parinacota", "Region de Tarapacá", "Region de Antofagasta", "Region de Atacama", "Region de Coquimbo", "Region de Valparaiso", "Region Metropolitana", "Region del Libertador General Bernardo O'higgins", "Region del Maule", "Region del Ñuble", "Region del Biobio", "Region de la Araucania", "Region de los Rios", "Region de los Lagos", "Region de Aysén del General Carlos Ibáñez del Campo", "Region de Magallanes"]

mp = int(input("""
------------ Ingrese El Codigo De Su Region ----------------
-                                                          -
- 15.Region de Arica y Parinacota                          -
- 01.Region de Tarapacá                                    -
- 02.Region de Antofagasta                                 -
- 03.Region de Atacama                                     -
- 04.Region de Coquimbo                                    -
- 05.Region de Valparaiso                                  -
- 13.Region Metropolitana                                  -
- 06.Region del Libertador General Bernardo O'higgins      -
- 07.Region del Maule                                      -
- 16.Region del Ñuble                                      -
- 08.Region del Biobio                                     -
- 09.Region de la Araucania                                -
- 14.Region de los Rios                                    -
- 10.Region de los Lagos                                   -
- 11.Region de Aysén del General Carlos Ibáñez del Campo   -
- 12.Region de Magallanes                                  -
-                                                          -
------------------------------------------------------------
<> """))

while (mp < 0) or (mp > 16):
    print("""
           ----------------------------------
----------- Error, Ingrese una opcion valida --------------
           ----------------------------------
""")
    
    mp = int(input("""
------------- Ingrese El Codigo De Su Region ---------------
-                                                          -
- 15.Region de Arica y Parinacota                          -
- 01.Region de Tarapacá                                    -
- 02.Region de Antofagasta                                 -
- 03.Region de Atacama                                     -
- 04.Region de Coquimbo                                    -
- 05.Region de Valparaiso                                  -
- 13.Region Metropolitana                                  -
- 06.Region del Libertador General Bernardo O'higgins      -
- 07.Region del Maule                                      -
- 16.Region del Ñuble                                      -
- 08.Region del Biobio                                     -
- 09.Region de la Araucania                                -
- 14.Region de los Rios                                    -
- 10.Region de los Lagos                                   -
- 11.Region de Aysén del General Carlos Ibáñez del Campo   -
- 12.Region de Magallanes                                  -
-                                                          -
------------------------------------------------------------
<> """))
    
wwhile (mp > 0): #AGREGAR LOS IF PARA SALIR DEL PROGRAMA O BUCLE

    if mp == 15:
        print("""
----------Tipo De Examenes PCR----------
-                                      -
- a.- Examenes PCR Acumulativos        -
- b.- Examenes PCR No Acumulativos     -
-                                      -
----------------------------------------""")
        z = input("<> ")

        z = z.lower()

        if z == "a":

            import matplotlib.pyplot as plt
            ejex=[0,"23","24","25","26","27","28","29","30","1","2","3","4","5","6"]
            ejey=[0,757,848,1344,1210,1089,1669,824,660,689,1304,975,1042,1076,782]
            plt.plot(ejex,ejey)
            plt.show()

        if z == "b":
    
            import matplotlib.pyplot as plt
            ejex=[0,"23-24","25-26","27-28","29-30","1-2","3-4","5-6"]
            ejey=[0,1605,2554,2758,1484,1993,2017,1858]
            plt.plot(ejex,ejey)
            plt.show()

    if mp == int("01"):
        print("""
----------Tipo De Examenes PCR----------
-                                      -
- a.- Examenes PCR Acumulativos        -
- b.- Examenes PCR No Acumulativos     -
-                                      -
----------------------------------------""")
        z = input("<> ")

        z = z.lower()

    
        if z == "a":

            import matplotlib.pyplot as plt
            ejex=[0,"23","24","25","26","27","28","29","30","1","2","3","4","5","6"]
            ejey=[0,1229,1121,1368,1156,1468,2306,1498,917,1082,1285,1236,1348,2886,1003]
            plt.plot(ejex,ejey)
            plt.show()

        if z == "b":
    
            import matplotlib.pyplot as plt
            ejex=[0,"23-24","25-26","27-28","29-30","1-2","3-4","5-6"]
            ejey=[0,2350,2524,3774,2415,2367,2584,3889]
            plt.plot(ejex,ejey)
            plt.show()

    if mp == int("02"):
        print("""
----------Tipo De Examenes PCR----------
-                                      -
- a.- Examenes PCR Acumulativos        -
- b.- Examenes PCR No Acumulativos     -
-                                      -
----------------------------------------""")
        z = input("<> ")

        z = z.lower()

    
        if z == "a":

            import matplotlib.pyplot as plt
            ejex=[0,"23","24","25","26","27","28","29","30","1","2","3","4","5","6"]
            ejey=[0,913,2496,2505,2290,2440,4993,5152,907,2279,2642,2250,2712,2850,4430]
            plt.plot(ejex,ejey)
            plt.show()

        if z == "b":
    
            import matplotlib.pyplot as plt
            ejex=[0,"23-24","25-26","27-28","29-30","1-2","3-4","5-6"]
            ejey=[0,3409,4795,7433,6059,4921,4962,7280]
            plt.plot(ejex,ejey)
            plt.show()
 
    if mp == int("03"):
        print("""
----------Tipo De Examenes PCR----------
-                                      -
- a.- Examenes PCR Acumulativos        -
- b.- Examenes PCR No Acumulativos     -
-                                      -
----------------------------------------""")
        z = input("<> ")

        z = z.lower()

    
        if z == "a":

            import matplotlib.pyplot as plt
            ejex=[0,"23","24","25","26","27","28","29","30","1","2","3","4","5","6"]
            ejey=[0,622,752,1894,1497,1378,1405,1101,1535,729,781,2531,1636,1468,1026]
            plt.plot(ejex,ejey)
            plt.show()

        if z == "b":
    
            import matplotlib.pyplot as plt
            ejex=[0,"23","24","25","26","27","28","29","30","1","2","3","4","5","6"]
            ejey=[0,622,1374,3268,4765,6143,7548,8649,10184,10913,11694,14225,15861,17329,18355]
            plt.plot(ejex,ejey)
            plt.show()

    if mp == int("04"):
        print("""
----------Tipo De Examenes PCR----------
-                                      -
- a.- Examenes PCR Acumulativos        -
- b.- Examenes PCR No Acumulativos     -
-                                      -
----------------------------------------""")
        z = input("<> ")

        z = z.lower()

    
        if z == "a":

            import matplotlib.pyplot as plt
            ejex=[0,"23","24","25","26","27","28","29","30","1","2","3","4","5","6"]
            ejey=[0,1155,988,2701,2605,2609,2963,1221,1420,1150,1695,2775,3695,1518,1855]
            plt.plot(ejex,ejey)
            plt.show()

        if z == "b":
    
            import matplotlib.pyplot as plt
            ejex=[0,"23-24","25-26","27-28","29-30","1-2","3-4","5-6"]
            ejey=[0,1155,2143,4844,7449,10058,13021,14242,15662,16812,18507,21282,24977,26495,28350]
            plt.plot(ejex,ejey)
            plt.show()
            

    if mp == int("05"):
        print("""
----------Tipo De Examenes PCR----------
-                                      -
- a.- Examenes PCR Acumulativos        -
- b.- Examenes PCR No Acumulativos     -
-                                      -
----------------------------------------""")
        z = input("<> ")

        z = z.lower()

    
        if z == "a":

            import matplotlib.pyplot as plt
            ejex=[4,8,13,17,20]
            ejey=[54,67,98,78,45]
            plt.plot(ejex,ejey)
            plt.show()

        if z == "b":
    
            import matplotlib.pyplot as plt
            ejex=[999,1000,13,17,20]
            ejey=[54,67,98,78,45]
            plt.plot(ejex,ejey)
            plt.show()
            

    if mp == int("13"):
        print("""
----------Tipo De Examenes PCR----------
-                                      -
- a.- Examenes PCR Acumulativos        -
- b.- Examenes PCR No Acumulativos     -
-                                      -
----------------------------------------""")
        z = input("<> ")

        z = z.lower()

    
        if z == "a":

            import matplotlib.pyplot as plt
            ejex=[4,8,13,17,20]
            ejey=[54,67,98,78,45]
            plt.plot(ejex,ejey)
            plt.show()

        if z == "b":
    
            import matplotlib.pyplot as plt
            ejex=[999,1000,13,17,20]
            ejey=[54,67,98,78,45]
            plt.plot(ejex,ejey)
            plt.show()
            

    if mp == int("06"):
        print("""
----------Tipo De Examenes PCR----------
-                                      -
- a.- Examenes PCR Acumulativos        -
- b.- Examenes PCR No Acumulativos     -
-                                      -
----------------------------------------""")
        z = input("<> ")

        z = z.lower()

    
        if z == "a":

            import matplotlib.pyplot as plt
            ejex=[4,8,13,17,20]
            ejey=[54,67,98,78,45]
            plt.plot(ejex,ejey)
            plt.show()

        if z == "b":
    
            import matplotlib.pyplot as plt
            ejex=[999,1000,13,17,20]
            ejey=[54,67,98,78,45]
            plt.plot(ejex,ejey)
            plt.show()
            

    if mp == int("07"):
        print("""
----------Tipo De Examenes PCR----------
-                                      -
- a.- Examenes PCR Acumulativos        -
- b.- Examenes PCR No Acumulativos     -
-                                      -
----------------------------------------""")
        z = input("<> ")

        z = z.lower()

    
        if z == "a":

            import matplotlib.pyplot as plt
            ejex=[4,8,13,17,20]
            ejey=[54,67,98,78,45]
            plt.plot(ejex,ejey)
            plt.show()

        if z == "b":
    
            import matplotlib.pyplot as plt
            ejex=[999,1000,13,17,20]
            ejey=[54,67,98,78,45]
            plt.plot(ejex,ejey)
            plt.show()
            

    if mp == 16:
        print("""
----------Tipo De Examenes PCR----------
-                                      -
- a.- Examenes PCR Acumulativos        -
- b.- Examenes PCR No Acumulativos     -
-                                      -
----------------------------------------""")
        z = input("<> ")

        z = z.lower()

    
        if z == "a":

            import matplotlib.pyplot as plt
            ejex=[4,8,13,17,20]
            ejey=[54,67,98,78,45]
            plt.plot(ejex,ejey)
            plt.show()

        if z == "b":
    
            import matplotlib.pyplot as plt
            ejex=[999,1000,13,17,20]
            ejey=[54,67,98,78,45]
            plt.plot(ejex,ejey)
            plt.show()
            

    if mp == int("08"):
        print("""
----------Tipo De Examenes PCR----------
-                                      -
- a.- Examenes PCR Acumulativos        -
- b.- Examenes PCR No Acumulativos     -
-                                      -
----------------------------------------""")
        z = input("<> ")

        z = z.lower()

    
        if z == "a":

            import matplotlib.pyplot as plt
            ejex=[4,8,13,17,20]
            ejey=[54,67,98,78,45]
            plt.plot(ejex,ejey)
            plt.show()

        if z == "b":
    
            import matplotlib.pyplot as plt
            ejex=[999,1000,13,17,20]
            ejey=[54,67,98,78,45]
            plt.plot(ejex,ejey)
            plt.show()

    if mp == int("09"):
        print("""
----------Tipo De Examenes PCR----------
-                                      -
- a.- Examenes PCR Acumulativos        -
- b.- Examenes PCR No Acumulativos     -
-                                      -
----------------------------------------""")
        z = input("<> ")

        z = z.lower()

    
        if z == "a":

            import matplotlib.pyplot as plt
            ejex=[4,8,13,17,20]
            ejey=[54,67,98,78,45]
            plt.plot(ejex,ejey)
            plt.show()

        if z == "b":
    
            import matplotlib.pyplot as plt
            ejex=[999,1000,13,17,20]
            ejey=[54,67,98,78,45]
            plt.plot(ejex,ejey)
            plt.show()
            

    if mp == 14:
        print("""
----------Tipo De Examenes PCR----------
-                                      -
- a.- Examenes PCR Acumulativos        -
- b.- Examenes PCR No Acumulativos     -
-                                      -
----------------------------------------""")
        z = input("<> ")

        z = z.lower()

    
        if z == "a":

            import matplotlib.pyplot as plt
            ejex=[4,8,13,17,20]
            ejey=[54,67,98,78,45]
            plt.plot(ejex,ejey)
            plt.show()

        if z == "b":
    
            import matplotlib.pyplot as plt
            ejex=[999,1000,13,17,20]
            ejey=[54,67,98,78,45]
            plt.plot(ejex,ejey)
            plt.show()
            

    if mp == 10:
        print("""
----------Tipo De Examenes PCR----------
-                                      -
- a.- Examenes PCR Acumulativos        -
- b.- Examenes PCR No Acumulativos     -
-                                      -
----------------------------------------""")
        z = input("<> ")

        z = z.lower()

    
        if z == "a":

            import matplotlib.pyplot as plt
            ejex=[4,8,13,17,20]
            ejey=[54,67,98,78,45]
            plt.plot(ejex,ejey)
            plt.show()

        if z == "b":
    
            import matplotlib.pyplot as plt
            ejex=[999,1000,13,17,20]
            ejey=[54,67,98,78,45]
            plt.plot(ejex,ejey)
            plt.show()
            

    if mp == 11:
        print("""
----------Tipo De Examenes PCR----------
-                                      -
- a.- Examenes PCR Acumulativos        -
- b.- Examenes PCR No Acumulativos     -
-                                      -
----------------------------------------""")
        z = input("<> ")

        z = z.lower()

    
        if z == "a":

            import matplotlib.pyplot as plt
            ejex=[4,8,13,17,20]
            ejey=[54,67,98,78,45]
            plt.plot(ejex,ejey)
            plt.show()

        if z == "b":
    
            import matplotlib.pyplot as plt
            ejex=[999,1000,13,17,20]
            ejey=[54,67,98,78,45]
            plt.plot(ejex,ejey)
            plt.show()
            

    if mp == 12:
        print("""
----------Tipo De Examenes PCR----------
-                                      -
- a.- Examenes PCR Acumulativos        -
- b.- Examenes PCR No Acumulativos     -
-                                      -
----------------------------------------""")
        z = input("<> ")

        z = z.lower()

    
        if z == "a":

            import matplotlib.pyplot as plt
            ejex=[4,8,13,17,20]
            ejey=[54,67,98,78,45]
            plt.plot(ejex,ejey)
            plt.show()

        if z == "b":
    
            import matplotlib.pyplot as plt
            ejex=[999,1000,13,17,20]
            ejey=[54,67,98,78,45]
            plt.plot(ejex,ejey)
            plt.show()

print("holiwis")


