diccionario={}

class empleado (list):
    def __init__(self, nif, nombre, DOB, sueldom, tipo, var1, var2):
        self.nif=nif
        self.nombre=nombre
        self.DOB=DOB
        self.sueldom=sueldom
        self.tipo=tipo
        self.var1=var1
        self.var2=var2

        self.data=nombre + ", " + DOB + ", " + sueldom + ", " + tipo + ", " + var1 + ", " + var2
        diccionario[self.nif]=self.data

    def datos(self):
        return self.nombre

    def add(self, NIF, nombre, DOB, sueldom, tipo):
        return

def pedir_num():
    print("Menu de opciones")
    print("(1) Añadir empleado")
    print("(2) Borrar empleado")
    print("(3) Mostrar lista empleados")
    print("(4) Mostrar detalle empleado")
    print("(5) Mostrar empleados cumpleaños")
    print("(6) Terminar")
    func=int(input("Elige una opcion: "))
    print("")
    escoger_func(func)


def escoger_func(dato):
    if dato==1:
        add_empl()
    elif dato==2:
        del_empl()
    elif dato==3:
        list_empl()
    elif dato==4:
        data_empl()
    elif dato==5:
        cump_empl()
    elif dato==6:
        end_empl()
    else:
        print("Por favor, escoja una de las 6 opciones posibles")
        print("")
        pedir_num()
    return

def add_empl():
    global diccionario
    print("Introduzca los datos del empleado")
    tipo=input("Tipo de empleado (fijo/temporal): ")
    nombre=input("Introduce el nombre: ")
    nif=input("Introduce el NIF: ")
    dob=input("Introduce la fecha de nacimiento (dd/mm/aaaa): ")
    sueldom=input("Introduce el sueldo mensual: ")
    if tipo=="fijo":
        var1=input("Introduce el año de alta: ")
        var2=input("Introduce el complemento anual: ")
    else:
        var1=input("Introduce la fecha de alta: ")
        var2=input("Introduce la fecha de baja: ")

    empleado1=empleado(nif, nombre, dob, sueldom, tipo, var1, var2)

    pedir_num()
    return

def del_empl():
    global diccionario
    NIF=input("Introduce el NIF del empleado a borrar: ")
    print("")
    if not NIF in diccionario:
        print("Ese empleado no forma parte de la lista")
    else:
        del diccionario[NIF]
        print("Se ha eliminado la suscripcion al empleado " + NIF)
    
    pedir_num()
    return

def list_empl():
    global diccionario
    for empl, data in diccionario.items():
        print(empl, "\t", data)
    print("")

    pedir_num()
    return

def data_empl():
    global diccionario
    NIF=input("Introduce el NIF del empleado quieres consultar: ")
    if not NIF in diccionario:
        print("Ese empleado no forma parte de la lista")
    else:
        print(diccionario[NIF])

    print("")
    pedir_num()
    return

def cump_empl():
    global diccionario
    mes=int(input("Introduce un mes (1-12): "))
    for empl, data in diccionario.items():
        split_data=data.split(", ")
        dob=split_data[1]
        split_dob=dob.split("/")
        mes_empl=int(split_dob[1])
        print(mes + mes_empl)
        if mes_empl==mes:
            print(split_data[0] + ", " + dob)
    print("")

    print("")
    pedir_num()
    return

def end_empl():
    print("Gracias por utilizar nuestros servicios")
    return

pedir_num()