from carrito import CarritoCompras


def test_agregar_producto():
    carrito = CarritoCompras()
    carrito.agregar_producto("Teclado", 25000, 2)

    assert carrito.calcular_subtotal() == 50000


def test_no_agregar_producto_con_precio_negativo():
    carrito = CarritoCompras()
    carrito.agregar_producto("Teclado", -25000, 1)

    assert carrito.calcular_subtotal() == 0


def test_no_agregar_producto_con_cantidad_cero():
    carrito = CarritoCompras()
    carrito.agregar_producto("Teclado", 25000, 0)

    assert carrito.calcular_subtotal() == 0


def test_aplicar_descuento_del_diez_por_ciento():
    carrito = CarritoCompras()
    carrito.agregar_producto("Teclado", 25000, 2)
    carrito.aplicar_descuento(10)

    assert carrito.calcular_total() == 45000


def test_no_aplicar_descuento_superior_al_cincuenta_por_ciento():
    carrito = CarritoCompras()
    carrito.agregar_producto("Teclado", 25000, 2)
    carrito.aplicar_descuento(51)

    assert carrito.calcular_total() == 50000


def test_carrito_vacio_tiene_total_cero():
    carrito = CarritoCompras()

    assert carrito.calcular_total() == 0