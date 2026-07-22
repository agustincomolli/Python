# Composicion de clases en python 

# "que tine" o "tiene un"

#CLASE PELICULA(metodo y atributos):
#atributos: titulo, duracion, lanzamiento

#CLASE CATALOGO(metodo y atributos):


class Pelicula:
   def __init__(self, titulo, duracion, lanzamiento):
      self.titulo = titulo
      self.duracion = duracion
      self.lanzamiento = lanzamiento

   def __str__(self):
       return 'Titulo:{}, Pelicula: {}'.format(self.titulo, self.lanzamiento)

class Catalogo:
    lista_peliculas = [] #lista vacia

    def __init__(self, lista_peliculas=[]): #metodo constructor
        self.lista_peliculas = lista_peliculas #inicializamos la lista

    def agregar_pelicula(self, pelicula): #metodo para agregar pelicula
        self.lista_peliculas.append(pelicula) #agregamos la pelicula a la lista

    def mostrar_peliculas(self): #metodo para mostrar peliculas
        for pelicula in self.lista_peliculas:
            print(pelicula) #imprimimos la pelicula


#PROGRAMA PRINCIPAL

pelicula1 = Pelicula("El Padrino", 175, 1972) #creamos un objeto de la clase Pelicula
pelicula2 = Pelicula("El Padrino 2", 202, 1974) #creamos un objeto de la clase Pelicula

#catalogo_de_peliculas = Catalogo() #creamos un objeto de la clase Catalogo

catalago_de_peliculas = Catalogo() #creamos un objeto de la clase Catalogo

pelicula3 = Pelicula("El Padrino 3", 162, 1990) #creamos un objeto de la clase Pelicula
pelicula4 = Pelicula("El Padrino 4", 162, 1990) #creamos un objeto de la clase Pelicula

catalago_de_peliculas.agregar_pelicula(pelicula1) #agregamos la pelicula1 al catalogo
catalago_de_peliculas.agregar_pelicula(pelicula2) #agregamos la pelicula2 al catalogo
catalago_de_peliculas.agregar_pelicula(pelicula3) #agregamos la pelicula3 al catalogo
catalago_de_peliculas.agregar_pelicula(pelicula4) #agregamos la pelicula4 al catalogo

catalago_de_peliculas.mostrar_peliculas() #mostramos las peliculas del catalogo


lista_de_peliculas_2 = [pelicula1, pelicula2, pelicula3, pelicula4] #creamos una lista de peliculas

cotalogo_de_peliculas2 = Catalogo(lista_de_peliculas_2) #creamos un objeto de la clase Catalogo