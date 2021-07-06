listac = ["15", "01", "02", "03", "04", "05", "13", "06", "07", "16", "08", "09", "14", "10", "11", "12"]

listar = ["Región de Arica y Parinacota", "Región de Tarapacá", "Region de Antofagasta", "Region de Atacama", "Región de Coquimbo", "Región de Valparaiso", "Región Metropolitana", "Región del Libertador General Bernardo O'higgins", "Región del Maule", "Región del Ñuble", "Región del Biobio", "Región de la Araucania", "Región de los Rios", "Región de los Lagos", "Región de Aysén del General Carlos Ibáñez del Campo", "Región de Magallanes"]
x   =   0

pepe   =   input("Ingrese region: ")

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
x = int(input("Ingrese una region o su codigo: "))

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
