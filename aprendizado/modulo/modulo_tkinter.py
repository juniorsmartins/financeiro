import tkinter as tk

# Criar Janela
window = tk.Tk()
window.geometry("1200x800")
window.title("Gerencia Frases")

# Adicionar frame
frame = tk.Frame(window)
frame.pack(padx=10, pady=10, fill='x', expand=True)

# Adicionar Label
label = tk.Label(frame, text="Olá, Mundo!")
label.pack(fill='x', expand=True)

# Adicionar input text
frase_lab = tk.Label(frame, text="Frase")
frase_lab.pack(fill='x', expand=True)

frase_inp = tk.Entry(frame)
frase_inp.pack(fill='x', expand=True)

# Criar função para alterar texto do label
def click():
    label.config(text=frase_inp.get())

# Adicionar botão de enviar
button = tk.Button(frame, text="Enviar", command=click)
button.pack()


window.mainloop()








