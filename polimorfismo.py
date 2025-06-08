# Polimorfismo en diferentes formas de pago

class TarjetaCredito:
    def pagar(self, cantidad):
        print(f"Pagando ${cantidad} con tarjeta de crédito.")

class Efectivo:
    def pagar(self, cantidad):
        print(f"Pagando ${cantidad} en efectivo.")

class Transferencia:
    def pagar(self, cantidad):
        print(f"Pagando ${cantidad} por transferencia bancaria.")

# Función que aplica polimorfismo
def procesar_pago(metodo_pago, cantidad):
    metodo_pago.pagar(cantidad)

# Uso del polimorfismo
pagos = [TarjetaCredito(), Efectivo(), Transferencia()]
for metodo in pagos:
    procesar_pago(metodo, 50)