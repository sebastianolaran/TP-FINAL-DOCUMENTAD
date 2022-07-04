from configuraciones.datos_iniciales import condiciones_iniciales
from acciones_funciones.validadores import texto
from acciones_funciones.diccionario_de_palabras import diccionario_de_palabras
from formularios.formulario_ingreso import formulario_ingreso
from app.app_consola import inicia_app
from configuraciones.estilos_widgets import msg_warning
"La funcion se encarga de ,luego de recibir la cantidad de jugadores,verificar que este"
"Dentro de los parametros permitidos para el uso del juego en defecto"
"Autor Omar Yaldin"
def confirmar(lista):

    players_entry,entrada_jugadores,root,botones,textos = lista
    MAX_JUGADORES = condiciones_iniciales()["cantidad_jugadores"]
    cantidad = texto(players_entry.get(),textos)

    if cantidad and cantidad <= MAX_JUGADORES:
        entrada_jugadores.pack_forget()
        jugadores = []
        
        diccionario_de_palabras()
        formulario_ingreso(root,botones,jugadores,cantidad,inicia_app,textos).pack() 
    else:
        msg_warning(f'{textos["MSJ_MAXIMO_JUGADORES"]} {MAX_JUGADORES}',textos)
