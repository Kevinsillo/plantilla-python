from abc import ABC, abstractmethod


class ReservasRepository(ABC):
    """
    Interfaz que define los métodos que deben implementar los repositorios de reservas
    """

    @abstractmethod
    def crear_tabla(self) -> None:
        """
        Crea la tabla de reservas
        """

    @abstractmethod
    def obtener_reservas(self) -> list:
        """
        Obtiene todas las reservas

        return: Lista con las reservas
        """

    @abstractmethod
    def guardar_reserva(self, nombre: str, fecha_inicio: str, fecha_fin: str) -> None:
        """
        Guarda una reserva

        param nombre: Nombre del cliente
        param fecha_inicio: Fecha de inicio de la reserva
        param fecha_fin: Fecha de fin de la reserva
        """
