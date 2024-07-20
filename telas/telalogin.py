import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.style import Style


tela1 = ttk.Window("telalogin")
tela1.geometry("500x400")
estilo = Style(theme="superhero")
tela1.resizable(width=False,height=False)
tela1.configure(background="#00FF00")

titulo = ttk.Label(tela1, text="Adonix-Pay",foreground="#FFFFFF",background="#00FF00")
titulo.pack(pady=30)
titulo.config(font=("calibri",35,"bold"))

login = ttk.Frame(tela1)
login.pack(pady=20,padx=13,fill="x")
ttk.Label(login, text="login").pack(side=LEFT,padx=5)
ttk.Entry(login).pack(side=LEFT,fill="x",padx=5,expand=True)

senha = ttk.Frame(tela1)
senha.pack(pady=20,padx=13,fill="x")
ttk.Label(senha, text="senha").pack(side=LEFT,padx=5)
ttk.Entry(senha).pack(side=LEFT,fill="x",padx=5,expand=True)

entrar = ttk.Frame(tela1)
entrar.pack(pady=32,padx=12)
ttk.Button(entrar,text="entrar").pack(side=LEFT,padx=18)

tela1.mainloop()