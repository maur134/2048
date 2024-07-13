from tkinter import *
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
import random

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

class Game2028:
    def __init__(self, ventana):
        self.ventana = ventana
        self.x = ventana.winfo_screenwidth()
        self.y = ventana.winfo_screenheight()
        self.ventana.geometry(f"{self.x}x{self.y}+0+0")
        self.ventana.title("2048")
        ventana.columnconfigure(0, weight = 1)
        ventana.rowconfigure(0, weight = 1)
        self.ventana.title("2048")
        self.grid = [[0] * 4 for _ in range(4)] #genera una lista con cuatro 0 [0,0,0,0] y gracias al for se muestra 4 creando el tablero
        self.frame = [[None] * 4 for _ in range(4)] #similar al anterior pero este nos servira para hacer los cuadros del tablero
        self.tema={
            0: "#242424",
            2: "#4DBA8B",   # Color base
            4: "#449A78",   # Variación más oscura del color base
            8: "#55D39E",   # Variación más clara del color base
            16: "#3C8F6E",  # Otra variación más oscura del color base
            32: "#66E5B0",  # Otra variación más clara del color base
            64: "#339B72",  # Variación diferente del color base
            128: "#77F7C3", # Variación más clara del color base
            256: "#2B765D", # Variación más oscura del color base
            512: "#88F7D3", # Otra variación más clara del color base
            1024: "#22634C",# Otra variación más oscura del color base
            2048: "#B9FFE6" # Variación más clara y más cercana al blanco
        }
        
        # {
        #     0: "#242424",
        #     2: "#f19c45", 4: "#f19c45",
        #     8: "#ee3d42",  16: "#ee3d42",
        #     32: "#edc951", 64: "#edc951",
        #     128: "#00a0b0", 256: "#00a0b0",
        #     512: "#6a4a3c", 1024: "#6a4a3c",
        #     2048: "#000"
        #     }
        
        
        
        self.menu_bar()
        self.main_game()
        self.inicio()
        self.puntaje = 0
        self.mayor_puntuacion = 0
        ventana.bind('<Key>', self.flechas)

#-------------------------------------------------------------------------------------------------------------------------------------------------------   
    def menu_bar(self):
        #Nav bar         
        menu_bar = Menu(self.ventana)
        menu_1 = tk.Menu(menu_bar, tearoff=0)
        menu_2 = tk.Menu(menu_bar, tearoff=0)
        
        menu_1.add_command(label="Facil", command=lambda: self.dificultad("Facil"))
        menu_1.add_separator()
        menu_1.add_command(label="Media", command=lambda: self.dificultad("Media"))
        menu_1.add_separator()
        menu_1.add_command(label="Dificll", command=lambda: self.dificultad("Dificil"))

        menu_2.add_command(label="Tema 1", command=lambda: self.agregar_tema(1))
        menu_2.add_separator()
        menu_2.add_command(label="Tema 2", command=lambda: self.agregar_tema(2))
        menu_2.add_separator()
        menu_2.add_command(label="Tema 3", command=lambda: self.agregar_tema(3))
        menu_2.add_separator()
        menu_2.add_command(label="Cursed", command=lambda: self.agregar_tema(4))
        
        menu_bar.add_cascade(label="Dificultad", menu=menu_1)
        menu_bar.add_cascade(label="Temas", menu=menu_2)
        self.ventana.configure(menu=menu_bar)
 #-------------------------------------------------------------------------------------------------------------------------------------------------------   
    def main_game(self):
        self.frame_jueguito = ctk.CTkFrame(master = self.ventana, width= 450, height=545, corner_radius = 25)
        self.frame_jueguito.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)
        self.header()
        self.tablero()
        
    def header(self):
        self.frame2_time = ctk.CTkFrame(self.frame_jueguito, width= 430, height=100, fg_color = "transparent")    #contenedor superior, con el 2048, puntaje y mejor puntaje
        self.frame2_time.place(relx = 0.5,rely = 0.14, anchor = ctk.CENTER)
        

        nombre = ctk.CTkLabel(master = self.frame2_time,text = "2048", font = ('Arial Black', 40)) #2048
        nombre.place(x = 90, rely = 0.5, anchor = ctk.CENTER)

        # frame_score = tk.Frame(self.frame2_time, bg = "#ebe6ea") #frame hecho para posicionar el nombre arriba y el puntaje debajo
        # frame_score.grid(column = 1, row = 0)
        
        score_frame = ctk.CTkFrame(master = self.frame2_time, fg_color = "#4DBA8B")
        score_frame.place(x = 230, rely = 0.5, anchor = ctk.CENTER)

        score_name =ctk.CTkLabel(score_frame, text = "Score", font = ('Arial Black', 16), text_color = "white", width = 85) #nombre
        score_name.grid(column = 1, row = 0, sticky = (W, N, E, S), padx = 10)
        
        self.score1 =ctk.CTkLabel(score_frame, text = "0", font = ('Arial Black', 20), text_color = "white", width = 85) #puntaje
        self.score1.grid(column = 1, row = 1, padx = 10)
        
        best_frame = ctk.CTkFrame(master = self.frame2_time, fg_color = "#4DBA8B")
        best_frame.place(x = 347, rely = 0.5, anchor = ctk.CENTER)

        best_name = ctk.CTkLabel(best_frame, text = "Best", font = ('Arial Black', 16), text_color = "white", width = 85) #nombre
        best_name.grid(column = 1, row = 0, sticky = (W, N, E, S), padx = 10)
        
        self.best = ctk.CTkLabel(best_frame, text = "0", font = ('Arial Black', 20), text_color = "white", width = 85) #mejor puntaje
        self.best.grid(column = 1, row = 1, padx = 10)

#-------------------------------------------------------------------------------------------------------------------------------------------------------      
    def tablero(self):
        self.container_frame = ctk.CTkFrame(master = self.frame_jueguito)  # Frame hecho para pintar el padding del mismo color que el main xd
        self.container_frame.place(relx = 0.5, rely = 0.6, anchor = ctk.CENTER)
        
        self.main_frame = ctk.CTkFrame(master = self.container_frame)
        self.main_frame.pack(expand=True, fill=tk.BOTH)

        # for row in range(len(self.grid)): #por cada "fila" crea 4 columnas con sus respectivos cuadros
        #     for col in range(len(self.grid[row])):
        #         cuadro_tablero = ctk.CTkFrame(master = self.main_frame, width = 100, height = 100, border_width = None)
        #         cuadro_tablero.grid(row = row, column = col, padx = 5, pady = 5, sticky=(W, N, E, S))
        #         cuadro = tk.Label(cuadro_tablero, text = "", font = ("Arial", 24, "bold"), width=4, height=2, bg="#ebe6ea")
        #         # cuadro = ctk.CTkLabel(master = cuadro_tablero, text = "", font = ("Arial", 24, "bold"), width=4, height=2, fg_color ="#ebe6ea")
        #         # cuadro.pack(expand=True, fill=tk.BOTH)
        #         cuadro.grid(sticky=(W, N, E, S))

        #         self.frame[row][col] = cuadro

        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                cuadro_tablero = ctk.CTkFrame(master=self.main_frame, width=100, height=100, corner_radius = 10, fg_color="transparent")
                cuadro_tablero.grid(row=row, column=col, padx = 5, pady=5, sticky="nsew")
                
                cuadro = ctk.CTkLabel(master=cuadro_tablero, text="", font=("Arial", 24, "bold"), width=85, height=85, fg_color="#242424", corner_radius = 8)
                cuadro.grid(sticky="nsew")

                self.frame[row][col] = cuadro
        
        
#-------------------------------------------------------------------------------------------------------------------------------------------------------    
    def inicio(self):
        self.cuadro_random()
        self.cuadro_random()
        self.update_grid()

    def cuadro_random(self):
        celdas = [(r, c) for r in range(len(self.grid)) for c in range(len(self.grid)) if self.grid[r][c] == 0]  # Crea una lista de todas las celdas vacías (valor 0) en la cuadrícula
        if celdas:  # Verifica si hay celdas vacías disponibles
            row, col = random.choice(celdas)  # Elige una celda vacía al azar
            self.grid[row][col] = random.choice([2, 4])  # Asigna un valor aleatorio de 2 o 4 a la celda seleccionada
                    
    def update_grid(self):
        for row in range(len(self.grid)): # Itera sobre cada fila de la cuadrícula
            for col in range(len(self.grid)): # Itera sobre cada columna de la cuadrícula
                value = self.grid[row][col]  # Obtiene el valor de la celda en la posición (row, col)
                cuadro = self.frame[row][col] # Obtiene la etiqueta correspondiente a esa celda
                cuadro.configure(text=str(value) if value != 0 else "",fg_color = self.tema.get(value, "#cdc1b4"), text_color = "white")
# Configura el texto de la etiqueta; si el valor es 0, el texto es una cadena vacía (es un operador ternario)
# Configura el color de fondo; celdas vacías son gris claro, otras son naranja

#-------------------------------------------------------------------------------------------------------------------------------------------------------
    def flechas(self, event):
         if event.keysym in ["Up", "Down", "Left", "Right"]: #atributo .keysym para que tome el nombre de las flechas
            if self.movimiento(event.keysym): # Si el movimiento es válido 
                self.cuadro_random() # Añade un nuevo cuadro aleatorio
                self.update_grid() # Actualiza la cuadrícula visualmente
                self.mayor_puntaje()
                if self.checkeo_victoria(): # Verifica si el jugador ha ganado
                    self.ventana_victoria_derrota("¡Has ganado!")
                elif self.checko_derrota(): # Verifica si el juego ha terminado
                    self.ventana_victoria_derrota("¡Juego terminado!")

    def movimiento (self, direccion):
        def compress(row):
            new_row = [i for i in row if i != 0] #for comprimido, en el cual se le asigna los valores distintos a 0 de "row"
            new_row += [0] * (len(row) - len(new_row)) #A new_row se le suma la diferencia de las longitudes de row y new row
            return new_row
        
        def merge(row): #fusion de los cuadros
            for i in range(len(row) - 1):  # Itera sobre cada índice de la fila menos el último (xq el if comprueba con el siguiente elemento)
                if row[i] == row[i + 1] and row[i] != 0:  # Comprueba si el elemento actual y el siguiente son iguales y no son cero
                    row[i] *= 2  # Duplica el valor del elemento actual
                    self.puntaje += row[i] 
                    row[i + 1] = 0  # Establece el siguiente elemento a cero
            return row  # Devuelve la fila modificada
        movimiento_estado = False

        if direccion == "Up":  # Verifica si la dirección del movimiento es "Up"
            for col in range (len(self.grid)):  # Itera a través de cada columna del tablero.
                new_col = [self.grid[row][col] for row in range(len(self.grid))]  # Crea una lista con todos los valores de la columna actual.
                new_col = compress(merge(compress(new_col)))  # Comprime la columna, combina celdas adyacentes iguales, y vuelve a comprimirla.
                for row in range(len(self.grid)):  # Itera a través de cada fila de la columna actual.
                    if self.grid[row][col] != new_col[row]:  # Verifica si el valor de la celda ha cambiado.
                        movimiento_estado = True  #establece movimiento_estado como True para indicar que se ha realizado un movimiento.
                    self.grid[row][col] = new_col[row]  # Actualiza el valor de la celda en el tablero con el nuevo valor de la columna.


        elif direccion == "Down": #Practicamente lo mismo que el "UP" pero gracias al [::-1] invierte la forma de combinar la columna 
             for col in range(len(self.grid)):
                new_col = [self.grid[row][col] for row in range(len(self.grid))]
                new_col = compress(merge(compress(new_col[::-1])))[::-1]
                for row in range(len(self.grid)):
                    if self.grid[row][col] != new_col[row]:
                        movimiento_estado = True
                    self.grid[row][col] = new_col[row]
            
        elif direccion == "Left":  # Verifica si la dirección del movimiento es "Left"
            for row in range(len(self.grid)):  #Itera a travez de cada fila del tablero
                new_row = compress(merge(compress(self.grid[row]))) # comprime la columna, combina las celdas adyacentes iguales y vuelve a comprimirlas
                if self.grid[row] != new_row:  # verivica si el valor de la celda ha cambiado 
                    movimiento_estado = True  # establece movimiento_estado en true, indicando que se ha realizado un movimiento
                self.grid[row] = new_row  #Actualiza el valor de la celda en el tablero con el nuevo valor de la fila
                
            
        elif direccion == "Right":  #Practicamente lo mismo que el "Left" pero gracias al [::-1] invierte la forma de combinar la fila 
            for row in range(len(self.grid)):
                new_row = compress(merge(compress(self.grid[row][::-1])))[::-1]
                if self.grid[row] != new_row:
                    movimiento_estado = True
                self.grid[row] = new_row
                
        self.score1.configure(text = str(self.puntaje))
        return movimiento_estado #Linea de mierda me olvide de ponerla y no funcaba 
#-------------------------------------------------------------------------------------------------------------------------------------------------------
    def mayor_puntaje(self):  # Celda con mayor valor
        if self.puntaje > self.mayor_puntuacion:  # Verificar si el puntaje actual es mayor
            self.mayor_puntuacion = self.puntaje
        self.best.configure(text=str(self.mayor_puntuacion)) 
#-------------------------------------------------------------------------------------------------------------------------------------------------------
    def checkeo_victoria(self):
        return any(2048 in row for row in self.grid) #retornara "true" si se haya un 2048 en alguna fila del self.grid
    
    def checko_derrota(self):
        for row in range(len(self.grid)): 
            for col in range(len(self.grid)):
                if self.grid[row][col] == 0: #si alguna celda vale 0 retornara false ya que aun quedan movimiento/s
                    return False
                if row < 3 and self.grid[row][col] == self.grid[row + 1][col]: #verifica si la celda de abajo es igual a la de arriba
                    return False #si se cumple la condicion devuelve false, permitiendo otro movimiento
                if col < 3 and self.grid[row][col] == self.grid[row][col + 1]: #verifica si la celda de al lado es igual a otra
                    return False #si se cumple la condicion devuelve false, permitiendo otro movimiento
        return True

    def ventana_victoria_derrota(self, message):
        messagebox.showinfo("2048", message)
        self.reiniciar_juego()
#-------------------------------------------------------------------------------------------------------------------------------------------------------
    #logica del menu
    def dificultad(self, esternocleidomastoideo):
        # if esternocleidomastoideo == "Facil":
        #     self.grid = [[0] * 4 for _ in range(4)]
        # elif esternocleidomastoideo == "Media":
        #     self.grid = [[0] * 5 for _ in range(5)]
        # elif esternocleidomastoideo == "Dificil":
        #     self.grid = [[0] * 6 for _ in range(6)]
        # self.reiniciar_juego()
        if esternocleidomastoideo == "Facil":
            self.grid = [[0] * 4 for _ in range(4)]
            self.frame_width = 450
            self.frame_height = 545
        elif esternocleidomastoideo == "Media":
            self.grid = [[0] * 5 for _ in range(5)]
            self.frame_width = 550
            self.frame_height = 645
        elif esternocleidomastoideo == "Dificil":
            self.grid = [[0] * 6 for _ in range(6)]
            self.frame_width = 650
            self.frame_height = 745
        self.reiniciar_juego()

    def agregar_tema(self, tema):
        temas = {
            1: {
                0: "#f2e6d8",
                2: "#f9a78f", 4: "#f9a78f",
                8: "#f75c03", 16: "#f75c03",
                32: "#ffba08", 64: "#ffba08",
                128: "#8ac926", 256: "#8ac926",
                512: "#1982c4", 1024: "#1982c4",
                2048: "#6a4a3c"
            },
            2: {
                0: "#",
                2: "#", 4: "#",
                8: "#", 16: "#",
                32: "#", 64: "#",
                128: "#", 256: "#",
                512: "#", 1024: "#",
                2048: "#"
            },
            3: {
                0: "#",
                2: "#", 4: "#",
                8: "#", 16: "#",
                32: "#", 64: "#",
                128: "#", 256: "#",
                512: "#", 1024: "#",
                2048: "#"
            },
            4: {
                0: "#",
                2: "#", 4: "#",
                8: "#", 16: "#",
                32: "#", 64: "#",
                128: "#", 256: "#",
                512: "#", 1024: "#",
                2048: "#"
            }
        }
        self.tema = temas.get(tema, self.tema)
        self.update_grid()
#-------------------------------------------------------------------------------------------------------------------------------------------------------
    def reiniciar_juego(self):
        self.frame_jueguito.configure(width=self.frame_width, height=self.frame_height)
        self.frame_jueguito.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.grid = [[0] * len(self.grid) for _ in range(len(self.grid))]
        self.frame = [[None] * len(self.grid) for _ in range(len(self.grid))]
        self.main_frame.destroy()
        self.container_frame.destroy()
        self.tablero()
        self.cuadro_random()
        self.cuadro_random()
        self.update_grid()
        self.puntaje = 0
        self.score1.config(text=str(self.puntaje))
#-------------------------------------------------------------------------------------------------------------------------------------------------------        
if __name__ == "__main__":
    ventana = ctk.CTk()
    Game2028(ventana)
    ventana.mainloop()
    

# print("ᴍᴀᴅᴇ ʙʏ ᴍᴀᴜʀɪᴄɪᴏ ʟᴜᴄᴇʀᴏ")
