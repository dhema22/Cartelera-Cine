from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk 

raiz=tk.Tk()

archivo=open("Actividad6-3.xml","r")
contenido=archivo.read()
xml=BeautifulSoup(contenido,"xml")
contador=0
arbol=ttk.Treeview(raiz, columns=('titulo','año','director','actores','genero','categoria'))
arbol.heading("#0", text="identificador")
arbol.heading("titulo", text="Nombre")
arbol.heading("año",text="año")
arbol.heading("director",text="director")
arbol.heading("actores", text="actores")
arbol.heading("genero", text="genero")
arbol.heading("categoria", text="categoria")


for pelicula in xml.find_all("pelicula"):
    tipo=pelicula.get("tipo")
    titulo=pelicula.get("titulo")
    year=pelicula.get("year")
    director=pelicula.get("director")
    actores=pelicula.get("actores")
    genero=pelicula.get("genero")
    categoria=pelicula.get("categoria")

    
    if tipo=="label":
        ttk.Label(raiz, text=titulo).pack(padx=50,pady=50)
    elif tipo=="lista":
        arbol.insert('',contador,text=contador,values=(titulo,year,director,actores,genero,categoria))
        arbol.pack()
    elif tipo=="categoria":
        v=tk.IntVar()
        v.set(0)
        radioBoton1=ttk.Radiobutton(raiz, text="joven menor de 25 años", variable=v, value=1)
        radioBoton1.pack()
        radioBoton2=ttk.Radiobutton(raiz, text="tercera edad", variable=v, value=2)
        radioBoton2.pack()
        radioBoton3=ttk.Radiobutton(raiz, text="adulto", variable=v, value=3)
        radioBoton3.pack()

        ttk.Button(raiz, text="comprar").pack(padx=10,pady=10)
    elif tipo=="review":
        ttk.Label(raiz, text=titulo).pack(padx=20, pady=20)
        tk.Text(raiz, width=30, height=10).pack(padx=20,pady=20)
        ttk.Button(raiz, text="enviar").pack(padx=10,pady=10)
    
    
    contador=contador+1


raiz.mainloop()