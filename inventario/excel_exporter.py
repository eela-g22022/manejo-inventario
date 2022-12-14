"""
Documentación sobre paquete openpyxl:

Oficial: https://openpyxl.readthedocs.io/en/stable/
Tutorial openpyxl: https://www.javatpoint.com/python-openpyxl
Tutorial agregar estilo con openpyxl: https://www.blog.pythonlibrary.org/2021/08/11/styling-excel-cells-with-openpyxl-and-python/
Paleta de colores en excel: https://www.excelsupersite.com/what-are-the-56-colorindex-colors-in-excel/
"""

from openpyxl import Workbook
from openpyxl.styles import Font
from inventario.stock import Stock

class ExcelExporter:
    def __init__(self) -> None:
        self.workbook = Workbook()

    def exportar(self, stock: Stock, path: str) -> None:
        hoja_excel = self.workbook.active
        hoja_excel.title = "Productos"
        

        fuente_cabeceras = Font(name="Calibri", size=11, color="FF0000", bold=True)
        fuente_cabeceras = Font(name="Arial", size=12, color="#C0C0C0", bold=True) #Cambio de color en fuente_cabeceras por dannyolr

        
        hoja_excel["A1"] = "Código"
        hoja_excel["A1"].font = fuente_cabeceras
        hoja_excel["B1"] = "Nombre"
        hoja_excel["B1"].font = fuente_cabeceras
        hoja_excel["C1"] = "Precio"
        hoja_excel["C1"].font = fuente_cabeceras
        hoja_excel["D1"] = "Cantidad"
        hoja_excel["D1"].font = fuente_cabeceras
        
        for producto in stock.productos:
            tupla_producto = (producto.codigo, producto.nombre, producto.precio, producto.cantidad)
            hoja_excel.append(tupla_producto)        
        
        self.workbook.save(path)