from inventario.producto import Producto

class Stock:
    
    def __init__(self) -> None:
        self.__productos: list[Producto] = []
        
    def __comprobar_producto(self, codigo_a_buscar: str) -> bool:
        return any(codigo_a_buscar == item.codigo for item in self.__productos)    
    
    def agregar_producto(self, prod_a_agregar: Producto) -> None:
        if self.__comprobar_producto(prod_a_agregar.codigo):
            raise ValueError(f"El producto: {prod_a_agregar.codigo} ya existe")
        else:
            self.__productos.append(prod_a_agregar)
        
    def quitar_producto(self, prod_a_quitar: Producto) -> None:
        self.__productos.remove(prod_a_quitar)
    
    @property
    def productos(self) -> list[Producto]:
        return self.__productos