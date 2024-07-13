from tkinter import *
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
import random
import json

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


class Login:
    def __init__(self, root):
        self.root = root
        root.update_idletasks()
        x = (root.winfo_screenwidth() // 2)-(600 // 2)
        y = (root.winfo_screenheight() // 2)-(600 // 2)
        self.root.geometry(f"600x600+{x}+{y}")
        self.root.title("Login|2048")
        self.login()

    def login(self,event=None):
        
        self.login_frame = ctk.CTkFrame(master = self.root, width = 400, height = 500, corner_radius = 15)
        self.login_frame.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)
        user_label = ctk.CTkLabel(master = self.login_frame, text = "Inicia sesion para jugar", font = ('Century Gothic', 22))
        user_label.place(x=50, y=105)
        
        self.user_entry = ctk.CTkEntry(master = self.login_frame, width = 300, height = 40, placeholder_text = "Nombre de usuario")
        self.user_entry.place(x=50, y=170)
        
        self.password_entry = ctk.CTkEntry(master = self.login_frame, width = 300, height = 40, placeholder_text = "Ingrese su contraseña", show = "x")
        self.password_entry.place(x=50, y=230)
        
        button_register = ctk.CTkLabel(master = self.login_frame, text = "Registrarse", font = ('Century Gothic', 12))
        button_register.place(x=275, y=280)
        button_register.bind('<Button-1>', self.register)
        self.button_Login = ctk.CTkButton(master = self.login_frame, width = 300, height = 40, text = "Iniciar sesion", command = self.login_logic)
        self.button_Login.place(x=50, y=320)
        
        
    def login_logic(self):
        name_user = self.user_entry.get()
        password = self.password_entry.get()
        usuario_existe = False
        if name_user != "" and password != "":
            with open ("users.json", "r") as file:
                usuarios = json.load(file)
            for usuario in usuarios:
                if usuario["user_name"] == name_user:
                    usuario_existe = True
                    if usuario["password"] == password:
                        print(f"Usuario: {name_user}|Contraseña: {password}")
                        self.root.destroy()
                        menu_prin = ctk.CTk()
                        Menu_principal(menu_prin)
                        menu_prin.mainloop()
                        
                    elif usuario["password"] != password:
                        password_incorrecta = ctk.CTkLabel(master = self.login_frame, text = "Contraseña incorrecta", font = ('Century Gothic', 12))
                        password_incorrecta.place(x=140, y=300)
                        self.button_Login.place(x=50, y=340)
                        
            if not usuario_existe:
                usuario_incorrecto = ctk.CTkLabel(master=self.login_frame, text=f"El usuario '{name_user}' no existe", font=('Century Gothic', 12))
                usuario_incorrecto.place(x=140, y=300)
                self.button_Login.place(x=50, y=340)
                    

                    
        elif name_user == "" or password == "":
            error_register = ctk.CTkLabel(master = self.login_frame, text = "Hay campos vacio", font = ('Century Gothic', 12))
            error_register.place(x=140, y=300)
            self.button_Login.place(x=50, y=340)
        
                    
    def register(self,event=None):
        self.login_frame.destroy()
        self.register_frame = ctk.CTkFrame(master = self.root, width = 400, height = 500, corner_radius = 15)
        self.register_frame.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)
        
        x_btn = ctk.CTkLabel(master = self.register_frame, text = "X",  text_color= "white", font = ('Century Gothic', 20))
        x_btn.place(x=350, y=50)
        x_btn.bind('<Button-1>', self.x)

        user_register_label = ctk.CTkLabel(master = self.register_frame, text = "Crea un usuario para jugar", font = ('Century Gothic', 22))
        user_register_label.place(x=55, y=105)
        
        self.user_register_entry = ctk.CTkEntry(master = self.register_frame, width = 300, height = 40, placeholder_text = "Nombre de usuario")
        self.user_register_entry.place(x=50, y=170)

        
        self.password_register_entry = ctk.CTkEntry(master = self.register_frame, width = 300, height = 40, placeholder_text = "Ingrese su contraseña", show = "x")
        self.password_register_entry.place(x=50, y=230)
        
        self.password_confirmed_entry = ctk.CTkEntry(master = self.register_frame, width = 300, height = 40, placeholder_text = "Confirme su contraseña", show = "x")
        self.password_confirmed_entry.place(x=50, y=290)
        
        self.button_register_Login = ctk.CTkButton(master = self.register_frame, width = 300, height = 40, text = "Crear Usuario", command = self.register_logic)
        self.button_register_Login.place(x=50, y=350)
    def x (self,event=None):
        self.register_frame.destroy()
        self.login()
    def register_logic(self,event=None):
        user_name = self.user_register_entry.get()
        password = self.password_register_entry.get()
        password_confirmed = self.password_confirmed_entry.get()

        
        if user_name != "" and password != "" and password == password_confirmed:
            datos = {"user_name": user_name, "password": password}
            with open ("users.json", "r") as file:
                usuarios = json.load(file)
            for usuario in usuarios:
                if usuario["user_name"] == user_name:
                    messagebox.showerror("Error", "El usuario ya existe")
                    break
            else:
                usuarios.append(datos) # Si el usuario no existe, agrega los nuevos datos a la lista de usuarios
                with open ("users.json", "w") as file:
                    json.dump(usuarios, file, indent=4)
                messagebox.showinfo("Registro", "Usuario registrado con éxito")
                self.register_frame.destroy()
                self.login()
                    
            
        elif user_name == "" or password == "" or password_confirmed == "":
            error_register = ctk.CTkLabel(master = self.register_frame, text = "Hay campos vacio", font = ('Century Gothic', 12))
            error_register.place(x=140, y=340)
            self.button_register_Login.place(x=50, y=380)
            
            
        elif password != password_confirmed:
            self.error_register1 = ctk.CTkLabel(master = self.register_frame, text = "Las contraseñas no son iguales", font = ('Century Gothic', 12))
            self.error_register1.place(x=100, y=340)
            self.button_register_Login.place(x=50, y=380)

class Menu_principal:
    def __init__(self, menu_prin):
        self.menu_prin = menu_prin
        menu_prin.update_idletasks()
        self.x = menu_prin.winfo_screenwidth()
        self.y = menu_prin.winfo_screenheight()
        self.menu_prin.geometry(f"{self.x}x{self.y}+0+0")
        self.menu_prin.title("Inicio")
        self.main_menu()
        
    
    def main_menu (self):
        ancho_men = 1042
        ancho_padding = 50
        padding_men = ancho_men - ancho_padding
        self.men = ctk.CTkFrame(master = self.menu_prin, width = ancho_men, height = self.y)
        self.men.place(x = self.x - padding_men, rely = 0.5, anchor = tk.CENTER)
        self.section_stats()
        self.section_info_user()
    
    def section_info_user(self):
        a = self.y - 958
        b = self.y - a
        user_info = ctk.CTkFrame(master = self.menu_prin, width = 428, height = b, fg_color = "#4DBA8B", corner_radius = 50)
        user_info.place(x = -43, y = a)

    def section_stats (self):
        ancho_stats = 428
        ancho_padding = 30
        padding_stats = ancho_stats - ancho_padding
        altura_partidas = 237
        modos_de_juego_altura = 100

        a = self.y - 958
        b = self.y - a
        
        stats = ctk.CTkFrame(master = self.menu_prin, width = ancho_stats, height = self.y)
        stats.place(x = self.x - ancho_stats )

        estadisticas = ctk.CTkLabel(master = stats, text = "Estadisticas", font = ('Arial Black', 24))
        estadisticas.place(relx = 0.5, y = a // 2, anchor = tk.CENTER)

        partidas = ctk.CTkFrame(master = stats, width = padding_stats, height = altura_partidas, fg_color = "#4DBA8B", corner_radius = 25)
        partidas.place(x = ancho_padding // 2, y = a)

        partidas_jugadas = ctk.CTkLabel(master = partidas, text = "99", font = ('Arial Black', 96))
        partidas_jugadas.place(relx = 0.5,  rely = 0.5, anchor = tk.CENTER)
        partidas_jugadas2 = ctk.CTkLabel(master = partidas, text = "Partidas jugadas", font = ('Arial Black', 16))
        partidas_jugadas2.place(relx = 0.5, y = altura_partidas - 25 , anchor = tk.CENTER)

        modo_de_juego = ctk.CTkLabel(master = stats, text = "Modos jugados", font = ('Arial Black', 24))
        modo_de_juego.place(x = ancho_padding // 2 , y = a + altura_partidas + 30)

        modo_de_juego1 = ctk.CTkFrame(master = stats, width = padding_stats, height = modos_de_juego_altura, fg_color = "#B3E7CB", corner_radius = 25)
        modo_de_juego1.place(x = ancho_padding // 2 , y = a + altura_partidas + 80)
        
        Clasico_label = ctk.CTkLabel(master = modo_de_juego1, text = "Clasico", font = ('Century Gothic', 24),text_color= "#114333")
        Clasico_label.place(relx = 0.2, rely = 0.5, anchor = tk.CENTER)
        Clasico_cantindad_label = ctk.CTkLabel(master = modo_de_juego1, text = "99", font = ('Century Gothic', 24),text_color= "#114333")
        Clasico_cantindad_label.place(x = padding_stats - 40 , rely = 0.5, anchor = tk.CENTER)

        modo_de_juego2 = ctk.CTkFrame(master = stats, width = padding_stats, height = modos_de_juego_altura, fg_color = "#B3E7CB", corner_radius = 25)
        modo_de_juego2.place(x = ancho_padding // 2 , y = a + altura_partidas + 200)

        self.contra_reloj_label = ctk.CTkLabel(master = modo_de_juego2, text = "Contra reloj", font = ('Century Gothic', 24),text_color= "#114333")
        self.contra_reloj_label.place(x = 105, rely = 0.5, anchor = tk.CENTER)
        contra_reloj = ctk.CTkLabel(master = modo_de_juego2, text = "99", font = ('Century Gothic', 24),text_color= "#114333")
        contra_reloj.place(x = padding_stats - 40 , rely = 0.5, anchor = tk.CENTER)

        modo_de_juego3 = ctk.CTkFrame(master = stats, width = padding_stats, height = modos_de_juego_altura, fg_color = "#81D4AD", corner_radius = 25)
        modo_de_juego3.place(x = ancho_padding // 2 , y = a + altura_partidas + 320)

        versus_label = ctk.CTkLabel(master = modo_de_juego3, text = "1 vs 1", font = ('Century Gothic', 24),text_color= "#114333")
        versus_label.place(x = 65, rely = 0.5, anchor = tk.CENTER)
        versus = ctk.CTkLabel(master = modo_de_juego3, text = "99", font = ('Century Gothic', 24),text_color= "#114333")
        versus.place(x = padding_stats - 40 , rely = 0.5, anchor = tk.CENTER)

        modo_de_juego4 = ctk.CTkFrame(master = stats, width = padding_stats, height = modos_de_juego_altura, fg_color = "#81D4AD", corner_radius = 25)
        modo_de_juego4.place(x = ancho_padding // 2 , y = a + altura_partidas + 440)

        libre_label = ctk.CTkLabel(master = modo_de_juego4, text = "Libre", font = ('Century Gothic', 24),text_color= "#114333")
        libre_label.place(x = 63, rely = 0.5, anchor = tk.CENTER)
        libre = ctk.CTkLabel(master = modo_de_juego4, text = "99", font = ('Century Gothic', 24),text_color= "#114333")
        libre.place(x = padding_stats - 40 , rely = 0.5, anchor = tk.CENTER)
        

class Game2028:
    def __init__(self, ventana):
        self.ventana = ventana
        #ventana.update_idletasks()
        #x = (ventana.winfo_screenwidth() // 2)-(400 // 2)
        #y = (ventana.winfo_screenheight() // 2)-(400 // 2)
        #self.ventana.geometry(f"400x400+{x}+{y}") #tamaño de la ventana y su ubicacion inicial
        ventana.columnconfigure(0, weight = 1)
        ventana.rowconfigure(0, weight = 1)
        self.ventana.title("2048")
        self.grid = [[0] * 4 for _ in range(4)] #genera una lista con cuatro 0 [0,0,0,0] y gracias al for se muestra 4 creando el tablero
        self.frame = [[None] * 4 for _ in range(4)] #similar al anterior pero este nos servira para hacer los cuadros del tablero
        self.tema= {
            0: "#ebe6ea",
            2: "#f19c45", 4: "#f19c45",
            8: "#ee3d42",  16: "#ee3d42",
            32: "#edc951", 64: "#edc951",
            128: "#00a0b0", 256: "#00a0b0",
            512: "#6a4a3c", 1024: "#6a4a3c",
            2048: "#000"}
        self.menu_bar()
        self.header()
        self.tablero()
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
        self.ventana.config(menu=menu_bar)
 #-------------------------------------------------------------------------------------------------------------------------------------------------------   
    def header(self):
        frame2_time = tk.Frame(self.ventana, bg = "#ebe6ea")    #contenedor superior, con el 2048, puntaje y mejor puntaje
        frame2_time.grid(column = 0, row = 0, sticky = (W, E))

        
        nombre = tk.Label(frame2_time,text = "2048", font = ("Arial", 40, "bold"), bg = "#ebe6ea", foreground = "#b1a39d") #2048
        nombre.grid(padx = 40, pady = 40)

        frame_score = tk.Frame(frame2_time, bg = "#ebe6ea") #frame hecho para posicionar el nombre arriba y el puntaje debajo
        frame_score.grid(column = 1, row = 0)
        
        score_name =tk.Label(frame_score, text = "Score", font = ("Arial", 11, "bold"), bg = "#bcaca4", foreground="white") #nombre
        score_name.grid(column = 0, row = 0, sticky = (W, N, E, S))
        
        self.score1 =tk.Label(frame_score, text = "", font = ("Arial", 20, "bold"), bg = "#bcaca4", foreground="white", width=5) #puntaje
        self.score1.grid(column = 0, row = 1)

        best_name =tk.Label(frame_score, text = "Best", font = ("Arial", 11, "bold"), bg = "#bcaca4", foreground="white") #nombre
        best_name.grid(column = 1, row = 0, sticky = (W, N, E, S), padx = 10)
        
        self.best =tk.Label(frame_score, text = "", font = ("Arial", 20, "bold"), bg = "#bcaca4", foreground="white", width=5) #mejor puntaje
        self.best.grid(column = 1, row = 1, padx = 10)

#-------------------------------------------------------------------------------------------------------------------------------------------------------      
    def tablero(self):
        self.container_frame = tk.Frame(self.ventana, bg="#ebe6ea")  # Frame hecho para pintar el padding del mismo color que el main xd
        self.container_frame.grid(column=0, row=1, ipady=20, sticky = (W, N, E, S))
        
        self.main_frame = tk.Frame(self.container_frame, bg = "#bcaca4")
        self.main_frame.grid (padx = 40, sticky = (W, N, E, S))

        self.container_frame.grid_columnconfigure(0, weight=1)
        self.container_frame.grid_rowconfigure(1, weight=1)
 
        for row in range(len(self.grid)): #por cada "fila" crea 4 columnas con sus respectivos cuadros
            for col in range(len(self.grid[row])):
                cuadro_tablero = tk.Frame(self.main_frame, width = 100, height = 100, bg = "red", relief = "flat")
                cuadro_tablero.grid(row = row, column = col, padx = 5, pady = 5, sticky=(W, N, E, S))
                cuadro = tk.Label(cuadro_tablero, text = "", font = ("Arial", 24, "bold"), width=4, height=2, bg="#ebe6ea")
                cuadro.pack(expand=True, fill=tk.BOTH)
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
                cuadro.config(text=str(value) if value != 0 else "",bg=self.tema.get(value, "#cdc1b4"), foreground="white")
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
                
        self.score1.config(text = str(self.puntaje))
        return movimiento_estado #Linea de mierda me olvide de ponerla y no funcaba 
#-------------------------------------------------------------------------------------------------------------------------------------------------------
    def mayor_puntaje(self):  # Celda con mayor valor
        if self.puntaje > self.mayor_puntuacion:  # Verificar si el puntaje actual es mayor
            self.mayor_puntuacion = self.puntaje
        self.best.config(text=str(self.mayor_puntuacion)) 
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
        if esternocleidomastoideo == "Facil":
            self.grid = [[0] * 4 for _ in range(4)]
        elif esternocleidomastoideo == "Media":
            self.grid = [[0] * 5 for _ in range(5)]
        elif esternocleidomastoideo == "Dificil":
            self.grid = [[0] * 6 for _ in range(6)]
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
    """root = ctk.CTk()
    Login(root)
    root.mainloop()"""
    menu_prin = ctk.CTk()
    Menu_principal(menu_prin)
    menu_prin.mainloop()

    # ventana = tk.Tk()
    # Game2028(ventana)
    # ventana.mainloop()

print("ᴍᴀᴅᴇ ʙʏ ᴍᴀᴜʀɪᴄɪᴏ ʟᴜᴄᴇʀᴏ")