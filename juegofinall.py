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
        self.x = root.winfo_screenwidth()
        self.y = root.winfo_screenheight()
        self.root.geometry(f"{self.x}x{self.y}+0+0")
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
        self.jugar_sin_login = ctk.CTkButton(master = self.login_frame, width =  300, height = 40, text = "Jugar sin loguearse", fg_color = "transparent", hover_color = "#1b1b1b", command = self.sin_login)
        self.jugar_sin_login.place(x=50, y=370)
    def sin_login(self):
        self.root.withdraw()  # Oculta la ventana principal
        self.login_frame.destroy()

        self.root.deiconify()
        Game2028(self.root)
        
        
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


                        self.root.withdraw()
                        self.login_frame.destroy()
                        self.root.deiconify()

                        juego = Game2028(self.root, user_name=name_user, score_json=usuario["score_json"])
                        juego.borrado_sesion_register()


                    elif usuario["password"] != password:
                        password_incorrecta = ctk.CTkLabel(master = self.login_frame, text = "Contraseña incorrecta", font = ('Century Gothic', 12))
                        password_incorrecta.place(x=140, y=300)
                        self.button_Login.place(x=50, y=340)
                        self.jugar_sin_login.place(x=50, y=390)
                        
            if not usuario_existe:
                usuario_incorrecto = ctk.CTkLabel(master=self.login_frame, text=f"El usuario '{name_user}' no existe", font=('Century Gothic', 12))
                usuario_incorrecto.place(x=140, y=300)
                self.button_Login.place(x=50, y=340)
                self.jugar_sin_login.place(x=50, y=390)
                    

                    
        elif name_user == "" or password == "":
            error_register = ctk.CTkLabel(master = self.login_frame, text = "Hay campos vacio", font = ('Century Gothic', 12))
            error_register.place(x=140, y=300)
            self.button_Login.place(x=50, y=340)
            self.jugar_sin_login.place(x=50, y=390)
        
                    
    def register(self, event=None):

        self.root.withdraw() 
        self.login_frame.destroy() 
        register_window = ctk.CTkToplevel()
        Register(register_window)

class Register:
    def __init__(self, root):
        self.root = root
        root.update_idletasks()
        self.x = root.winfo_screenwidth()
        self.y = root.winfo_screenheight()
        self.root.geometry(f"{self.x}x{self.y}+0+0")
        self.root.title("Registro | 2048")
        self.register()

    def register(self, event=None):
        self.register_frame = ctk.CTkFrame(master=self.root, width=400, height=500, corner_radius=15)
        self.register_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        x_btn = ctk.CTkLabel(master=self.register_frame, text="×", text_color="white", font=('Century Gothic', 40))
        x_btn.place(x=350, y=50)
        x_btn.bind('<Button-1>', self.btn_x)

        user_register_label = ctk.CTkLabel(master=self.register_frame, text="Crea un usuario para jugar", font=('Century Gothic', 22))
        user_register_label.place(x=55, y=105)

        self.user_register_entry = ctk.CTkEntry(master=self.register_frame, width=300, height=40, placeholder_text="Nombre de usuario")
        self.user_register_entry.place(x=50, y=170)

        self.password_register_entry = ctk.CTkEntry(master=self.register_frame, width=300, height=40, placeholder_text="Ingrese su contraseña", show="×")
        self.password_register_entry.place(x=50, y=230)

        self.password_confirmed_entry = ctk.CTkEntry(master=self.register_frame, width=300, height=40, placeholder_text="Confirme su contraseña", show="×")
        self.password_confirmed_entry.place(x=50, y=290)

        self.button_register_Login = ctk.CTkButton(master=self.register_frame, width=300, height=40, text="Crear Usuario", command=self.register_logic)
        self.button_register_Login.place(x=50, y=350)

    def btn_x(self, event=None):
        self.root.withdraw()
        self.register_frame.destroy()
        login_window = ctk.CTkToplevel(self.root)
        Login(login_window)

    def register_logic(self, event=None):
        user_name = self.user_register_entry.get()
        password = self.password_register_entry.get()
        password_confirmed = self.password_confirmed_entry.get()

        if user_name != "" and password != "" and password == password_confirmed:
            datos = {"user_name": user_name, "password": password, "score_json": 0}  # Inicializar con el mejor puntaje como 0
            with open("users.json", "r") as file:
                usuarios = json.load(file)
            

            for usuario in usuarios:
                if usuario["user_name"] == user_name:
                    messagebox.showerror("Error", "El usuario ya existe")
                    break
            else:
                usuarios.append(datos)  # Si el usuario no existe, agrega los nuevos datos a la lista de usuarios
                with open("users.json", "w") as file:
                    json.dump(usuarios, file, indent=4)
                messagebox.showinfo("Registro", "Usuario registrado con éxito")
                self.register_frame.destroy()
                
                self.root.withdraw()  # Oculta la ventana principal de registro
                self.register_frame.destroy()  # Destruye el frame de registro
                login_window = ctk.CTkToplevel(self.root)
                Login(login_window) 
                

        elif user_name == "" or password == "" or password_confirmed == "":
            error_register = ctk.CTkLabel(master=self.register_frame, text="Hay campos vacíos", font=('Century Gothic', 12))
            error_register.place(x=140, y=340)
            self.button_register_Login.place(x=50, y=380)

        elif password != password_confirmed:
            self.error_register1 = ctk.CTkLabel(master=self.register_frame, text="Las contraseñas no son iguales", font=('Century Gothic', 12))
            self.error_register1.place(x=100, y=340)
            self.button_register_Login.place(x=50, y=380)


class Game2028:
    def __init__(self, ventana, user_name=None, score_json=None):
        self.ventana = ventana
        self.user_name = user_name
        self.score_json = score_json
        ventana.update_idletasks()
        self.x = ventana.winfo_screenwidth()
        self.y = ventana.winfo_screenheight()
        self.ventana.geometry(f"{self.x}x{self.y}+0+0")
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
        
        """{
            0: "#242424",
            2: "#f19c45", 4: "#f19c45",
            8: "#ee3d42",  16: "#ee3d42",
            32: "#edc951", 64: "#edc951",
            128: "#00a0b0", 256: "#00a0b0",
            512: "#6a4a3c", 1024: "#6a4a3c",
            2048: "#000"
            }"""
        self.menu_bar()
        self.sesions()
        self.footer()
        self.main_game()
        self.inicio()
        self.puntaje = 0
        self.mayor_puntuacion = 0
        ventana.bind('<Key>', self.flechas)

#-------------------------------------------------------------------------------------------------------------------------------------------------------   
    def menu_bar(self):
        #Nav bar         
        dificultad = ["Facil", "Media", "Dificil"]
        dificultad_options = ctk.CTkOptionMenu(master = self.ventana, values = dificultad
            , height = 40, fg_color = "#2c2c2c", button_color = "#2c2c2c"
            , button_hover_color = "#131313", anchor = "center", command = self.dificultad)
        dificultad_options.place(x = 70, y = 20)
 #-------------------------------------------------------------------------------------------------------------------------------------------------------   
    def sesions(self):
        self.sesion = ctk.CTkButton(master = self.ventana, text = "Iniciar sesion", fg_color = "transparent",
            border_color = "#2c2c2c", border_width = 3, hover_color = "#2c2c2c", height = 40,
            font = ('Arial', 12), command = self.login_game)
        self.sesion.place(x = self.x - 350, y = 20)
        
        self.register_btn = ctk.CTkButton(master = self.ventana, text = "Registrar", height = 40, font = ('Arial', 12), command = self.register_game)
        self.register_btn.place(x = self.x - 200, y = 20)
    def login_game(self, event=None):
        self.ventana.withdraw()
        login_window = ctk.CTkToplevel(self.ventana)
        Login(login_window)
    
    def register_game(self):
        self.ventana.withdraw()
        register_window = ctk.CTkToplevel(self.ventana)
        Register(register_window)
        
    def borrado_sesion_register(self):
        self.sesion.place_forget()
        self.register_btn.place_forget()
        if self.user_name:
            self.user_label = ctk.CTkLabel(master=self.ventana, text=self.user_name, font=('Arial Black', 20))
            self.user_label.place(x=self.x - 120, y=20)
            
            self.best.configure(text=str(self.score_json))

            self.cerrar_sesion_btn = ctk.CTkButton(master=self.ventana, text="Cerrar sesión", height=40, font=('Arial', 12), command=self.cerrar_sesion)
            self.cerrar_sesion_btn.place(x=self.x - 180, y= self.y - 130)
    
    def cerrar_sesion(self):
        self.ventana.withdraw()  # Oculta la ventana principal del juego
        self.cerrar_sesion_btn.place_forget()  # Oculta el botón de cerrar sesión

        # Destruye la instancia actual de Game2028 y vuelve a mostrar la ventana de inicio de sesión
        self.ventana_login = ctk.CTkToplevel(self.ventana)
        Login(self.ventana_login)
#-------------------------------------------------------------------------------------------------------------------------------------------------------      
    def main_game(self):
        self.frame_jueguito = ctk.CTkFrame(master = self.ventana, width= 450, height=545, corner_radius = 25)
        self.frame_jueguito.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)
        self.header()
        self.tablero()
 #-------------------------------------------------------------------------------------------------------------------------------------------------------             
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
        
        self.best = ctk.CTkLabel(best_frame, text = "", font = ('Arial Black', 20), text_color = "white", width = 85) #mejor puntaje
        self.best.grid(column = 1, row = 1, padx = 10)

#-------------------------------------------------------------------------------------------------------------------------------------------------------      
    def tablero(self):
        self.container_frame = ctk.CTkFrame(master = self.frame_jueguito)  # Frame hecho para pintar el padding del mismo color que el main xd
        self.container_frame.place(relx = 0.5, rely = 0.6, anchor = ctk.CENTER)
        
        self.main_frame = ctk.CTkFrame(master = self.container_frame)
        self.main_frame.pack(expand=True, fill=tk.BOTH)


        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                self.cuadro_tablero = ctk.CTkFrame(master=self.main_frame, width=100, height=100, corner_radius = 10, fg_color="transparent")
                self.cuadro_tablero.grid(row=row, column=col, padx = 5, pady=5, sticky="nsew")
                
                self.cuadro = ctk.CTkLabel(master=self.cuadro_tablero, text="", font=("Arial", 24, "bold"), width= 85, height=85, fg_color="#242424", corner_radius = 8)
                self.cuadro.grid(sticky="nsew")

                self.frame[row][col] = self.cuadro
#-------------------------------------------------------------------------------------------------------------------------------------------------------      
    def footer(self):
        self.reglas = ctk.CTkButton(master = self.ventana, text = "Reglas", fg_color = "transparent",
            border_color = "#2c2c2c", hover_color = "#2c2c2c", height = 40,
            font = ('Arial', 12), command = self.reglas_toplevel_ctk)
        self.reglas.place(relx = 0.5, y = self.y - 130, anchor = tk.CENTER)
    
    def reglas_toplevel_ctk(self):
        self.reglas_toplevel = ctk.CTkToplevel(self.ventana)
        self.reglas_toplevel.title("Reglas del Juego 2048")
        ventana.update_idletasks()
        ejex = (ventana.winfo_screenwidth() // 2)-(425 // 2)
        ejey = (ventana.winfo_screenheight() // 2)-(500 // 2)


        self.reglas_toplevel.geometry(f"400x300+{ejex}+{ejey}")

        reglas_texto = """
        Reglas del Juego 2048:
        
        1. Usa las flechas del teclado para mover las fichas.
        2. Cada vez que mueves, una nueva ficha aparece en un espacio vacío.
        3. Las fichas con el mismo número se combinan cuando chocan.
        4. El objetivo es crear una ficha con el número 2048.
        5. El juego termina cuando no hay más movimientos posibles.
        
        ¡Buena suerte y diviértete!
        """
        
        self.reglas_label = ctk.CTkLabel(self.reglas_toplevel, text=reglas_texto, wraplength=350, justify="left")
        self.reglas_label.pack(padx=20, pady=20)
       
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
        
        if self.user_name:
                with open("users.json", "r+") as file:
                    usuarios = json.load(file)
                    for usuario in usuarios:
                        if usuario["user_name"] == self.user_name:
                            usuario["score_json"] = self.mayor_puntuacion
                            file.seek(0)  # Mueve el puntero al inicio del archivo
                            json.dump(usuarios, file, indent=4)
                            break
        

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
            self.width_height = 85
        elif esternocleidomastoideo == "Media":
            self.grid = [[0] * 5 for _ in range(5)]
            self.frame_width = 550
            self.frame_height = 645
            self.width_height = 85
        elif esternocleidomastoideo == "Dificil":
            self.grid = [[0] * 6 for _ in range(6)]
            self.frame_width = 550
            self.frame_height = 645
            self.width_height = 65
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
        
        self.puntaje = 0
        self.score1.configure(text=str(self.puntaje))
        self.best.configure(text=str(self.mayor_puntuacion))
        
        self.cuadro_random()
        self.cuadro_random()
        self.update_grid()
        self.frame_jueguito.configure(width=self.frame_width, height=self.frame_height)
        for row in range(len(self.frame)):
            for col in range(len(self.frame[row])):
                cuadro = self.frame[row][col]
                if cuadro:
                    cuadro.configure(width=self.width_height, height=self.width_height)
        # = ctk.CTkLabel(master=self.cuadro_tablero, text="", font=("Arial", 24, "bold"), width= self.width_height, height=self.width_height, fg_color="#242424", corner_radius = 8)

#-------------------------------------------------------------------------------------------------------------------------------------------------------        
if __name__ == "__main__":
    # root = ctk.CTk()
    # Login(root)
    # root.mainloop()

    # menu_prin = ctk.CTk()
    # Menu_principal(menu_prin)
    # menu_prin.mainloop()

    ventana = ctk.CTk()
    Game2028(ventana)
    ventana.mainloop()
print("ᴍᴀᴅᴇ ʙʏ ᴍᴀᴜʀɪᴄɪᴏ ʟᴜᴄᴇʀᴏ")
