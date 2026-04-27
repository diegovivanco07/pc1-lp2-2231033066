class Pasajero:

    RUTAS_VALIDAS = ["Iquitos-Nauta", "Iquitos-Yurimaguas",
                     "Iquitos-Pucallpa", "Iquitos-Sta. Rosa"]

    def __init__(self, dni, nombre_completo, edad, peso_equipaje, ruta):
        self.dni = dni
        self.nombre_completo = nombre_completo
        self.edad = edad
        self.peso_equipaje = peso_equipaje
        self.ruta = ruta

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, valor):
        if len(valor) != 8 or not valor.isdigit():
            raise ValueError("DNI inválido")
        self.__dni = valor

    @property
    def nombre_completo(self):
        return self.__nombre_completo

    @nombre_completo.setter
    def nombre_completo(self, valor):
        valor = valor.strip()
        if len(valor) < 5:
            raise ValueError("Nombre muy corto")
        self.__nombre_completo = valor.title()

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, valor):
        if valor < 0 or valor > 120:
            raise ValueError("Edad inválida")
        self.__edad = valor

    @property
    def peso_equipaje(self):
        return self.__peso_equipaje

    @peso_equipaje.setter
    def peso_equipaje(self, valor):
        if valor < 0 or valor > 25:
            raise ValueError("Peso inválido")
        self.__peso_equipaje = float(valor)

    @property
    def ruta(self):
        return self.__ruta

    @ruta.setter
    def ruta(self, valor):
        if valor not in self.RUTAS_VALIDAS:
            raise ValueError("Ruta incorrecta")
        self.__ruta = valor

    @property
    def categoria_edad(self):
        if self.edad < 12:
            return "Niño"
        elif self.edad < 18:
            return "Adolescente"
        elif self.edad < 60:
            return "Adulto"
        else:
            return "Adulto mayor"

    @property
    def tarifa_base(self):
        if self.ruta == "Iquitos-Nauta":
            return 25
        elif self.ruta == "Iquitos-Sta. Rosa":
            return 80
        elif self.ruta == "Iquitos-Yurimaguas":
            return 120
        else:
            return 180

    @property
    def recargo_equipaje(self):
        if self.peso_equipaje > 15:
            return (self.peso_equipaje - 15) * 2
        return 0

    @property
    def tarifa_total(self):
        base = self.tarifa_base

        if self.categoria_edad == "Niño" or self.categoria_edad == "Adulto mayor":
            base = base * 0.5

        return base + self.recargo_equipaje

    def __str__(self):
        return "DNI: " + self.dni + "\n" + \
               "Nombre: " + self.nombre_completo + "\n" + \
               "Edad: " + str(self.edad) + "\n" + \
               "Ruta: " + self.ruta + "\n" + \
               "Total: S/. " + str(round(self.tarifa_total, 2))


if __name__ == "__main__":
    p = Pasajero("62858589", "juan perez", 20, 18, "Iquitos-Pucallpa")
    print(p)