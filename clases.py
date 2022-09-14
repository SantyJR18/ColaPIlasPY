class Paciente: 
    #Paciente
    def __init__(self,nom, ape):
     
     
     self.nombres = nom
     self.apellidos  = ape 
     
     
    def __str__(self):
        return f"""Nombres: {self.nombres}
Apellidos: {self.apellidos}"""

class Cola:
    def __init__(self):
        self.elementos = []

    def pacienteNuevo(self, elem):
        self.elementos.append(elem)

    def quitar(self):
        try:
           return self.elementos.pop(0)
        except Exception as ex:
           print("Cola vacía...", str(ex))

    def estaVacia(self):
        return self.elementos == []