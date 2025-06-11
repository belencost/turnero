
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
        if not isinstance(tipo, str):
            raise ValueError("El tipo de turno debe ser texto")
        if tipo.strip() not in self.contadores:
            raise ValueError("Tipo de turno inválido")
        
        #Sumamos 1 al contador correspondiente

        tipo = tipo.strip()
        self.contadores[tipo] += 1
        numero = self.contadores[tipo]
        return f"{tipo}-{numero:03d}"

       


