import clases as c

cola = c.Cola()
cod = 1

def menu():
    print("\n1. Agregar Paciente.")
    print("2. Atender Paciente.")
    print("3. Paciente en espera.")
    print("4. Salir.")
    op = int(input("Digite el numero segun la opcion: "))
    print("\n")
    return op

def nuevoPacienteAtnd():
    nom = input("Nombres: ")
    ape = input("Apellidos: ")
    atnd = c.Paciente(nom,ape)
    try:
        cola.pacienteNuevo(atnd)
    except Exception as ex:
        print(str(ex))

def atenderAtnd():
    print("\nPaciente atendido (fuera de cola)")
    print(cola.quitar())

def pacienteActualAtnd():
    for atnd in cola.elementos:
      
        print("\nPaciente en espera")
        print(atnd)
        print("---------")

def main():
    op = 0
    while(op != 4):
        op = menu()
        if(op==1): nuevoPacienteAtnd()
        elif(op==2): atenderAtnd()
        elif(op==3): pacienteActualAtnd()
        elif(op==4): print("Tenga un buen día...")
        else: print("Opcion Invalida...")

main()