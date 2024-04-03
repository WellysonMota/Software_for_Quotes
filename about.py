import tkinter as tk


def about():
    janela_about = tk.Tk()
    janela_about.title("Sobre este Programa")
    janela_about.geometry("480x240")

    label = tk.Label(janela_about, text="Olá, este programa foi desenvolvido por Welly Mota")
    label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    label = tk.Label(janela_about, text="Version: 1.0")
    label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    janela_about.mainloop()
