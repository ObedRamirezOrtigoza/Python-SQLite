#clases

class Pelicula:

     #este es un cosntructor
     #No se pasa el ID pues es nuestra primary key y se pasa sola
    def __init__(self,nombre,duracion,genero):
        self.nombre=nombre
        self.duracion=duracion
        self.genero=genero

class Genero: 
    def __init__(self,nombre):
        self.nombre=nombre

#clase para mostrar un catalogo, catalogo no es ua tabla de la db
class Catalogo:
    def __init__(self,nombre):
        self.nombre=nombre
        self.peliculas=[] #una lisa donde se van a guardar las peliculas, las peliculas van a ser objetos
        

        
         