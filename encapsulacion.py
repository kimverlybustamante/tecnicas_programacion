# Clase con encapsulación para una cuenta de usuario
class Usuario:
    def _init_(self, usuario, contraseña):
        self.__usuario = usuario
        self.__contraseña = contraseña  # Atributo privado

    def cambiar_contraseña(self, antigua, nueva):
        if antigua == self.__contraseña:
            self.__contraseña = nueva
            print("Contraseña actualizada correctamente.")
        else:
            print("Contraseña incorrecta.")

    def mostrar_usuario(self):
        print(f"Usuario: {self.__usuario}")

# Uso de la encapsulación
u = Usuario("juan99", "1234")
u.mostrar_usuario()
u.cambiar_contraseña("0000", "abcd")  # Incorrecto
u.cambiar_contraseña("1234", "abcd")  # Correcto