import tkinter

# Crear ventana
ventana = tkinter.Tk()
ventana.title("Trabajo paginaclic")
ventana.iconbitmap("homepage_home_house_icon_153873.ico")
ventana.geometry("900x700+400+50")


frame1 = tkinter.Frame()
frame1.configure(bg="pink1", bd=20, width=200, height=200)
label1 = tkinter.Label(frame1, text="gryffindor")

frame2 = tkinter.Frame()
frame2.configure(bg="orange", bd=20, width=200, height=200)
label2 = tkinter.Label(frame2, text="Hufflepuff")

frame3 = tkinter.Frame()
frame3.configure(bg="salmon3", bd=20, width=200, height=200)

def saludar():  # Método del botón
    print("¡Hola, gente!")

boton = tkinter.Button(frame3, text="Saludar", command=saludar)  # Command es para llamar al método
label3 = tkinter.Label(frame3, text="clic")

frame4 = tkinter.Frame()
frame4.configure(bg="cyan", bd=20, width=200, height=200)
label4 = tkinter.Label(frame4, text="slytherin")

# Configuración de la cuadrícula y empaquetado de widgets
frame1.grid(row=0, column=0)
label1.pack(pady=10)

frame2.grid(row=0, column=1)
label2.pack(pady=10)

frame3.grid(row=1, column=0)
label3.pack(pady=10)
boton.pack()

frame4.grid(row=1, column=1)
label4.pack(side=tkinter.LEFT, pady=10)  # Empaquetar etiqueta en frame4 a la izquierda

# Botón en el lado derecho de la etiqueta
boton_frame4 = tkinter.Button(frame4, text="Click Aquí", command=saludar)
boton_frame4.pack(side=tkinter.LEFT, padx=5, pady=10)  # Botón al lado de la etiqueta

ventana.mainloop()