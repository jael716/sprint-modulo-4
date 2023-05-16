import json
import random


class ValorNoValido(Exception):
    pass


# La clase Personaje
class Personaje:
    def __init__(self, nombre, poder,vida):
        if not isinstance(nombre, str):
            raise ValorNoValido("El nombre debe ser una cadena de texto.")
        if not isinstance(poder, (int)) or poder < 0:
            raise ValorNoValido("El poder debe ser un número positivo.")

        self.nombre = nombre
        self.poder = poder
        self.__vida=vida

    def atacar(self,adversario):
        adversario.__vida-=self.poder
        return f"{self.nombre} ataca con un poder de {self.poder} a {adversario.nombre}."
    
    def salud_adversario(self,adversario): 
        return f"{adversario.nombre} tiene una salud de {adversario.__vida}"
    
    def salud_propia(self): 
        return f"{self.nombre} tiene una salud de {self.__vida}"



# La clase Saiyajin hereda de la clase Personaje
class Saiyajin(Personaje):
    def __init__(self, nombre, poder,vida, transformacion):
        super().__init__(nombre, poder,vida)  # Usamos la función super()
        if not isinstance(transformacion, str):
            raise ValorNoValido("La transformación debe ser una cadena de texto.")

        self.transformacion = transformacion

    def transformar(self):
        return f"{self.nombre} se transforma en {self.transformacion}."


# La clase Androide hereda de la clase Personaje
class Androide(Personaje):
    def __init__(self, nombre, poder,vida, creador):
        super().__init__(nombre, poder,vida)
        if not isinstance(creador, str):
            raise ValorNoValido("El creador debe ser una cadena de texto.")

        self.creador = creador

    def informacion(self):
        return f"{self.nombre} fue creado por {self.creador}."


# La clase kai hereda de la clase Personaje
class Kai(Personaje):
    def __init__(self, nombre, poder,vida, planeta):
        super().__init__(nombre, poder,vida)
        if not isinstance(planeta, str):
            raise ValorNoValido("El planeta debe ser una cadena de texto.")

        self.planeta = planeta

    def entrenamiento(self):
        return f"{self.nombre} entrena en el planeta {self.planeta}."



# Crear instancias de las clases
goku = Saiyajin("Goku", 9001, 55000, "Super Saiyajin")
vegeta = Saiyajin("Vegeta", 8950, 54000, "Super Saiyajin")
gohan = Saiyajin("Gohan", 8600, 40000, "Super Saiyajin")
trunks = Saiyajin("Trunks", 8650, 41000, "Super Saiyajin")
c16 = Androide("C-16", 8400, 60000, "Dr. Gero")
c17 = Androide("C-17", 8500, 45000, "Dr. Gero")
c18 = Androide("C-18", 8600, 45000, "Dr. Gero")
kaioshin = Kai("Kaioshin",8800, 30000, "Kaishin")
kaiosama = Kai("Kaiosama", 3600, 15000, "Namek")
kaioshin_anciano = Kai("Kaioshin-Anciano", 1500, 100000, "Planeta Sagrado")
print(goku.atacar(c17))
print(goku.transformar())
print(c17.atacar(goku))
print(c17.informacion())
print(kaioshin.atacar(c16))
print(kaioshin.entrenamiento())
print(c16.salud_propia())
# Guardar la información de los personajes en un archivo JSON
personajes = [goku.__dict__, c17.__dict__, kaioshin.__dict__, vegeta.__dict__, gohan.__dict__, trunks.__dict__, c16.__dict__, c18.__dict__, kaiosama.__dict__, kaioshin_anciano.__dict__]
with open("personajes.json", "w") as f:
    json.dump(personajes, f)

# Carga de datos de personajes desde el archivo JSON
with open("personajes.json", "r") as f:
    personajes_json = json.load(f)
print("------------------------------------------")
# Mapeo de los datos JSON a las instancias de la clase
personajes = []
for personaje_json in personajes_json:
    if 'transformacion' in personaje_json:
        personajes.append(Saiyajin(personaje_json['nombre'], personaje_json['poder'], personaje_json['_Personaje__vida'], personaje_json['transformacion']))
    elif 'creador' in personaje_json:
        personajes.append(Androide(personaje_json['nombre'], personaje_json['poder'], personaje_json['_Personaje__vida'], personaje_json['creador']))
    elif 'planeta' in personaje_json:
        personajes.append(Kai(personaje_json['nombre'], personaje_json['poder'], personaje_json['_Personaje__vida'], personaje_json['planeta']))

# Selección de dos personajes al azar para la batalla
while True:
    if len(personajes)<2:
        break
    p1 = random.choice(personajes)
    p2 = random.choice(personajes)
    # Para evitar que un personaje luche contra sí mismo
    while p1==p2:
        p2 = random.choice(personajes)
    print("Enfrentamiento entre")
    print(f"{p1.nombre} v/s {p2.nombre}")

    # Lógica de la batalla
    while True:
        p1.atacar(p2)
        if p2._Personaje__vida <= 0:
            print(f"{p1.nombre} ha ganado la batalla.")
            personajes.remove(p2)
            break

        p2.atacar(p1)
        if p1._Personaje__vida <= 0:
            print(f"{p2.nombre} ha ganado la batalla.")
            personajes.remove(p1)
            break
    print("-------------------------------")