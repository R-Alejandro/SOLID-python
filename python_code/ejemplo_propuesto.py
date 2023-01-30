"""Codigo FEO"""

class Parseador:
    pass
    def __init__(self, encabezado: list):
        self.fecha = encabezado[0]
        self.total = encabezado[1]
    
    def get_fecha(self):
        print(f"fecha: {self.fecha}")
        
    def formatear_archivo_salida(self, distribuidor, porcentaje_iva):
        
        if distribuidor == 'candyglobal':
            print("salida Candyglobal")
            print(f"fecha: {self.fecha}, iva: {porcentaje_iva}, total: {self.total}")
                        
        elif distribuidor == 'distrijas':
            print("salida Distrijas")
            print(f"fecha: {self.fecha}, iva: {porcentaje_iva}, total: {self.total}")
        
        else:
            raise Exception(f"distribuidor desconocido: {distribuidor}")
            


def main():
    parsear = Parseador(["2022/02/01", "10.000"])
    parsear.formatear_archivo_salida('candyglobal', 19)
    parsear.formatear_archivo_salida('distrijas', 19)

if __name__ == '__main__':
    main()