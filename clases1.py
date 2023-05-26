class tienda:
    def init (self,id_tienda,caja):
        self.id_tienda = id_tienda
        self.caja = caja
        self.producto=[]
    
    def str (self):
        return f"{self.id_tienda} - {self.caja}"

    def calcular(self,p1):
        self.producto.append(p1)


class Producto:
    def init (self, id_productos,cant_actual,cant_minima,id_detalles):
        self.id_productos = id_productos
        self.cant_actual = cant_actual
        self.cant_minima =cant_minima
        self.id_detalles = id_detalles
        self.id_detalles=[]
    
    def str (self):
        return f"{self.id} - { self.cant_actual} - {self.cant_minima} - {self.id_detalles}"
    
    def calcular(self,deta1):
        self.id_detalles.append(deta1)


class detalle_vent:
    def init(self,id_detalle,nombre,tipos,precio,iva):
        self.id_detalle = id_detalle
        self.nombre = nombre
        self.tipos = tipos
        self.precio = precio
        self.iva = iva
        
    def str(self):
        return f"{self.id_detalle} - {self.nombre} - {self.tipos} - {self.precio} - {self.iva}"
  
    

class iva_general:
    def init (self,iva_papel,iva_super, iva_drogueria ):
        self.iva_papel=iva_papel
        self.iva_super=iva_super
        self.iva_drogueria=iva_drogueria
        

    def str (self):
         return f"{self.iva_papel} - {self.iva_super} - {self.iva_drogueria}"
    


class inventario:
    def init (self,id_inventarios,cant_prod,producto):
        self.id_iventarios=id_inventarios
        self.cant_prod=cant_prod
        self.producto=producto
        
    def str (self):
        return f" {self.id_iventarios} - {self.producto} - {self.cant_prod}"
    


class tipos_Productos:
    def init(self, papeleria, supermercado, drogueria):
        self.papeleria = papeleria
        self.supermercado = supermercado
        self.drogueria = drogueria

    def str(self):
        return f"{self.papeleria} - {self.supermercado} - {self.drogueria}"



#Agregacion
tip=tipos_Productos("papeleria","supermercado","drogueria")
impu=iva_general(1.16,1.04,1.12)

deta1 = detalle_vent(1, "pan", tip, 0.5, impu)
print("Agregacion:\n", deta1)

#Compososicion
p1=Producto(1,23,12,0)
p1.calcular(deta1)
print("\nComposicion producto:\n",p1)

tienda=tienda(1,"saldo de la cuenta")
tienda.calcular(p1)
print("\nComposicion tienda:\n",tienda)

#Agregacion
invent=inventario(1,p1,"calculo")
print("\nAgregacion Inventario:\n",invent)