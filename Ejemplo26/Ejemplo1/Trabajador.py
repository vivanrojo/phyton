class Trabajador:
      # ATRIBUTOS O VARIABLES DE INSTANCIA DE LA CLASE
      def __init__(self, id_trabajador, nombre, apaterno, tipo_trabajador, parametros_sueldo):
          self.id_trabajador = id_trabajador
          self.nombre = nombre
          self.apaterno = apaterno 
          self.tipo_trabajador = tipo_trabajador
          self.parametros_sueldo = parametros_sueldo
 
      # MOSTRAR LOS ATRIBUTOS DEL OBJETO
      def __str__(self):
          return (self.id_trabajador + ' ' + self.nombre + ' ' + self.apaterno \
                 + ' ' + str(self.tipo_trabajador) + ' ' + self.parametros_sueldo)
       