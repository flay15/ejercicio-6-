# Clase Vehículo con encapsulamiento
import datetime

class Vehiculo:
    def __init__(self, marca, año):
        self.__marca = marca
        self.__anio = año
    
    # Getter para marca
    def obtener_marca(self):
        return self.__marca
    
    # Setter para marca
    def establecer_marca(self, marca):
        self.__marca = marca
    
    # Getter para año
    def obtener_anio(self):
        return self.__anio
    
    # Setter para año con validación
    def establecer_anio(self, anio):
        anio_actual = datetime.datetime.now().year
        if anio <= anio_actual:
            self.__anio = anio
        else:
            print("El año no puede ser mayor al año actual.")

# Ejemplo de uso
vehiculo = Vehiculo("Toyota", 2015)
print(vehiculo.obtener_marca())
print(vehiculo.obtener_anio())

vehiculo.establecer_anio(2025)  # Intento de establecer un año futuro
