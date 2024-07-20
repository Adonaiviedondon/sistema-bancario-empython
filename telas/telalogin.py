import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.style import Style

tela1 = ttk.Window("telalogin")
tela1.geometry("700x500")
estilo = Style(theme="superhero")
tela1.resizable(width=False,height=False)

tela1.mainloop()