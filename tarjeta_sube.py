class NoHaySaldoException(Exception):
    pass

class UsuarioDesactivadoException(Exception):
    pass

class EstadoNoExistenteException(Exception):
    pass

PRIMARIO = "primario"
PRECIO_TICKET = 70
DESACTIVADO = "desactivado"
ACTIVADO = "activado"
SECUNDARIO = "secundario"

"""class Sube():
    def __init__(self):
        self.saldo = 0
        self.grupo_beneficiario = None
        self.estado = "activado"
    
    def obtener_precio_ticket(self):#definimos nueva función
        if self.grupo_beneficiario == PRIMARIO: #si el atributo grupo beneficiario es igual a PRIMARIO
            self.precio_ticket = PRECIO_TICKET / 2 #el precio ticket será los 70(PRECIO TICKET original) dividido 2 = 35
        else: #si no
            self.precio_ticket = PRECIO_TICKET 
        return self.precio_ticket
    
   def pagar_pasaje(self):"""
        
    





class Sube():
    def __init__(self): #iniciar atributos
        self.saldo = 0
        self.grupo_beneficiario = None
        self.estado = "activado"

    def obtener_precio_ticket(self): #definir función
        if self.grupo_beneficiario == PRIMARIO:
            self.precio_ticket = PRECIO_TICKET / 2
        else:
            self.precio_ticket = PRECIO_TICKET
        return self.precio_ticket 

    def pagar_pasaje(self):
        precio_ticket = PRECIO_TICKET
        if self.estado == "desactivado":
            raise UsuarioDesactivadoException()
        if self.grupo_beneficiario == PRIMARIO:
            precio_ticket = 35
        if self.grupo_beneficiario == SECUNDARIO:
            precio_ticket = 42
        if self.saldo >= precio_ticket:
            self.saldo = self.saldo - precio_ticket
        else:
            raise NoHaySaldoException()
        
    def cambiar_estado(self, estado):
        self.estado = estado
        if estado == "pendiente":
            raise EstadoNoExistenteException()

