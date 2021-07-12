#Eleccion 2 Seccion 1 Carlos Miranda - Seccion 1 Jose Saez

#Se requiere instalar la biblioteca MatPlotLib para ejecutar el codigo

menu = True #se aplica esta condicion para entrar en el while

while (menu == True):  #al estar en esta condicion se entra en el menu
    print("""
------------- Ingrese El Codigo De Su Region -----------------
-                                                            -
- 15 - Region de Arica y Parinacota                          -
- 01 - Region de Tarapacá                                    -
- 02 - Region de Antofagasta                                 -
- 03 - Region de Atacama                                     -
- 04 - Region de Coquimbo                                    -
- 05 - Region de Valparaiso                                  -
- 13 - Region Metropolitana                                  -
- 06 - Region del Libertador General Bernardo O'higgins      -
- 07 - Region del Maule                                      -
- 16 - Region del Ñuble                                      -
- 08 - Region del Biobio                                     -
- 09 - Region de la Araucania                                -
- 14 - Region de los Rios                                    -
- 10 - Region de los Lagos                                   -
- 11 - Region de Aysén del General Carlos Ibáñez del Campo   -
- 12 - Region de Magallanes                                  -
-                                                            -
- 00 - Salir del programa                                    -
-                                                            -
--------------------------------------------------------------""")
    opc = int(input("<> "))       #Se crea una variable con el fin de manejarlo de forma mas amena a continuación 

    if (opc > 0) and (opc <= 16): #ciclo para todas las regiones

        if opc == 15: 
            print(""" 
    ----------Tipo De Examenes PCR----------
    -                                      -
    - a.- Examenes PCR Acumulativos        -
    - b.- Examenes PCR No Acumulativos     -
    -                                      -
    ----------------------------------------""") #mensaje de indicacion para seleccion de opciones
            z = input("<> ")   #se almacena el input en una variable con el fin de analizarla y aplicarle un if futuramente 

            z = z.lower() #se coloca esto para que por si el usuario ingresa la "a" o "b" en mayuscula se trabajen en minusculas 

            if z == "b":      #si su respuesta es igual a b se le mostrara los examenes no acumulables

                import matplotlib.pyplot as plt #se llama a la biblioteca para asi crear un grafico de lineas
                ejex=[0,"23","24","25","26","27","28","29","30","1","2","3","4","5","6"] #variables que se encuentran en el eje X
                ejey=[0,757,848,1344,1210,1089,1669,824,660,689,1304,975,1042,1076,782] #variables que se encuentran en el eje Y
                plt.plot(ejex,ejey) #con esto se declaran las variables que se tomaran en el grafico
                plt.title("Examenes PCR No Acumulativos") #titulo del grafico
                plt.show() #indicacion para mostrar el grafico

            if z == "a": #si su respuesta es igual a a se le mostrara los examenes no acumulables
        
                import matplotlib.pyplot as plt
                ejex=[0,"23","24","25","26","27","28","29","30","1","2","3","4","5","6"]
                ejey=[0,757,1605,2949,4159,5248,6917,7741,8401,9090,10394,11369,12411,13487,14269]
                plt.plot(ejex,ejey)
                plt.title("Examenes PCR Acumulativos")
                plt.show()
        if opc == int("01"):
            print("""
    ----------Tipo De Examenes PCR----------
    -                                      -
    - a.- Examenes PCR Acumulativos        -
    - b.- Examenes PCR No Acumulativos     -
    -                                      -
    ----------------------------------------""")
            z = input("<> ")

            z = z.lower()


            if z == "b":

                import matplotlib.pyplot as plt
                
                ejex=[0,"23","24","25","26","27","28","29","30","1","2","3","4","5","6"]
                ejey=[0,1229,1121,1368,1156,1468,2306,1498,917,1082,1285,1236,1348,2886,1003]
                plt.plot(ejex,ejey)
                plt.title("Examenes PCR No Acumulativos")
                plt.show()

            if z == "a":

                import matplotlib.pyplot as plt
                ejex=[0,"23","24","25","26","27","28","29","30","1","2","3","4","5","6"]
                ejey=[0,1229,2350,3718,4874,6342,8648,10146,11063,12145,13430,14666,16014,18900,19903]
                plt.plot(ejex,ejey)
                plt.title("Examenes PCR Acumulativos")
                plt.show()

        if opc == int("02"):
            print("""
    ----------Tipo De Examenes PCR----------
    -                                      -
    - a.- Examenes PCR Acumulativos        -
    - b.- Examenes PCR No Acumulativos     -
    -                                      -
    ----------------------------------------""")
            z = input("<> ")

            z = z.lower()


            if z == "b":

                import matplotlib.pyplot as plt
                ejex=[0,"23","24","25","26","27","28","29","30","1","2","3","4","5","6"]
                ejey=[0,913,2496,2505,2290,2440,4993,5152,907,2279,2642,2250,2712,2850,4430]
                plt.plot(ejex,ejey)
                plt.title("Examenes PCR No Acumulativos")
                plt.show()

            if z == "a":

                import matplotlib.pyplot as plt
                ejex=[0,"23","24","25","26","27","28","29","30","1","2","3","4","5","6"]
                ejey=[0,913,3409,5914,8204,10644,15637,20789,21696,23975,26617,28867,31579,34429,38859]
                plt.plot(ejex,ejey)
                plt.title("Examenes PCR Acumulativos")
                plt.show()

        if opc == int("03"):
            print("""
    ----------Tipo De Examenes PCR----------
    -                                      -
    - a.- Examenes PCR Acumulativos        -
    - b.- Examenes PCR No Acumulativos     -
    -                                      -
    ----------------------------------------""")
            z = input("<> ")

            z = z.lower()


            if z == "b":

                import matplotlib.pyplot as plt
                ejex=[0,"23","24","25","26","27","28","29","30","1","2","3","4","5","6"]
                ejey=[0,622,752,1894,1497,1378,1405,1101,1535,729,781,2531,1636,1468,1026]
                plt.plot(ejex,ejey)
                plt.title("Examenes PCR No Acumulativos")
                plt.show()

            if z == "a":

                import matplotlib.pyplot as plt
                ejex=[0,"23","24","25","26","27","28","29","30","1","2","3","4","5","6"]
                ejey=[0,622,1374,3268,4765,6143,7548,8649,10184,10913,11694,14225,15861,17329,18355]
                plt.plot(ejex,ejey)
                plt.title("Examenes PCR Acumulativos")
                plt.show()

        if opc == int("04"):
            print("""
    ----------Tipo De Examenes PCR----------
    -                                      -
    - a.- Examenes PCR Acumulativos        -
    - b.- Examenes PCR No Acumulativos     -
    -                                      -
    ----------------------------------------""")
            z = input("<> ")

            z = z.lower()

            if z == "b":
        
                import matplotlib.pyplot as plt
                ejex=[0,"23","24","25","26","27","28","29","30","1","2","3","4","5","6"]
                ejey=[0,1155,988,2701,2605,2609,2963,1221,1420,1150,1695,2775,3695,1518,1855]
                plt.plot(ejex,ejey)
                plt.title("Examenes PCR No Acumulativos")
                plt.show()

            if z == "a":

                import matplotlib.pyplot as plt
                ejex=[0,"23","24","25","26","27","28","29","30","1","2","3","4","5","6"]
                ejey=[0,1155,2143,4844,7449,10058,13021,14242,15662,16812,18507,21282,24977,26495,28350]
                plt.plot(ejex,ejey)
                plt.title("Examenes PCR Acumulativos")
                plt.show()

        if opc == int("05"):
            print("""
    ----------Tipo De Examenes PCR----------
    -                                      -
    - a.- Examenes PCR Acumulativos        -
    - b.- Examenes PCR No Acumulativos     -
    -                                      -
    ----------------------------------------""")
            z = input("<> ")

            z = z.lower()

            if z == "b":
        
                import matplotlib.pyplot as plt
                ejex=[0,"23","24","25","26","27","28","29","30","1","2","3","4","5","6"]
                ejey=[0,2004,3272,6878,6477,6886,5275,2854,2124,3386,6313,6690,6819,4253,2501]
                plt.plot(ejex,ejey)
                plt.title("Examenes PCR No Acumulativos")
                plt.show()

            if z == "a":

                import matplotlib.pyplot as plt
                ejex=[0,"23","24","25","26","27","28","29","30","1","2","3","4","5","6"]
                ejey=[0,2004,5276,12154,18631,25517,30792,33646,35770,39156,45469,52159,58979,63231,65732]
                plt.plot(ejex,ejey)
                plt.title("Examenes PCR Acumulativos")
                plt.show()

        if opc == int("13"):
            print("""
    ----------Tipo De Examenes PCR----------
    -                                      -
    - a.- Examenes PCR Acumulativos        -
    - b.- Examenes PCR No Acumulativos     -
    -                                      -
    ----------------------------------------""")
            z = input("<> ")

            z = z.lower()

            if z == "b":
        
                import matplotlib.pyplot as plt
                ejex=[0,"23","24","25","26","27","28","29","30","1","2","3","4","5","6"]
                ejey=[0,9306,1907,22067,23450,22387,20678,7160,8238,11110,21711,21085,22425,23501,11024]
                plt.plot(ejex,ejey)
                plt.title("Examenes PCR No Acumulativos")
                plt.show()

            if z == "a":

                import matplotlib.pyplot as plt
                ejex=[0,"23","24","25","26","27","28","29","30","1","2","3","4","5","6"]
                ejey=[0,9306,11213,33280,56730,79117,99795,106955,115193,126303,148014,169099,191524,215025,226049]
                plt.plot(ejex,ejey)
                plt.title("Examenes PCR Acumulativos")
                plt.show()

        if opc == int("06"):
            print("""
    ----------Tipo De Examenes PCR----------
    -                                      -
    - a.- Examenes PCR Acumulativos        -
    - b.- Examenes PCR No Acumulativos     -
    -                                      -
    ----------------------------------------""")
            z = input("<> ")

            z = z.lower()

            if z == "b":
        
                import matplotlib.pyplot as plt
                ejex=[0,"23","24","25","26","27","28","29","30","1","2","3","4","5","6"]
                ejey=[0,1100,884,3110,2916,3277,2467,1175,745,884,2948,2880,3107,2078,1058]
                plt.plot(ejex,ejey)
                plt.title("Examenes PCR No Acumulativos")
                plt.show()

            if z == "a":

                import matplotlib.pyplot as plt
                ejex=[0,"23","24","25","26","27","28","29","30","1","2","3","4","5","6"]
                ejey=[0,1100,1984,5094,8010,11287,13754,14929,15674,16558,19506,22386,25493,27571,28629]
                plt.plot(ejex,ejey)
                plt.title("Examenes PCR Acumulativos")
                plt.show()

        if opc == int("07"):
            print("""
    ----------Tipo De Examenes PCR----------
    -                                      -
    - a.- Examenes PCR Acumulativos        -
    - b.- Examenes PCR No Acumulativos     -
    -                                      -
    ----------------------------------------""")
            z = input("<> ")

            z = z.lower()

            if z == "b":
        
                import matplotlib.pyplot as plt
                ejex=[0,"23","24","25","26","27","28","29","30","1","2","3","4","5","6"]
                ejey=[0,1056,1511,3816,4529,4984,4690,1822,893,1407,4078,4322,4094,3337,1874]
                plt.plot(ejex,ejey)
                plt.title("Examenes PCR No Acumulativos")
                plt.show()

            if z == "a":

                import matplotlib.pyplot as plt
                ejex=[0,"23","24","25","26","27","28","29","30","1","2","3","4","5","6"]
                ejey=[0,1056,2567,6383,10912,15896,20586,22408,23301,24708,28786,33108,37202,40539,42413]
                plt.plot(ejex,ejey)
                plt.title("Examenes PCR Acumulativos")
                plt.show()

        if opc == int("16"):
            print("""
    ----------Tipo De Examenes PCR----------
    -                                      -
    - a.- Examenes PCR Acumulativos        -
    - b.- Examenes PCR No Acumulativos     -
    -                                      -
    ----------------------------------------""")
            z = input("<> ")

            z = z.lower()

            if z == "b":
        
                import matplotlib.pyplot as plt
                ejex=[0,"23","24","25","26","27","28","29","30","1","2","3","4","5","6"]
                ejey=[0,496,784,1768,1670,1854,1393,801,493,743,1917,1696,1833,1326,658]
                plt.plot(ejex,ejey)
                plt.title("Examenes PCR No Acumulativos")
                plt.show()

            if z == "a":

                import matplotlib.pyplot as plt
                ejex=[0,"23","24","25","26","27","28","29","30","1","2","3","4","5","6"]
                ejey=[0,496,1280,3048,4718,6572,7965,8766,9259,10002,11919,13615,15448,16774,17432]
                plt.plot(ejex,ejey)
                plt.title("Examenes PCR Acumulativos")
                plt.show()
                
        if opc == int("08"):
            print("""
    ----------Tipo De Examenes PCR----------
    -                                      -
    - a.- Examenes PCR Acumulativos        -
    - b.- Examenes PCR No Acumulativos     -
    -                                      -
    ----------------------------------------""")
            z = input("<> ")

            z = z.lower()


            if z == "b":

                import matplotlib.pyplot as plt
                ejex=[0,"23","24","25","26","27","28","29","30","1","2","3","4","5","6"]
                ejey=[0,2650,5721,8380,7254,7051,7959,3189,2300,5723,8275,7459,6883,7183,2885]
                plt.plot(ejex,ejey)
                plt.title("Examenes PCR No Acumulativos")
                plt.show()

            if z == "a":

                import matplotlib.pyplot as plt
                ejex=[0,"23","24","25","26","27","28","29","30","1","2","3","4","5","6"]
                ejey=[0,2650,8371,16751,24005,31056,39015,42204,44504,50227,58502,65961,72844,80027,82912]
                plt.plot(ejex,ejey)
                plt.title("Examenes PCR Acumulativos")
                plt.show()

        if opc == int("09"):
            print("""
    ----------Tipo De Examenes PCR----------
    -                                      -
    - a.- Examenes PCR Acumulativos        -
    - b.- Examenes PCR No Acumulativos     -
    -                                      -
    ----------------------------------------""")
            z = input("<> ")
            
            z = z.lower()


            if z == "b":

                import matplotlib.pyplot as plt
                ejex=[0,"23","24","25","26","27","28","29","30","1","2","3","4","5","6"]
                ejey=[0,769,1590,3231,3344,3245,3090,1374,1033,1360,2913,3252,3389,2777,1525]
                plt.plot(ejex,ejey)
                plt.title("Examenes PCR No Acumulativos")
                plt.show()

            if z == "a":

                import matplotlib.pyplot as plt
                ejex=[0,"23","24","25","26","27","28","29","30","1","2","3","4","5","6"]
                ejey=[0,769,2359,5590,8934,12179,15269,16643,17676,19036,21949,25201,28590,31367,32892]
                plt.plot(ejex,ejey)
                plt.title("Examenes PCR Acumulativos")
                plt.show()


        if opc == int("14"):
            print("""
    ----------Tipo De Examenes PCR----------
    -                                      -
    - a.- Examenes PCR Acumulativos        -
    - b.- Examenes PCR No Acumulativos     -
    -                                      -
    ----------------------------------------""")
            z = input("<> ")

            z = z.lower()


            if z == "b":

                import matplotlib.pyplot as plt
                ejex=[0,"23","24","25","26","27","28","29","30","1","2","3","4","5","6"]
                ejey=[0,554,882,2618,2500,2319,1523,970,484,928,2565,2195,2197,1543,824]
                plt.plot(ejex,ejey)
                plt.title("Examenes PCR No Acumulativos")
                plt.show()

            if z == "a":

                import matplotlib.pyplot as plt
                ejex=[0,"23","24","25","26","27","28","29","30","1","2","3","4","5","6"]
                ejey=[0,554,1436,4054,6554,8873,10396,11366,11850,12778,15343,17538,19735,21278,22102]
                plt.plot(ejex,ejey)
                plt.title("Examenes PCR Acumulativos")
                plt.show()   
    
        if opc == int("10"):
            print("""
    ----------Tipo De Examenes PCR----------
    -                                      -
    - a.- Examenes PCR Acumulativos        -
    - b.- Examenes PCR No Acumulativos     -
    -                                      -
    ----------------------------------------""")
            z = input("<> ")

            z = z.lower()


            if z == "b":

                import matplotlib.pyplot as plt
                ejex=[0,"23","24","25","26","27","28","29","30","1","2","3","4","5","6"]
                ejey=[0,1067,1997,5249,5411,4804,4486,2160,1110,1964,5239,5282,4492,3709,1794]
                plt.plot(ejex,ejey)
                plt.title("Examenes PCR No Acumulativos")
                plt.show()

            if z == "a":

                import matplotlib.pyplot as plt
                ejex=[0,"23","24","25","26","27","28","29","30","1","2","3","4","5","6"]
                ejey=[0,1067,3064,8313,13724,18528,23014,25174,26284,28248,33487,38769,43261,46970,48764]
                plt.plot(ejex,ejey)
                plt.title("Examenes PCR Acumulativos")
                plt.show()


        if opc == int("11"):
            print("""
    ----------Tipo De Examenes PCR----------
    -                                      -
    - a.- Examenes PCR Acumulativos        -
    - b.- Examenes PCR No Acumulativos     -
    -                                      -
    ----------------------------------------""")
            z = input("<> ")

            z = z.lower()


            if z == "b":

                import matplotlib.pyplot as plt
                ejex=[0,"23","24","25","26","27","28","29","30","1","2","3","4","5","6"]
                ejey=[0,87,381,750,532,722,543,233,177,350,499,481,525,500,199]
                plt.plot(ejex,ejey)
                plt.title("Examenes PCR No Acumulativos")
                plt.show()

            if z == "a":

                import matplotlib.pyplot as plt
                ejex=[0,"23","24","25","26","27","28","29","30","1","2","3","4","5","6"]
                ejey=[0,87,468,1218,1750,2472,3015,3248,3425,3775,4274,4755,5280,5780,5899]
                plt.plot(ejex,ejey)
                plt.title("Examenes PCR Acumulativos")
                plt.show()


        if opc == int("12"):
            print("""
    ----------Tipo De Examenes PCR----------
    -                                      -
    - a.- Examenes PCR Acumulativos        -
    - b.- Examenes PCR No Acumulativos     -
    -                                      -
    ----------------------------------------""")
            z = input("<> ")

            z = z.lower()


            if z == "b":

                import matplotlib.pyplot as plt
                ejex=[0,"23","24","25","26","27","28","29","30","1","2","3","4","5","6"]
                ejey=[0,302,293,1006,778,893,590,435,301,260,947,1038,672,609,499]
                plt.plot(ejex,ejey)
                plt.title("Examenes PCR No Acumulativos")
                plt.show()

            if z == "a":

                import matplotlib.pyplot as plt
                ejex=[0,"23","24","25","26","27","28","29","30","1","2","3","4","5","6"]
                ejey=[0,302,595,1601,2379,3272,3862,4297,4598,4858,5805,6843,7515,8124,8623]
                plt.plot(ejex,ejey)
                plt.title("Examenes PCR Acumulativos")
                plt.show()
    elif opc == 00:    #se crea un elif con el fin de dar termino al programa en caso de que la persona lo desee
        print("Fin Del Programa")
        menu = False #se decreta menu = false para finalizar el ciclo y salir del programa 
    else:                    #se crea un else en caso de que una persona cometa un erro al ingresar un dato
        print("""      
              ----------------------------------
-------------- Error, Ingrese una opcion valida --------------
              ----------------------------------
    """)


