import tkinter as tk
import subprocess

def launch_snake():
    subprocess.Popen(['python', '-m', 'freegames.snake'])

def launch_pong():
    subprocess.Popen(['python', '-m', 'freegames.pong'])

root = tk.Tk()
root.title("Mini Consola Retro")

tk.Label(root, text="Selecciona un juego", font=('Arial', 18)).pack(pady=10)

tk.Button(root, text="🐍 Snake", width=20, command=launch_snake).pack(pady=5)
tk.Button(root, text="🏓 Pong", width=20, command=launch_pong).pack(pady=5)

root.mainloop()
