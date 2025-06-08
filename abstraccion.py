from abc import ABC, abstractmethod

# Clase abstracta para dispositivos electrónicos
class Dispositivo(ABC):
    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass

# Implementación concreta
class Televisor(Dispositivo):
    def encender(self):
        print("El televisor se ha encendido.")

    def apagar(self):
        print("El televisor se ha apagado.")

# Uso de la abstracción
tv = Televisor()
tv.encender()
tv.apagar()