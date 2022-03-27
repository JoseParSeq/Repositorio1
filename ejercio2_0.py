
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
