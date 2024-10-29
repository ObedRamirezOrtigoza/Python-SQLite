#Codigo relacionado a la base de datos
from constantes import * #Importar todas las constantes 
import sqlite3

def conectar_db():
    conexion = sqlite3.connect(DATABASE_NAME) #pasamos el nombre de la base de datos pero esta es una variable de entorno de ambiente asi que se escribe en constantes
    cursor = conexion.cursor()
    return conexion, cursor

def agregar_pelicula(pelicula):
    conexion,cursor = conectar_db()
    pelicula = (
        pelicula.nombre,
        pelicula.duracion,
        pelicula.genero
    )
    sql = f"INSERT INTO pelicula (nombre, duracion, genero) VALUES {pelicula};"
    #sql = f"INSERT INTO pelicula (nombre, duracion, genero) VALUES ('{pelicula[0]}', {pelicula[1]}, '{pelicula[2]}');"
    ##sql = "INSERT INTO pelicula (nombre, duracion, genero) VALUES (?, ?, ?)"
    ##cursor.execute(sql, pelicula)
    cursor.execute(sql)
    conexion.commit()
    conexion.close()


def obtener_peliculas():
    conexion,cursor = conectar_db()
    sql = "SELECT * FROM pelicula;"
    cursor.execute(sql)
    peliculas= cursor.fetchall()
    print(peliculas)
    conexion.close()
    return peliculas

