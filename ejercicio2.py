class Libro:
    def __init__(self, tit, aut, edi):
        self.titulo = tit
        self.autor = aut
        self.edicion = edi

    def __str__(self):
        return f"""Titulo: {self.titulo}
Autor: {self.autor}
Edición: {self.edicion}"""

pila = []

def menu():
    print("Pila")
    print("1. Libros a tomar prestados ")
    print("2. Mostrar libros retirados de la biblioteca")
    print("3. Salir")
    print("Digite la opcion: ")


def librosAtomar():
    tit = input("Titulo del libro: ")
    aut = input("Autor del libro: ")
    edi = int(input("Edición del libro: "))
    pila.append(Libro(tit, aut, edi))
    print("Libro apilado...")
   

def mostrarPila():
    
    for libro in pila:
        print("Libro que lleva el lector: ")
        print(libro)
        print("Recuerde que debe devolver el libro....")

def principal():
    try:
        op = 0
        while (op != 4):
            menu()
            op = int(input())
            if (op == 1):
                librosAtomar()
            elif (op == 2):
                mostrarPila()
            elif (op == 3):
                print("Gracias por llevar sus libros...")
            else:
                print("Opcion invalida....")

    except Exception as ex:
        print("Error:", str(ex))

principal()