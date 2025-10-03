class Carrera:

    def __init__(self,nombre, duracion, institucion):
        self.id = None
        self.nombre = nombre
        self.duracion = duracion
        self.institucion = institucion

    def getNombre(self):
        return self.nombre
    def getDuracion(self):
        return self.duracion
    def getInstitucion(self):
        return self.institucion
    def getId(self):
        return self.id
    def setNombre(self, nombre):
        self.nombre = nombre
    def setDuracion(self, duracion):
        self.duracion = duracion
    def setInstitucion(self, institucion):
        self.institucion = institucion
    def setId(self, id):
        self.id = id

    def __str__(self):
        return f"Id: {self.id}, Carrera: {self.nombre}, Duración: {self.duracion} años, Institución: {self.institucion}"
