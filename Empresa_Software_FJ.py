"""
=========================================================
PROYECTO: SISTEMA INTEGRAL DE GESTIÓN DE CLIENTES,
SERVICIOS Y RESERVAS PARA LA EMPRESA SOFTWARE FJ
=========================================================

Este documento servirá como guía general para la distribución de responsabilidades y desarrollo
del proyecto.

El sistema permitirá gestionar clientes, servicios y reservas sin utilizar bases de datos,
implementando Programación Orientada a Objetos, manejo avanzado de excepciones y registro de eventos.
"""
"""
=========================================================
INICIO DE LAS SIMULACIONES DEL SISTEMA
=========================================================

A continuación se ejecutarán diferentes operaciones
para demostrar el correcto funcionamiento de la
aplicación ante escenarios válidos e inválidos.

Estas simulaciones permitirán verificar:

1. Registro de clientes.
2. Validación de datos.
3. Creación de servicios.
4. Procesamiento de reservas.
5. Manejo de excepciones.
6. Registro de eventos en logs.
7. Continuidad del sistema ante errores.

La guía exige un mínimo de 10 operaciones,
incluyendo casos exitosos y fallidos.
"""

"""
=========================================================
BLOQUE 1 - GESTIÓN DE CLIENTES
=========================================================

En este módulo se implementará la estructura base del sistema mediante una clase abstracta llamada
Entidad, la cual servirá como modelo general para las entidades del proyecto.
Posteriormente se desarrollará la clase Cliente, encargada de administrar los datos personales
de los usuarios registrados.

Este bloque permite aplicar los principios de:

• Abstracción
• Herencia
• Encapsulación
"""
# =========================================================
# BLOQUE 1 - GESTIÓN DE CLIENTES
# =========================================================

from abc import ABC, abstractmethod
import logging
import re

# =========================================================
# CONFIGURACIÓN DEL SISTEMA DE LOGS
# =========================================================

logging.basicConfig(
    filename="software_fj.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# =========================================================
# EXCEPCIONES PERSONALIZADAS
# =========================================================

class ErrorCliente(Exception):
    """Clase base para errores relacionados con clientes."""
    pass


class NombreInvalidoError(ErrorCliente):
    """Se genera cuando el nombre es inválido."""
    pass


class DocumentoInvalidoError(ErrorCliente):
    """Se genera cuando el documento es inválido."""
    pass


class CorreoInvalidoError(ErrorCliente):
    """Se genera cuando el correo es inválido."""
    pass


class TelefonoInvalidoError(ErrorCliente):
    """Se genera cuando el teléfono es inválido."""
    pass


# =========================================================
# CLASE ABSTRACTA ENTIDAD
# =========================================================

class Entidad(ABC):
    """
    Clase abstracta que representa una entidad general
    dentro del sistema.
    """

    def __init__(self, identificacion):
        self._identificacion = identificacion

    @abstractmethod
    def mostrar_informacion(self):
        """Método abstracto que será implementado por las clases hijas."""
        pass


# =========================================================
# CLASE CLIENTE
# =========================================================

class Cliente(Entidad):
    """
    Clase encargada de gestionar la información
    de los clientes registrados.
    """

    def __init__(self, identificacion, nombre, correo, telefono):

        super().__init__(identificacion)

        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

        logging.info(f"Cliente creado correctamente: {nombre}")

    # =====================================================
    # VALIDACIONES Y ENCAPSULAMIENTO
    # =====================================================

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):

        if not valor.strip():
            raise NombreInvalidoError(
                "El nombre no puede estar vacío."
            )

        self._nombre = valor

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):

        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        if not re.match(patron, valor):
            raise CorreoInvalidoError(
                "Formato de correo inválido."
            )

        self._correo = valor

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):

        if not valor.isdigit():
            raise TelefonoInvalidoError(
                "El teléfono debe contener solo números."
            )

        self._telefono = valor

    @property
    def identificacion(self):
        return self._identificacion

    # =====================================================
    # MÉTODO SOBRESCRITO
    # =====================================================

    def mostrar_informacion(self):
        print("\n===== INFORMACIÓN DEL CLIENTE =====")
        print(f"Documento: {self.identificacion}")
        print(f"Nombre: {self.nombre}")
        print(f"Correo: {self.correo}")
        print(f"Teléfono: {self.telefono}")


# =========================================================
# SIMULACIONES DEL BLOQUE 1
# =========================================================

print("\n=================================================")
print("SIMULACIONES - GESTIÓN DE CLIENTES")
print("=================================================\n")

# OPERACIÓN 1
try:
    cliente1 = Cliente(
        "1001",
        "Yuliana Giraldo",
        "yuliana@gmail.com",
        "3001234567"
    )
    cliente1.mostrar_informacion()

except Exception as e:
    logging.error(e)
    print(e)

# OPERACIÓN 2
try:
    cliente2 = Cliente(
        "1002",
        "",
        "cliente@gmail.com",
        "3111111111"
    )

except Exception as e:
    logging.error(e)
    print("Error:", e)

# OPERACIÓN 3
try:
    cliente3 = Cliente(
        "1003",
        "Carlos Lopez",
        "correo_incorrecto",
        "3201234567"
    )

except Exception as e:
    logging.error(e)
    print("Error:", e)

# OPERACIÓN 4
try:
    cliente4 = Cliente(
        "1004",
        "Diana Rojas",
        "diana@gmail.com",
        "telefono"
    )

except Exception as e:
    logging.error(e)
    print("Error:", e)

# OPERACIÓN 5
try:
    cliente5 = Cliente(
        "1005",
        "Juan Pérez",
        "juan@gmail.com",
        "3155555555"
    )

    cliente5.mostrar_informacion()

except Exception as e:
    logging.error(e)
    print("Error:", e)

finally:
    print("\nFinalización de pruebas del bloque 1.")
"""
=========================================================
BLOQUE 2 - GESTIÓN DE SERVICIOS
=========================================================

En este módulo se desarrollarán los diferentes servicios ofrecidos por la empresa Software FJ.

La implementación incluye una clase abstracta Servicio y tres clases especializadas derivadas:

• ReservaSala
• AlquilerEquipo
• AsesoriaEspecializada

Cada clase implementará sus propios cálculos de costos y validaciones, permitiendo demostrar
el uso de herencia, polimorfismo y métodos sobrescritos dentro del proyecto.
"""
"""
=========================================================
BLOQUE 3 - GESTIÓN DE RESERVAS Y CONTROL DE ERRORES
=========================================================

En este módulo se implementará la administración de reservas dentro del sistema Software FJ.
También se desarrollará el manejo avanzado de excepciones solicitado en la guía, incluyendo:

• Excepciones personalizadas.
• Estructuras try/except.
• try/except/else.
• try/except/finally.
• Encadenamiento de excepciones.
• Registro de errores en archivo de logs.

El objetivo es garantizar que la aplicación continúe funcionando incluso cuando ocurran
errores durante su ejecución.
"""