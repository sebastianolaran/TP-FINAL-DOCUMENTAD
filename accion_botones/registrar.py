
def registrarse(lista):
    formulario_registro,root,cuadro_botones,textos = lista
    form_registro = formulario_registro(root,cuadro_botones,textos)
    form_registro.pack()
    cuadro_botones.pack_forget()
    