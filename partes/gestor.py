from partes import jugador_del_juego

class gestorPartida:
    '''Esta clase es la que gestiona la partida en su conjunto'''  
    def __init__(self):
        self.jugadores =[]

    def anadirJugador(self, nombre, type):
        '''Esta función se encarga de añadir jugadores'''
        self.jugadores.append(jugador_del_juego(nombre,type)) 
        
    def VotacionDia(self, NombreVotado):
        '''Esta función gestiona las votaciones'''
        for j in self.jugadores:
            if j.Nombre == NombreVotado:
                if j.esta_vivo:
                    j.esta_vivo=False
                    return "El pueblo ha linchado a " + NombreVotado + " en la hoguera."
        return "Nadie fue linchado."    
        

    def ComprobarVictoria(self):  
        '''Esta función se encarga de comprobar si ha ganado alguien y quien ha sido'''
        list = sum(1 for j in self.jugadores if j.rol == "lobo" and j.esta_vivo)
        dict = sum(1 for j in self.jugadores if j.rol != "lobo" and j.esta_vivo)
        
        if list >= dict:
            return "¡Victoria de los Lobos!"
        elif list ==0:
            return "¡Victoria de los Aldeanos!"
        return "La partida debe continuar..."