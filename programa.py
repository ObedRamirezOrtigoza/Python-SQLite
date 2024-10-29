#Programa principal
import funciones
#para que sea recursivo el menu
while True:
    try:
        menu = int(input('''
[1]Agregar pelicula
[2]Obtener peliculas
[0]Para salir del programa\n
>>>'''))
        if menu==1:
            funciones.agregar_pelicula()
        elif menu==2:
            funciones.obtener_peliculas()
        elif menu==0:
            print("Saliendo del programa...")
            exit()
    except ValueError as error:
        print(f'ingrese una opcion valida, {error}')