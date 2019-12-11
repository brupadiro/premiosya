from django.db import models
from secciones.apuestas.models.juego import Juego

class Apuesta(models.Model):

    cantidad_apostada = models.PositiveIntegerField()
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    #Resultados
    resultado_1 = models.PositiveIntegerField(null=True)
    resultado_2 = models.PositiveIntegerField(null=True)
    #Resultado apuesta
    resultado_apuesta = models.IntegerField(null=True)
    def __str__(self):
        return "Apuesta al juego {}".format(self.juego)

"""
Campos relacionados a juegos

apuesta 1x2:
    resultado_1 ( int 1 o 0 )
    resultado_2 ( int 1 o 0 )

    Es la apuesta más fácil de entender, pero también la más difícil de jugar.
    El resultado_1 indica la victoria del equipo local,
    El resultado_2 indica la victoria del equipo local,
    Los dos resultados en 0 es un empate.

apuesta doble:

    resultado_1 ( int )
    resultado_2 ( int ) 

    Apuesta: resultado_local > resultado_visitante || resultado_local == resultado_visitante

    Apuesta a dos de los tres resultados posibles.
    Si cree que es imposible que pierda el equipo local, apueste a 1X (victoria en casa o empate).
    Esta apuesta aumenta sus posibilidades de beneficio, pero en detrimento de la cuota.

apuesta descando final:

    resultado_1 ( int )
    resultado_2 ( int ) 

    Este tipo de apuesta combina el resultado en el descanso y el resultado al final de los 90 minutos.
    Para ganar la apuesta hay que pronosticar el resultado en el descanso
    y el resultado al final del tiempo reglamentario.

apuesta resultado final:

    resultado_1 ( int )
    resultado_2 ( int ) 

    Debe pronosticar el resultado exacto del partido al final de los 90 minutos.


apuesta par/impar:

    resultado_1 ( int ) es resultado par
    resultado_2 ( int ) es resultado impar

    Debe pronosticar si el partido finaliza con resultado par o impar.

Total equipo local:

    resultado_1 ( int ) es resultado par

    Debe pronosticar el resultado del equipo local.

Total equipo visitante:

    resultado_1 ( int ) es resultado par

    Debe pronosticar el resultado del equipo visitante.


"""

