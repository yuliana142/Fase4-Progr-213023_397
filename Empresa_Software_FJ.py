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
    format="%(asctime)s - %(levelname)s - %(message)s")

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
            raise NombreInvalidoError("El nombre no puede estar vacío." )

        self._nombre = valor

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):

        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        if not re.match(patron, valor):
            raise CorreoInvalidoError("Formato de correo inválido.")

        self._correo = valor

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):

        if not valor.isdigit():
            raise TelefonoInvalidoError( "El teléfono debe contener solo números.")

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
        "3001234567")
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
        "3111111111")

except Exception as e:
    logging.error(e)
    print("Error:", e)

# OPERACIÓN 3
try:
    cliente3 = Cliente(
        "1003",
        "Carlos Lopez",
        "correo_incorrecto",
        "3201234567")

except Exception as e:
    logging.error(e)
    print("Error:", e)

# OPERACIÓN 4
try:
    cliente4 = Cliente(
        "1004",
        "Diana Rojas",
        "diana@gmail.com",
        "telefono")

except Exception as e:
    logging.error(e)
    print("Error:", e)

# OPERACIÓN 5
try:
    cliente5 = Cliente(
        "1005",
        "Juan Pérez",
        "juan@gmail.com",
        "3155555555")

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

# =========================================================
# BLOQUE 2 - GESTION DE SERVICIOS
# Intregrante 2 luiza Jhynnet torres delgado
# =========================================================

class ErrorServicio(Exception):
    """Clase base para errores relacionados con servicios."""
    pass


class CostoInvalidoError(ErrorServicio):
    """Error cuando el costo del servicio no es valido."""
    pass


class DuracionInvalidaError(ErrorServicio):
    """Error cuando la duracion no es valida."""
    pass



class Servicio(ABC):
    """Clase abstracta que representa los servicios ofrecidos por la empresa Software FJ."""

    def __init__(self, codigo, nombre, costo_base):
        if not codigo or not codigo.strip():
            raise ErrorServicio("El codigo del servicio es obligatorio.")

        if not nombre or not nombre.strip():
            raise ErrorServicio("El nombre del servicio es obligatorio.")

        if not isinstance(costo_base, (int, float)) or isinstance(costo_base, bool) or costo_base <= 0:
            raise CostoInvalidoError("El costo debe ser mayor que cero.")

        self._codigo = codigo
        self._nombre = nombre
        self._costo_base = costo_base

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @property
    def costo_base(self):
        return self._costo_base

    @abstractmethod
    def calcular_costo(self, cantidad):
        pass

    def mostrar_informacion(self):
        print(f"Codigo: {self.codigo}")
        print(f"Servicio: {self.nombre}")
        print(f"Costo base: ${self.costo_base:,.2f}")


# =========================================================
# SERVICIO 1 - RESERVA DE SALAS
# =========================================================

class ReservaSala(Servicio):

    def __init__(self, codigo, nombre, costo_base):
        super().__init__(codigo, nombre, costo_base)

    def calcular_costo(self, horas):
        if not isinstance(horas, (int, float)) or isinstance(horas, bool) or horas <= 0:
            raise DuracionInvalidaError(
                "Las horas de reserva deben ser mayores que cero."
            )

        return self.costo_base * horas


# =========================================================
# SERVICIO 2 - ALQUILER DE EQUIPOS
# =========================================================

class AlquilerEquipo(Servicio):

    def __init__(self, codigo, nombre, costo_base):
        super().__init__(codigo, nombre, costo_base)

    def calcular_costo(self, dias):
        if not isinstance(dias, (int, float)) or isinstance(dias, bool) or dias <= 0:
            raise DuracionInvalidaError(
                "Los dias de alquiler deben ser mayores que cero."
            )

        return self.costo_base * dias


# =========================================================
# SERVICIO 3 - ASESORIA ESPECIALIZADA
# =========================================================

class AsesoriaEspecializada(Servicio):

    def __init__(self, codigo, nombre, costo_base):
        super().__init__(codigo, nombre, costo_base)

    def calcular_costo(self, horas):
        if not isinstance(horas, (int, float)) or isinstance(horas, bool) or horas <= 0:
            raise DuracionInvalidaError(
                "Las horas de asesoria deben ser mayores que cero."
            )

        return self.costo_base * horas


# =========================================================
# SIMULACIONES DEL BLOQUE 2
# =========================================================

print("\n==============================================")
print("SIMULACIONES - GESTION DE SERVICIOS")
print("==============================================")

# OPERACION 6 - Reserva de sala exitosa
try:
    sala = ReservaSala("S001", "Sala de reuniones", 50000)
    costo = sala.calcular_costo(3)

    sala.mostrar_informacion()
    print(f"Costo por 3 horas: ${costo:,.2f}")

    logging.info("Reserva de sala simulada correctamente.")

except ErrorServicio as e:
    logging.error(f"Error en reserva de sala: {e}")
    print("Error:", e)


# OPERACION 7 - Alquiler de equipo exitoso
try:
    equipo = AlquilerEquipo("E001", "Proyector", 30000)
    costo = equipo.calcular_costo(2)

    equipo.mostrar_informacion()
    print(f"Costo por 2 dias: ${costo:,.2f}")

    logging.info("Alquiler de equipo simulado correctamente.")

except ErrorServicio as e:
    logging.error(f"Error en alquiler: {e}")
    print("Error:", e)


# OPERACION 8 - Asesoria especializada exitosa
try:
    asesoria = AsesoriaEspecializada(
        "A001", "Asesoria de software", 80000
    )

    costo = asesoria.calcular_costo(2)

    asesoria.mostrar_informacion()
    print(f"Costo por 2 horas: ${costo:,.2f}")

    logging.info("Asesoria simulada correctamente.")

except ErrorServicio as e:
    logging.error(f"Error en asesoria: {e}")
    print("Error:", e)


# OPERACION 9 - Duracion invalida
try:
    sala.calcular_costo(0)

except DuracionInvalidaError as e:
    logging.error(f"Duracion invalida: {e}")
    print("Error:", e)


# OPERACION 10 - Costo base invalido
try:
    servicio_invalido = ReservaSala(
        "S002", "Sala de capacitacion", -50000
    )

except CostoInvalidoError as e:
    logging.error(f"Costo invalido: {e}")
    print("Error:", e)


print("\nFinalizacion de pruebas del bloque 2.")

"""=========================================================
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

"""
=========================================================
SOFTWARE FJ
BLOQUE 3 - GESTION DE RESERVAS Y CONTROL DE ERRORES
INTEGRANTE 3
=========================================================

Este módulo administra las reservas y controla los errores
del sistema mediante excepciones personalizadas y logs.

No utiliza bases de datos ni librerías externas.
"""
import logging


# =========================================================
# 1. CONFIGURACION DE LOGS
# =========================================================

logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    encoding="utf-8"
)


def registrar_evento(mensaje):
    logging.info(mensaje)


def registrar_error(mensaje):
    logging.exception(mensaje)


# =========================================================
# 2. EXCEPCIONES PERSONALIZADAS
# =========================================================

class ErrorSoftwareFJ(Exception):
    pass


class DatosInvalidosError(ErrorSoftwareFJ):
    pass


class RegistroDuplicadoError(ErrorSoftwareFJ):
    pass


class RegistroNoEncontradoError(ErrorSoftwareFJ):
    pass


class ServicioNoDisponibleError(ErrorSoftwareFJ):
    pass


class ReservaInvalidaError(ErrorSoftwareFJ):
    pass


class OperacionNoPermitidaError(ErrorSoftwareFJ):
    pass


# =========================================================
# 3. FUNCIONES DE COMPATIBILIDAD CON OTROS MODULOS
# =========================================================

def obtener_id(objeto):
    identificador = getattr(objeto, "id", None)

    if identificador is None:
        identificador = getattr(objeto, "identificador", None)

    if identificador is None:
        raise DatosInvalidosError("El objeto no tiene identificador.")

    return str(identificador).strip()


def validar_servicio(servicio, detalle):

    if hasattr(servicio, "validar"):
        servicio.validar(detalle)

    elif hasattr(servicio, "validar_parametros"):

        if isinstance(detalle, dict):
            parametros = detalle

        elif hasattr(servicio, "capacidad"):
            parametros = {"personas": detalle}

        elif hasattr(servicio, "existencias") or hasattr(servicio, "cantidad"):
            parametros = {"cantidad": detalle}

        else:
            parametros = {"tema": str(detalle)}

        servicio.validar_parametros(parametros)

    else:
        raise DatosInvalidosError(
            "El servicio no tiene un método de validación."
        )


# =========================================================
# 4. CLASE RESERVA
# =========================================================

class Reserva:

    def __init__(self, identificador, cliente, servicio, horas, detalle):

        try:
            if not identificador:
                raise DatosInvalidosError(
                    "El identificador es obligatorio."
                )

            if cliente is None or servicio is None:
                raise DatosInvalidosError(
                    "Debe seleccionar un cliente y un servicio."
                )

            self.id = str(identificador).strip()
            self.horas = float(horas)

            if self.horas <= 0:
                raise ReservaInvalidaError(
                    "La duración debe ser mayor que cero."
                )

            validar_servicio(servicio, detalle)

            self.cliente = cliente
            self.servicio = servicio
            self.estado = "Pendiente"
            self.costo = None

            registrar_evento(
                f"Reserva {self.id} creada correctamente."
            )

        except (ValueError, TypeError) as error:
            registrar_error("Error en los datos de la reserva.")

            raise ReservaInvalidaError(
                "No se pudo crear la reserva."
            ) from error

        except ErrorSoftwareFJ:
            registrar_error("Error controlado al crear reserva.")
            raise

    # -----------------------------------------------------
    # CONFIRMAR RESERVA
    # -----------------------------------------------------

    def confirmar(self):

        if self.estado != "Pendiente":
            raise ReservaInvalidaError(
                "Solo se pueden confirmar reservas pendientes."
            )

        if not getattr(self.servicio, "disponible", True):
            raise ServicioNoDisponibleError(
                "El servicio no está disponible."
            )

        self.estado = "Confirmada"

        registrar_evento(
            f"Reserva {self.id} confirmada."
        )

        return "Reserva confirmada correctamente."

    # -----------------------------------------------------
    # CANCELAR RESERVA
    # -----------------------------------------------------

    def cancelar(self):

        if self.estado in ("Cancelada", "Procesada"):
            raise OperacionNoPermitidaError(
                "No se puede cancelar esta reserva."
            )

        self.estado = "Cancelada"

        registrar_evento(
            f"Reserva {self.id} cancelada."
        )

        return "Reserva cancelada correctamente."

    # -----------------------------------------------------
    # PROCESAR RESERVA Y CALCULAR COSTO
    # -----------------------------------------------------

    def procesar(self, impuesto=0.19, descuento=0):

        if self.estado != "Confirmada":
            raise ReservaInvalidaError(
                "Primero debe confirmar la reserva."
            )

        try:

            self.costo = self.servicio.calcular_costo(
                self.horas, impuesto, descuento
            )

            self.estado = "Procesada"

        except (ValueError, TypeError) as error:

            registrar_error("Error durante el cálculo del costo.")

            raise ReservaInvalidaError(
                "No fue posible calcular el costo."
            ) from error

        except ErrorSoftwareFJ:

            registrar_error("Error al procesar la reserva.")
            raise

        else:

            registrar_evento(
                f"Reserva {self.id} procesada. Total: {self.costo}"
            )

            return self.costo

        finally:

            registrar_evento(
                f"Finalizó el procesamiento de la reserva {self.id}."
            )

    # -----------------------------------------------------
    # DESCRIPCION DE RESERVA
    # -----------------------------------------------------

    def describir(self):

        nombre_cliente = getattr(
            self.cliente, "nombre", "Sin nombre"
        )

        nombre_servicio = getattr(
            self.servicio, "nombre", "Sin servicio"
        )

        return (
            f"Reserva: {self.id} | "
            f"Cliente: {nombre_cliente} | "
            f"Servicio: {nombre_servicio} | "
            f"Horas: {self.horas} | "
            f"Estado: {self.estado} | "
            f"Costo: {self.costo}"
        )


# =========================================================
# 5. ADMINISTRADOR DE RESERVAS
# =========================================================

class SistemaSoftwareFJ:

    def __init__(self):

        self.clientes = []
        self.servicios = []
        self.reservas = []

    def registrar_cliente(self, cliente):

        self._registrar(
            self.clientes, cliente, "cliente"
        )

    def registrar_servicio(self, servicio):

        self._registrar(
            self.servicios, servicio, "servicio"
        )

    def _registrar(self, lista, objeto, tipo):

        identificador = obtener_id(objeto)

        if any(obtener_id(x) == identificador for x in lista):

            raise RegistroDuplicadoError(
                f"El {tipo} ya está registrado."
            )

        lista.append(objeto)

        registrar_evento(
            f"{tipo.capitalize()} registrado: {identificador}"
        )

    def buscar(self, lista, identificador):

        for objeto in lista:

            if obtener_id(objeto) == str(identificador).strip():
                return objeto

        registrar_evento(
            f"Registro no encontrado: {identificador}"
        )

        raise RegistroNoEncontradoError(
            "No se encontró el registro solicitado."
        )

    # -----------------------------------------------------
    # CREAR RESERVA
    # -----------------------------------------------------

    def crear_reserva(
        self,
        id_reserva,
        id_cliente,
        id_servicio,
        horas,
        detalle
    ):

        try:

            if any(
                obtener_id(r) == str(id_reserva).strip()
                for r in self.reservas
            ):

                raise RegistroDuplicadoError(
                    "La reserva ya existe."
                )

            cliente = self.buscar(
                self.clientes, id_cliente
            )

            servicio = self.buscar(
                self.servicios, id_servicio
            )

            reserva = Reserva(
                id_reserva,
                cliente,
                servicio,
                horas,
                detalle
            )

        except ErrorSoftwareFJ:

            registrar_error("Error al crear una reserva.")
            raise

        else:

            self.reservas.append(reserva)

            registrar_evento(
                f"Reserva agregada al sistema: {id_reserva}"
            )

            return reserva

        finally:

            registrar_evento(
                f"Finalizó intento de creación de reserva: {id_reserva}"
            )

    # -----------------------------------------------------
    # BUSCAR RESERVA
    # -----------------------------------------------------

    def buscar_reserva(self, identificador):

        return self.buscar(
            self.reservas, identificador
        )


# =========================================================
# 6. OBJETOS DE PRUEBA
# =========================================================

# Estos objetos permiten probar este bloque sin modificar
# las clases Cliente y Servicio de los otros integrantes.

class ClientePrueba:

    def __init__(self, identificador, nombre):

        self.id = identificador
        self.nombre = nombre


class ServicioPrueba:

    def __init__(self, identificador, nombre, tarifa, capacidad):

        self.id = identificador
        self.nombre = nombre
        self.tarifa = float(tarifa)
        self.capacidad = int(capacidad)
        self.disponible = True

    def validar(self, detalle):

        personas = int(detalle)

        if not 1 <= personas <= self.capacidad:
            raise DatosInvalidosError(
                "La capacidad del servicio fue excedida."
            )

    def calcular_costo(self, horas, impuesto=0, descuento=0):

        if not self.disponible:
            raise ServicioNoDisponibleError(
                "Servicio no disponible."
            )

        horas = float(horas)
        impuesto = float(impuesto)
        descuento = float(descuento)

        if horas <= 0:
            raise DatosInvalidosError("Horas inválidas.")

        if not 0 <= impuesto <= 1:
            raise DatosInvalidosError("Impuesto inválido.")

        if not 0 <= descuento <= 1:
            raise DatosInvalidosError("Descuento inválido.")

        return round(
            self.tarifa * horas * (1 - descuento) * (1 + impuesto),
            2
        )


# =========================================================
# 7. PRUEBAS AUTOMATICAS
# =========================================================

def ejecutar_pruebas():

    sistema = SistemaSoftwareFJ()

    correctas = 0
    fallidas = 0

    cliente = ClientePrueba("C001", "Laura Gómez")
    cliente2 = ClientePrueba("C002", "Carlos Pérez")

    sala = ServicioPrueba(
        "S001", "Sala principal", 50000, 12
    )

    equipo = ServicioPrueba(
        "S002", "Proyector", 25000, 5
    )

    asesoria = ServicioPrueba(
        "S003", "Asesoría informática", 80000, 10
    )

    def probar(nombre, accion, error_esperado=None):

        nonlocal correctas, fallidas

        try:

            accion()

        except Exception as error:

            if (
                error_esperado is not None
                and isinstance(error, error_esperado)
            ):

                correctas += 1
                print(nombre, "- ERROR CONTROLADO")

            else:

                fallidas += 1
                print(nombre, "- FALLÓ:", error)

                registrar_error(
                    f"Prueba fallida: {nombre}"
                )

        else:

            if error_esperado is not None:

                fallidas += 1
                print(nombre, "- DEBIÓ GENERAR ERROR")

            else:

                correctas += 1
                print(nombre, "- CORRECTO")

        finally:

            registrar_evento(
                f"Finalizó prueba: {nombre}"
            )

    print("\n========== PRUEBAS SOFTWARE FJ ==========\n")

    # 1
    probar(
        "Registrar primer cliente",
        lambda: sistema.registrar_cliente(cliente)
    )

    # 2
    probar(
        "Registrar segundo cliente",
        lambda: sistema.registrar_cliente(cliente2)
    )

    # 3
    probar(
        "Registrar sala",
        lambda: sistema.registrar_servicio(sala)
    )

    # 4
    probar(
        "Registrar equipo",
        lambda: sistema.registrar_servicio(equipo)
    )

    # 5
    probar(
        "Registrar asesoría",
        lambda: sistema.registrar_servicio(asesoria)
    )

    # 6
    probar(
        "Rechazar cliente duplicado",
        lambda: sistema.registrar_cliente(cliente),
        RegistroDuplicadoError
    )

    # 7
    probar(
        "Rechazar servicio duplicado",
        lambda: sistema.registrar_servicio(sala),
        RegistroDuplicadoError
    )

    # 8
    probar(
        "Crear reserva válida",
        lambda: sistema.crear_reserva(
            "R001", "C001", "S001", 2, 8
        )
    )

    # 9
    probar(
        "Rechazar duración negativa",
        lambda: sistema.crear_reserva(
            "R002", "C001", "S001", -2, 3
        ),
        ReservaInvalidaError
    )

    # 10
    probar(
        "Rechazar cliente inexistente",
        lambda: sistema.crear_reserva(
            "R003", "C999", "S001", 1, 2
        ),
        RegistroNoEncontradoError
    )

    # 11
    probar(
        "Rechazar exceso de capacidad",
        lambda: sistema.crear_reserva(
            "R004", "C001", "S001", 1, 20
        ),
        DatosInvalidosError
    )

    # 12
    probar(
        "Confirmar reserva",
        lambda: sistema.buscar_reserva("R001").confirmar()
    )

    # 13
    probar(
        "Procesar reserva y calcular costo",
        lambda: sistema.buscar_reserva("R001").procesar(
            0.19, 0.10
        )
    )

    # 14
    probar(
        "Rechazar cancelación de reserva procesada",
        lambda: sistema.buscar_reserva("R001").cancelar(),
        OperacionNoPermitidaError
    )

    # 15
    probar(
        "Rechazar reserva duplicada",
        lambda: sistema.crear_reserva(
            "R001", "C001", "S001", 1, 5
        ),
        RegistroDuplicadoError
    )

    # 16
    reserva2 = sistema.crear_reserva(
        "R005", "C002", "S003", 1, 5
    )

    asesoria.disponible = False

    probar(
        "Rechazar servicio no disponible",
        reserva2.confirmar,
        ServicioNoDisponibleError
    )

    asesoria.disponible = True

    print("\n========== RESULTADOS ==========")

    print("Pruebas correctas:", correctas)
    print("Pruebas fallidas:", fallidas)
    print("Total:", correctas + fallidas)

    registrar_evento(
        f"Finalizaron las pruebas: {correctas} correctas, "
        f"{fallidas} fallidas."
    )


# =========================================================
# 8. EJECUCION PRINCIPAL
# =========================================================

if __name__ == "__main__":

    print("=" * 55)
    print("SOFTWARE FJ - INTEGRANTE 3")
    print("GESTION DE RESERVAS Y CONTROL DE ERRORES")
    print("=" * 55)

    ejecutar_pruebas()

    print("\nArchivo de eventos creado: logs.txt")
    print("Fin de las pruebas del Integrante 3.")
