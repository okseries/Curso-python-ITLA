import tkinter as tk

class Placeholder:
    def __init__(self, entry, placeholder_text, placeholder_color="gray", text_color="black"):
        """
        Clase para manejar el comportamiento de placeholder en un Entry.

        :param entry: El widget Entry de Tkinter.
        :param placeholder_text: El texto del placeholder.
        :param placeholder_color: El color del texto del placeholder.
        :param text_color: El color del texto real.
        """
        self.entry = entry
        self.placeholder_text = placeholder_text
        self.placeholder_color = placeholder_color
        self.text_color = text_color

        # Configurar el placeholder inicial
        self.add_placeholder(None)

        # Enlazar eventos para manejar el placeholder
        self.entry.bind("<FocusIn>", self.clear_placeholder)
        self.entry.bind("<FocusOut>", self.add_placeholder)

    def clear_placeholder(self, event):
        """
        Borra el placeholder cuando el Entry recibe el foco.
        """
        if self.entry.get() == self.placeholder_text:
            self.entry.delete(0, tk.END)
            self.entry.config(fg=self.text_color)

    def add_placeholder(self, event):
        """
        Restaura el placeholder si el Entry está vacío al perder el foco.
        """
        if not self.entry.get():  # Si está vacío
            self.entry.insert(0, self.placeholder_text)
            self.entry.config(fg=self.placeholder_color)
