


class Cliente:
    def __init__(self):
        pass


    def get_input(self):
        recetas = ()        # Lista con recetas para mostrarle al usuario
        for i in range(0, 10):
            receta = input("Dime una receta que hayas probado: ")
            rating = input("Dime un rating para la receta: ")
            recetas.append((receta, rating))
