menu = True

while (menu == True):
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
    opc = int(input("<> "))

    if (opc > 0) and (opc <= 16):

        if opc == 15:
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
                ejey=[0,757,848,1344,1210,1089,1669,824,660,689,1304,975,1042,1076,782]
                plt.plot(ejex,ejey)
                plt.title("Examenes PCR No Acumulativos")
                plt.show()

            if z == "a":
        
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
                ejex=[0,"23-24","25-26","27-28","29-30","1-2","3-4","5-6"]
                ejey=[0,3409,4795,7433,6059,4921,4962,7280]
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
                ejex=[0,"23-24","25-26","27-28","29-30","1-2","3-4","5-6"]
                ejey=[0,1155,2143,4844,7449,10058,13021,14242,15662,16812,18507,21282,24977,26495,28350]
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
                plt.show()

        if z == "a":

                import matplotlib.pyplot as plt
                ejex=[0,"23","24","25","26","27","28","29","30","1","2","3","4","5","6"]
                ejey=[0,1067,3064,8313,13724,18528,23014,25174,26284,28248,33487,38769,43261,46970,48764]
                plt.plot(ejex,ejey)
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
                plt.show()

        if z == "a":

                import matplotlib.pyplot as plt
                ejex=[0,"23","24","25","26","27","28","29","30","1","2","3","4","5","6"]
                ejey=[0,87,468,1218,1750,2472,3015,3248,3425,3775,4274,4755,5280,5780,5899]
                plt.plot(ejex,ejey)
                plt.show()


        if mopc == int("12"):
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
                plt.show()

        if z == "a":

                import matplotlib.pyplot as plt
                ejex=[0,"23","24","25","26","27","28","29","30","1","2","3","4","5","6"]
                ejey=[0,302,595,1601,2379,3272,3862,4297,4598,4858,5805,6843,7515,8124,8623]
                plt.plot(ejex,ejey)
                plt.title()
                plt.show()

print("holiwis")
    elif opc == 00:
        print("Fin Del Programa")
        menu = False
    else:
        print("""
              ----------------------------------
-------------- Error, Ingrese una opcion valida --------------
              ----------------------------------
    """)
