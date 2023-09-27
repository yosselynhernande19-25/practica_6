class Estudiante:
    def __init__(self, nombre, apellido, carnet, carrera):
        self.nombre = nombre
        self.apellido = apellido
        self.carnet = carnet
        self.carrera = carrera

    def actualizar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def actualizar_apellido(self, nuevo_apellido):
        self.apellido = nuevo_apellido

    def actualizar_carnet(self, nuevo_carnet):
        self.carnet = nuevo_carnet

    def actualizar_carrera(self, nueva_carrera):
        self.carrera = nueva_carrera

estudiante = Estudiante("Marilyn", "Orellana", "U20239011", "Ciencias Juridicas")
estudiante.actualizar_nombre("Marilyn Orellana")
print("Nombre Actual: " + estudiante.nombre)   
estudiante.actualizar_nombre("Yosselyn Hernández")
print("Nombre Actualizado:  " + estudiante.nombre)  
estudiante.actualizar_carnet("U20230717")
print("Cambio de Carnet:  " + estudiante.carnet) 
estudiante.actualizar_carrera("Tecnico en desarrollo de software")
print("Cambio de Carrera: " + estudiante.carrera) 