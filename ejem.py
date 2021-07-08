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
    elif opc == 00:
        print("Fin Del Programa")
        menu = False
    else:
        print("""
              ----------------------------------
-------------- Error, Ingrese una opcion valida --------------
              ----------------------------------
    """)
