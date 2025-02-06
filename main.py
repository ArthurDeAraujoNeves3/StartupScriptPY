import subprocess
import customtkinter
from time import sleep

# O 'r' no começo é para transforma a strin bruta, já que a '\' interpreta como formfeed (\f) 
# Coloque o nome do programe e o caminho para o .exe
programs = {
    "": {
        "path": r""
    },
}

colors = {
    "red": "#ff2c2c",
    "green": "#0BDA51",
    "white": "#FFFFFF"
}

# Tema da janela
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Configurações da tela
app = customtkinter.CTk()
app.geometry("700x300")
app.minsize(width=700, height=300)
app.title("Logs")

# def initializeScreenViewer():
def getProgram():
    errors = 0

    # key é o nome do programa
    for key in programs:
        errors = openProgram(key, programs[key]["path"], errors)
        sleep(2)
    
    # Se não houver erros, fechamos a janela
    if errors == 0:
        return app.quit()

def openProgram(name: str, path: str, errors: int):
    try:
        createMessage(text=f"Abrindo programa {name}...", error=False)
        subprocess.Popen(path)
    except:
        createMessage(text=f"{name} não encontrado. Caminho do executável incorreto \n {path}", error=True)
        errors += 1
        app.mainloop()

    return errors

def createMessage(text: str, error: bool):
    if error:
        return customtkinter.CTkLabel(app, wraplength=300, text=text, text_color=colors["white"], bg_color=colors["red"]).pack()
    
    return customtkinter.CTkLabel(app, wraplength=300, text=text).pack()
    
# Inicio
getProgram()
# app.mainloop()
