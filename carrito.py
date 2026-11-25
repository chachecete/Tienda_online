class CarritoCompras:
    def __init__(self) -> None:
        self.productos: list[tuple[str, float, int]] = []
        self.descuento = 0.0

    def agregar_producto(self, nombre: str, precio: float, cantidad: int) -> bool:
        if precio < 0 or cantidad <= 0:
            return False

        self.productos.append((nombre, precio, cantidad))
        return True

    def calcular_subtotal(self) -> float:
        return sum(precio * cantidad for _, precio, cantidad in self.productos)

    def aplicar_descuento(self, porcentaje: float) -> bool:
        if porcentaje < 0 or porcentaje > 50:
            return False

        self.descuento = porcentaje
        return True

    def calcular_total(self) -> float:
        return self.calcular_subtotal() * (1 - self.descuento / 100)