import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Mi Proyecto Retro")
    label = tk.Label(root, text="¡Hola, Tkinter funciona!", font=("Arial", 24))
    label.pack(pady=20)
    root.mainloop()

if __name__ == "__main__":
    main()
# Este script de prueba verifica si tkinter funciona correctamente
# al crear una ventana simple con un mensaje.
# Si ves la ventana con el mensaje, tkinter está funcionando correctamente.
# Si no ves la ventana, asegúrate de que tkinter esté instalado y configurado correctamente en tu entorno de Python.    
# Puedes instalar tkinter en tu entorno virtual con:
# pip install tk
# Si estás usando Python 3, tkinter debería estar incluido por defecto.