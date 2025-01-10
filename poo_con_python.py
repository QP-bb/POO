class Personaje:
    #Atributos de la clase
    # nombre = "Default"
    # fuerza = 0
    # inteligencia = 0
    # defensa = 0
    # vida = 0

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
    # ¿Que significa self? Referencia el mismo objeto
    # ¿Que es init? Constructor que inicializa el atributo del objeto
    # ¿Por que empieza con doble guion bajo? Porque es metodo
    # ¿En que momento se ejecuta el metodo init?
    # Cunado se crea un objeto
    def imprimir_attributos
        print("-Vida",self.vida)

    def subir_nivel(self, nombre, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa

    def definir_vida(self):
        return self.vida > 0

    def morir(self):
        print(self.nombre,"ha muerto")
        return self.vida <= 0

    def dmg(self, enemigo):
        return self.fuerza - enemigo.defensa

    def atk(self, enemigo):
        dmg = self.dmg(enemigo)
        enemigo.vida = enemigo.vida - dmg
        print(self.nombre, "ha realizado ", dmg, "puntos de daño a", enemigo.nombre)
        print("vida de ", enemigo.nombre, "es ", enemigo.vida)

    #Indicar que no se haga nada en este momento
    pass
#Variable del constructor de la clase
mi_personaje = Personaje("Dante",100, 3,70, 100)
mi_personaje.imprimir_attributos()
mi_enemigo = Personaje("Vergil", 70,30,70,100)
mi_enemigo.imprimir_attributos()
mi_personaje.atk(mi_enemigo)
mi_enemigo.imprimir_attributos()
print(mi_personaje.dmg(mi_enemigo))
mi_personaje.morir()
print(mi_personaje.definir_vida())

# mi_personaje.subir_nivel(10,1,5)
# print("------------------")
# mi_personaje.imprimir_attributos()

# mi_personaje.nombre = "ChemaFighter"
# mi_personaje.fuerza = 30
# mi_personaje.inteligencia = 12
# mi_personaje.defensa = 20
# mi_personaje.vida = 3