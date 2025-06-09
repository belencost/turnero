
class Turnero:
    def __init__(self):
#Se lleva la cuenta de cuantos turnos se generaron por tipo 
        self.contadores = {
            "CAJ": 0, #Caja
            "PERS": 0, #Atención personalizada 
            "REC": 0,  #Reclamos
            "JOP": 0, #Jubilaciones o pensiones
        }

    def generar_turno(self, tipo):
        #Si el tipo ingresado no es válido, se lanza un error
        if tipo not in self.contadores:
            raise ValueError("Tipo de turno no válido")
       
       #Sumamos 1 al contador correspondiente
        
        self.contadores[tipo] += 1
        return f"{tipo}-{self.contadores[tipo]:03d}"

