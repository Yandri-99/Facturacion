from Clientes import Clientes
from Producto import Producto

facturas = {}

def generar_factura(id_factura, id_cliente, productos_facturados):
    if id_cliente not in Clientes.clientes:
        print("El cliente no existe.")
        return
    
    total_factura = 0
    for p in productos_facturados:
        if p in Producto.productos and Producto.productos[p]['stock'] > 0:
            total_factura += Producto.productos[p]['precio']
            Producto.productos[p]['stock'] -= 1 
        else:
            print(f"Producto {Producto.productos[p]['nombre']} no disponible en stock.")
    
    facturas[id_factura] = {
        'cliente': Clientes.clientes[id_cliente]['nombre'],
        'productos': [Producto.productos[p]['nombre'] for p in productos_facturados],
        'total': total_factura
    }

    print('%r' % facturas)

    print(f" El cliente ingresado es: {facturas[1]['cliente']} ")
    print(f"Factura generada. Total: {total_factura} ")
    return total_factura