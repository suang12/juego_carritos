from tkinter import*
import random

BASE=760
ALTURA=460

# funciones de los carros
def mover_carro1(sapo):
    global desplazamiento_x, desplazamiento_y
    
    x0, y0, x1, y1 = c.coords()
    if x0 < 0 or x1 > BASE: 
        desplazamiento_x = -desplazamiento_x
    if y0 < 0 or y1 > ALTURA: 
        desplazamiento_y = -desplazamiento_y
    c.move(carro1, desplazamiento_x, desplazamiento_y)
    ventana_principal.after(intervalo, mover_carro1)



#ventana del juego
ventana_principal = Tk()
ventana_principal.title("JUEGUITO")
ventana_principal.geometry("800x500")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="green")
# centro del juego
frame_juego = Frame(ventana_principal)
frame_juego.config(bg="green", width=780 , height=480 )
frame_juego.place(x=10 , y=10)
c = Canvas(frame_juego, width=BASE, height=ALTURA)
c.config(bg="gray")
c.place(x=10, y=10)

rect_1 = c.create_rectangle(BASE/2-450,BASE/2+220,125,ALTURA-480,fill="red", outline="black")
rect_4 = c.create_rectangle(BASE/2-380,ALTURA/2-100,BASE/2+360,ALTURA/2-210,fill="white", outline="black")

# punto de inicio del carro 1
logo = PhotoImage(file="carrito1.png")
carro1 = Label(frame_juego, image=logo, bg="white")
carro1.place(x=10,y=40)

# punto de inicio del carro 2
logo1 = PhotoImage(file="carrito2.png")
carro2 = Label(frame_juego, image=logo1, bg="white")
carro2.place(x=10,y=300)

# boton para jugar 
bt_convertir = Button(frame_juego,text="JUGAR YA",)
bt_convertir.place(x=350, y=450, width=100, height=30)

# cartel de salida
lb_salida = Label(ventana_principal, text="S", bg="gray", fg="red", font=("Helvetica", 20))
lb_salida.place(x=280, y=150)
lb_salida = Label(ventana_principal, text="A", bg="gray", fg="red", font=("Helvetica", 20))
lb_salida.place(x=280, y=175)
lb_salida = Label(ventana_principal, text="L", bg="gray", fg="red", font=("Helvetica", 20))
lb_salida.place(x=280, y=200)
lb_salida = Label(ventana_principal, text="I", bg="gray", fg="red", font=("Helvetica", 20))
lb_salida.place(x=280, y=225)
lb_salida = Label(ventana_principal, text="D", bg="gray", fg="red", font=("Helvetica", 20))
lb_salida.place(x=280, y=245)
lb_salida = Label(ventana_principal, text="A", bg="gray", fg="red", font=("Helvetica", 18))
lb_salida.place(x=280, y=275)
#carreta para el carro 1


# cartel de meta 
lb_salida = Label(ventana_principal, text="M", bg="gray", fg="red", font=("Helvetica", 20))
lb_salida.place(x=720, y=150)
lb_salida = Label(ventana_principal, text="E", bg="gray", fg="red", font=("Helvetica", 20))
lb_salida.place(x=720, y=190)
lb_salida = Label(ventana_principal, text="T", bg="gray", fg="red", font=("Helvetica", 20))
lb_salida.place(x=720, y=230)
lb_salida = Label(ventana_principal, text="A", bg="gray", fg="red", font=("Helvetica", 20))
lb_salida.place(x=720, y=270)














# carretera para el carro 2
rect_4 = c.create_rectangle(BASE/2-380,ALTURA/2+50,BASE/2+360,ALTURA/2+140,fill="white", outline="black")

ventana_principal.mainloop()



