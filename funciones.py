#Funciones del programa
from modelos import Pelicula,Genero,Catalogo
import sql #import agregar_pelicula

def agregar_pelicula():
    print("Funcion para agregar peliculas\n")
    nombre =str(input("Ingrese el nombre de la pelicula que desea agregar: "))
    duracion =int(input("Ingrese la duracion en minutos de la pelicula que desea agregar: "))
    genero =int(input("Ingrese el genero de la pelicula que desea agregar: "))

    pelicula = Pelicula(nombre, duracion, genero)
    
    sql.agregar_pelicula(pelicula)

catalogo = Catalogo("Peliculas de mafia")

def obtener_peliculas():
    peliculas = sql.obtener_peliculas()
    for pelicula in peliculas:
        guardar_pelicula=Pelicula(pelicula[1],pelicula[2],pelicula[3])
        print(guardar_pelicula)
        catalogo.peliculas.append(guardar_pelicula)
        print(catalogo.peliculas)

    for pelicula in catalogo.peliculas:
        print(f'''\
Nombre de la pelicula:{pelicula.nombre}
Duracion de la pelicula:{pelicula.duracion} en minutos
Genero de la pelicula:{pelicula.genero}
''')
