from django.db import models
from secciones.apuestas.models.juego import Juego

class Apuesta(models.Model):

    cantidad_apostada = models.PositiveIntegerField()
    fecha = models.models.DateField()
    juego = models.OneToOneField(Juego, on_delete=models.CASCADE)
    
    #Resultados
    resultado_descanzo = models.PositiveIntegerField('resultado_descanzo')
    resultado_final = models.PositiveIntegerField('resultado_final')
    victoria_local = models.BooleanField('victoria_local')
    victoria_visitante = models.BooleanField('victoria_visitante')
    resultado_local = models.PositiveIntegerField('resultado_local')
    resultado_visitante = models.PositiveIntegerField('resultado_vistante')

"""
Campos relacionados a juegos

apuesta 1x2:
    victoria_local ( boolean )
    victoria_visitante ( boolean )

    Es la apuesta más fácil de entender, pero también la más difícil de jugar.
    El 1 indica la victoria del equipo local,
    la X un empate y el 2 significa la victoria del equipo visitante.

apuesta doble:

    resultado_local ( int )
    resultado_visitante ( int ) 

    Apuesta: resultado_local > resultado_visitante || resultado_local == resultado_visitante

    Apuesta a dos de los tres resultados posibles.
    Si cree que es imposible que pierda el equipo local, apueste a 1X (victoria en casa o empate).
    Esta apuesta aumenta sus posibilidades de beneficio, pero en detrimento de la cuota.

apuesta descanzo final:

    resultado_descanzo ( int )
    resultado_final ( int )

    Este tipo de apuesta combina el resultado en el descanso y el resultado al final de los 90 minutos.
    Para ganar la apuesta hay que pronosticar el resultado en el descanso
    y el resultado al final del tiempo reglamentario.

apuesta devolucion empate:

    victoria_local ( boolean )
    victoria_visitante ( boolean )

    if !victoria_local && !victoria_visitante => devolver cash

    Gracias a este tipo de apuesta, no perderá la apuesta si un partido termina en empate.
    La casa de apuestas le devolverá el dinero en ese caso.
    Esta apuesta resulta muy interesante si cree que uno de los equipos no tiene ninguna posibilidad de ganar,
    pero puede lograr un empate.

apuesta resultado final:

    resultado_local ( int )
    resultado_visitante ( int ) 

    Debe pronosticar el resultado exacto del partido al final de los 90 minutos.

"""