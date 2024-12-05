import tkinter as tk
from ui.main_app_ui import MainApp
from style.globalStyles import Colors

if __name__ == "__main__":
    # Iniciar la aplicación
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
