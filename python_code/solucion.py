"""
Single responsability
Open closed
Liskov substitution
Interface segregation
Dependency inversion
"""

from abc import ABC, abstractmethod

class Parseador:
    pass
    def __init__(self, encabezado: list):
        self.fecha = encabezado[0]
        self.total = encabezado[1]
        
    def get_fecha(self):
        print("get fecha")
            
class Formateador(ABC):
    
    @abstractmethod
    def formatea(self, parseador: Parseador) -> None:
        pass
    
class Formateador_SUM(Formateador):
    @abstractmethod
    def suma_valores(self, valores: list) -> None:
        pass
      
class CandyglobalFormatedor(Formateador_SUM):
    
    def __init__(self, porcentaje_iva: int):
        self.porcentaje_iva = porcentaje_iva
        
    def suma_valores(self, valores: list) -> None:
        print("suma = ",sum(valores))
    
    def formatea(self, parseador: Parseador) -> None:
        print("salida Candyglobal") 
        print(f"fecha: {parseador.fecha}, iva: {self.porcentaje_iva}, total: {parseador.total}")

class DistrijasFormatedor(Formateador):
    def __init__(self, porcentaje_iva: int):
        self.porcentaje_iva = porcentaje_iva
        
    def formatea(self, parseador: Parseador) -> None:
        print("salida Distrijas")
        print(f"fecha: {parseador.fecha}, iva: {self.porcentaje_iva}, total: {parseador.total}")
        
class RompoyFormatedor(Formateador_SUM):
    
    def __init__(self, valor_iva: float):
        self.valor_iva = valor_iva 
        
    def suma_valores(self, valores: list) -> None:
        print("suma = ",sum(valores))
        
    def formatea(self, parseador: Parseador) -> None:
        print("salida Rompoy")
        print(f"fecha: {parseador.fecha}, iva: {self.valor_iva}, total: {parseador.total}")
        
class LaTorreFormateador(Formateador_SUM):
    def __init__(self, valor_iva: float):
        self.valor_iva = valor_iva 
        
    def suma_valores(self, valores: list) -> None:
        print("suma = ",sum(valores))
    
    def formatea(self, parseador: Parseador) -> None:
        print("salida La Torre")
        print(f"fecha: {parseador.fecha}, iva: {self.valor_iva}, total: {parseador.total}")

def main():
    parsear = Parseador(["2022/02/01", "10.000"])
    
    formateador_distrijas = DistrijasFormatedor(19)
    formateador_distrijas.formatea(parsear)
    
    formateador_rompoy = RompoyFormatedor(20000.0)
    formateador_rompoy.formatea(parsear)

    formateador_torre = LaTorreFormateador(19000.0)
    formateador_torre.formatea(parsear)
    
if __name__ == '__main__':
    main()
    