class Carrera:

    def __init__(self, idcarreras, nombre, duracion, institucion):
        self.id = idcarreras
        self.nombre = nombre
        self.duracion = duracion
        self.institucion = institucion

    def getNombre(self):
        return self.nombre
    def getDuracion(self):
        return self.duracion
    def getInstitucion(self):
        return self.intitucion
    def getId(self):
        return self.id
    def setNombre(self, nombre):
        self.nombre = nombre
    def setDuracion(self, duracion):
        self.duracion = duracion
    def setInstitucion(self, institucion):
        self.institucion = institucion

    def __str__(self):
        return f"Id: {self.id}, Carrera: {self.nombre}, Duración: {self.duracion} años, Institución: {self.institucion}"
