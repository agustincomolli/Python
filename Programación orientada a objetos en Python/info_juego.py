class InfoJuego():
    autor = "Anónimo"

    def __init__(self,titulo_juego) -> None:
        self.titulo = titulo_juego
    
    def bienvenido(self):
        print(f"Bienvenido a {self.titulo}")

    @staticmethod
    def info():
        print("Creado con el creador de juegos OOP RPG (c) yo")

    @classmethod
    def creditos(cls):
        print("\nGracias por jugar.")
        print(f"Creado por {cls.autor}")