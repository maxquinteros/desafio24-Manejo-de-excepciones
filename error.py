class DimensionError(Exception):
    def __init__(self, mensaje, dimension = None, maximo = None):
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo
        super().__init__(self.mensaje)
        
    def __str__(self):
        if self.dimension == None and self.maximo == None:
            return (self.mensaje)
        else:
            return(f"{self.mensaje} La dimension que ingreso es {self.dimension} pero el máximo es {self.maximo}")
        