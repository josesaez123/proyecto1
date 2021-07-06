listac = ["15", "01", "02", "03", "04", "05", "13", "06", "07", "16", "08", "09", "14", "10", "11", "12"]

listar = ["Region de Arica y Parinacota", "Region de Tarapacá", "Region de Antofagasta", "Region de Atacama", "Region de Coquimbo", "Region de Valparaiso", "Region Metropolitana", "Region del Libertador General Bernardo O'higgins", "Region del Maule", "Region del Ñuble", "Region del Biobio", "Region de la Araucania", "Region de los Rios", "Region de los Lagos", "Region de Aysén del General Carlos Ibáñez del Campo", "Region de Magallanes"]
x   =   0

pepe = int(input("Ingrese una region o su codigo: "))

for i in range(listar):
    if pepe[0]  ==  listar[i]:
        x = 5

    if pepe[0]  ==  listac[i]:
        x = 10

print ("""
15.Región de Arica y Parinacota
01.Región de Tarapacá
02.Region de Antofagasta
03.Region de Atacama
04.Región de Coquimbo
05.Región de Valparaiso
13.Región Metropolitana
06.Región del Libertador General Bernardo O'higgins
07.Región del Maule
16.Región del Ñuble
08.Región del Biobio
09.Región de la Araucania
14.Región de los Rios
10.Región de los Lagos
11.Región de Aysén del General Carlos Ibáñez del Campo
12.Región de Magallanes
""")

if x == 1:
    print("a.- Examenes PCR acumulativos")
    print("b.- Examenes PCR no acumulativos")
    z = input("Ingrese una opcion: ")

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

if x == 1:
    print("a.- Examenes PCR acumulativos")
    print("b.- Examenes PCR no acumulativos")
    z = input("Ingrese una opcion: ")

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

if x == 2:
    print("a.- Examenes PCR acumulativos")
    print("b.- Examenes PCR no acumulativos")
    z = input("Ingrese una opcion: ")

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

if x == 3:
    print("a.- Examenes PCR acumulativos")
    print("b.- Examenes PCR no acumulativos")
    z = input("Ingrese una opcion: ")

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
