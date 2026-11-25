"""Funcionalidad para gestionar un carrito de compras."""

from math import isfinite


def _es_numero_finito(valor: object) -> bool:
    """Indica si el valor es un entero o decimal finito, excluyendo booleanos."""
    if isinstance(valor, bool) or not isinstance(valor, (int, float)):
        return False
    return not isinstance(valor, float) or isfinite(valor)


class CarritoCompras:
    """Almacena productos, calcula subtotales y aplica descuentos."""

    def __init__(self) -> None:
        """Inicializa un carrito vacío y sin descuento."""
        self._productos: list[tuple[str, float, int]] = []
        self._porcentaje_descuento = 0.0

    def agregar_producto(self, nombre: str, precio: float, cantidad: int) -> bool:
        """Agrega un producto válido; devuelve False si algún dato no es válido."""
        if (
            not isinstance(nombre, str)
            or not nombre.strip()
            or not _es_numero_finito(precio)
            or precio < 0
            or isinstance(cantidad, bool)
            or not isinstance(cantidad, int)
            or cantidad <= 0
        ):
            return False

        self._productos.append((nombre.strip(), precio, cantidad))
        return True

    def calcular_subtotal(self) -> float:
        """Devuelve la suma de los precios por sus cantidades."""
        return sum(
            precio_unitario * cantidad
            for _, precio_unitario, cantidad in self._productos
        )

    def aplicar_descuento(self, porcentaje: float) -> bool:
        """Aplica un descuento entre 0% y 50%; rechaza valores fuera del rango."""
        if (
            not _es_numero_finito(porcentaje)
            or porcentaje < 0
            or porcentaje > 50
        ):
            return False

        self._porcentaje_descuento = porcentaje
        return True

    def calcular_total(self) -> float:
        """Devuelve el subtotal después de aplicar el descuento vigente."""
        subtotal = self.calcular_subtotal()
        factor_descuento = 1 - self._porcentaje_descuento / 100
        return subtotal * factor_descuento