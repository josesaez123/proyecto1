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
    
while (mp > 0):

    if mp == 15:
        print("""
----------Tipo De Examenes PCR----------
-                                      -
- a.- Examenes PCR Acumulativos        -
- b.- Examenes PCR No Acumulativos     -
-                                      -
----------------------------------------""")
        z = input("<> ")
    
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

