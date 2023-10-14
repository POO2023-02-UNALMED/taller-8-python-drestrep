import deportista
import persona

class Futbolista(deportista.Deportista, persona.Persona):
    
    listaFutbolistas = []
    def __init__(self, nombre, edad, altura, sexo, anosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        persona.Persona.__init__(self, nombre, edad, altura, sexo)
        deportista.Deportista.__init__(self, "Futbol", anosPracticando)
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Futbolista.listaFutbolistas.append(self)
    
    def getGolesMarcados(self):
        return self._golesMarcados

    
    def setGolesMarcados(self, value):
        self._golesMarcados = value

    
    def getTarjetasRojas(self):
        return self._tarjetasRojas

    
    def setTarjetasRojas(self, value):
        self._tarjetasRojas = value

    
    def getPiernaHabil(self):
        return self._piernaHabil

    
    def setPiernaHabil(self, value):
        self._piernaHabil = value


    def __str__(self):
        return f"Mi nombre es {self._nombre} soy profesional en el deporte {self._deporte} Tengo {self._edad} años de edad y llevo {self._anosPracticando} años en el deporte"