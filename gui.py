# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 17:25:06 2021

@author: esteb
interfaz gráfica
"""
import tkinter as tk
from PIL import Image, ImageTk
import cv2
import imutils
import deteccion_placas as dp


ventana = tk.Tk()

ventana.geometry('1000x680+200+20') #tamaño y donde inicia
ventana.title("Detección Placas")
#ventana.columnconfigure(0, weight=0)
#ventana.columnconfigure(1, weight=1)
#ventana.rowconfigure(0, weight=1)

#funciones
cap = None

def stream():
    global cap
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    dp.main()
    iniciar()

def iniciar():
    global cap
    ret,frame = cap.read()
    if ret == True:
        fb_video.config(bg='green')
        et_video.grid(row=1, column=1)
        # dp.frame = imutils.resize(dp.frame, width= 640)
        # dp.frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # cv2.imshow('PLACA',dp.placa)
        # cv2.moveWindow('PLACA',780,10) #pos de la placa
        # cv2.rectangle(dp.frame,(dp.x,dp.y),(dp.x+dp.w,dp.y+dp.h),(0,255,0),3)
        # cv2.putText(dp.frame,dp.text,(dp.x-20,dp.y-10),1,2.2,(0,255,0),3)
        img = Image.fromarray(dp.frame)
        image = ImageTk.PhotoImage(image=img)
        et_video.configure(image=image)
        et_video.image =image
        et_video.after(10,iniciar)
        

        
def quitar():
    global cap
    fb_video.config(bg='red')
    et_video.grid_forget()
    cap.release()
    
    
#colores
fondo_boton = "#5e17eb"
#botones

boton= tk.Button(ventana, text ="iniciar video", bg =fondo_boton,
                 relief = "flat", cursor = "hand2", width =15, height = 2,
                 font= ("Calisto MT", 12, "bold"), command = stream)

boton1 = tk.Button(ventana, text ="quitar video", bg =fondo_boton,
                 relief = "flat", cursor = "hand2", width =15, height = 2,
                 font= ("Calisto MT", 12, "bold"),command = quitar)
boton.grid(padx =4,row = 4,column=0)
boton1.grid(padx =4,row = 4,column=5)

#video
fb_video = tk.Label(ventana, text = "Estado camara")
fb_video.grid(row=0, column=0)

et_video = tk.Label(ventana, bg="black")
et_video.grid(row=1, column=1)

#boton.grid(padx =15,row = 1,column=2)

ventana.mainloop()