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
    
class Verificador(ABC):
    @abstractmethod
    def salida_verificada(self):
        pass

class TotalVerificador(Verificador):
    def suma_valores(self, valores: list) -> None:
        print("suma = ",sum(valores))
        
    def salida_verificada(self):
        print("salida esta ok")

class CandyglobalFormatedor(Formateador):
    
    def __init__(self, porcentaje_iva: int, verificador: Verificador):
        self.porcentaje_iva = porcentaje_iva
        self.verificador = verificador      
    
    def formatea(self, parseador: Parseador) -> None:
        print("salida Candyglobal") 
        print(f"fecha: {parseador.fecha}, iva: {self.porcentaje_iva}, total: {parseador.total}")
        self.verificador.suma_valores([1,2,3])
        self.verificador.salida_verificada()

class DistrijasFormatedor(Formateador):
    
    def __init__(self, porcentaje_iva: int):
        self.porcentaje_iva = porcentaje_iva
        
    def formatea(self, parseador: Parseador) -> None:
        print("salida Distrijas")
        print(f"fecha: {parseador.fecha}, iva: {self.porcentaje_iva}, total: {parseador.total}")
        
class RompoyFormatedor(Formateador):
    
    def __init__(self, valor_iva: float, verificador: Verificador):
        self.valor_iva = valor_iva 
        self.verificador = verificador
        
    def formatea(self, parseador: Parseador) -> None:
        print("salida Rompoy")
        print(f"fecha: {parseador.fecha}, iva: {self.valor_iva}, total: {parseador.total}")
        self.verificador.suma_valores([1,2,3])
        self.verificador.salida_verificada()
        

def main():
    parsear = Parseador(["2022/02/01", "10.000"])
    verificador = TotalVerificador()
    
    formateador_distrijas = DistrijasFormatedor(19)
    formateador_distrijas.formatea(parsear)
    
    formateador_rompoy = RompoyFormatedor(20000.0, verificador)
    formateador_rompoy.formatea(parsear)
if __name__ == '__main__':
    main()
