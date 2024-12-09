import tkinter as tk
from tkinter import ttk, messagebox
from style.globalStyles import Colors
from gestorTarea.gestorTarea import GestorTarea

class EditTaskWindow:
    def __init__(self, root, on_save_callback, initial_data):
        """
        Ventana para editar una tarea existente.
        :param root: Ventana raíz o principal que actúa como padre.
        :param on_save_callback: Función a llamar cuando se guarden los cambios.
        :param initial_data: Diccionario con los datos iniciales de la tarea.
        """
        self.root = root
        self.window = tk.Toplevel(root)
        self.window.title("Editar Tarea")
        self.center_window(400, 350)  # Centrar la ventana secundaria
        self.window.config(bg=Colors.BACKGROUND_LIGHT)

        # Callback para guardar
        self.on_save_callback = on_save_callback

        # Datos iniciales
        self.initial_data = initial_data

        # Configurar UI
        self.setup_ui()

    def center_window(self, width, height):
        """
        Centra la ventana en la pantalla.
        """
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.window.geometry(f"{width}x{height}+{x}+{y}")

    def setup_ui(self):
        # Contenedor principal
        container = tk.Frame(self.window, bg=Colors.BACKGROUND_LIGHT)
        container.pack(expand=True, fill="both", padx=20, pady=20)

        # Campo de Título
        tk.Label(
            container,
            text="Título:",
            font=("Roboto", 12),
            bg=Colors.BACKGROUND_LIGHT,
            fg=Colors.TEXT_PRIMARY,
        ).grid(row=0, column=0, sticky="w", pady=10)
        self.title_entry = tk.Entry(container, font=("Roboto", 12), bg=Colors.BORDER_LIGHT, fg=Colors.TEXT_PRIMARY, relief="flat")
        self.title_entry.grid(row=0, column=1, pady=10, padx=10, sticky="ew")
        self.title_entry.insert(0, self.initial_data.get("titulo", ""))  # Cargar dato inicial

        # Campo de Descripción
        tk.Label(
            container,
            text="Descripción:",
            font=("Roboto", 12),
            bg=Colors.BACKGROUND_LIGHT,
            fg=Colors.TEXT_PRIMARY,
        ).grid(row=1, column=0, sticky="w", pady=10)
        self.description_entry = tk.Entry(container, font=("Roboto", 12), bg=Colors.BORDER_LIGHT, fg=Colors.TEXT_PRIMARY, relief="flat")
        self.description_entry.grid(row=1, column=1, pady=10, padx=10, sticky="ew")
        self.description_entry.insert(0, self.initial_data.get("descripcion", ""))  # Cargar dato inicial

        # Desplegable de Estado
        tk.Label(
            container,
            text="Estado:",
            font=("Roboto", 12),
            bg=Colors.BACKGROUND_LIGHT,
            fg=Colors.TEXT_PRIMARY,
        ).grid(row=2, column=0, sticky="w", pady=10)
        self.status_combobox = ttk.Combobox(
            container,
            values=["Pendiente", "En Progreso", "Completada"],
            state="readonly",
            font=("Roboto", 12),
        )
        self.status_combobox.grid(row=2, column=1, pady=10, padx=10, sticky="ew")
        self.status_combobox.set(self.initial_data.get("estado", "Pendiente"))  # Cargar dato inicial

        # Desplegable de Prioridad
        tk.Label(
            container,
            text="Prioridad:",
            font=("Roboto", 12),
            bg=Colors.BACKGROUND_LIGHT,
            fg=Colors.TEXT_PRIMARY,
        ).grid(row=3, column=0, sticky="w", pady=10)
        self.priority_combobox = ttk.Combobox(
            container,
            values=["Baja", "Media", "Alta"],
            state="readonly",
            font=("Roboto", 12),
        )
        self.priority_combobox.grid(row=3, column=1, pady=10, padx=10, sticky="ew")
        self.priority_combobox.set(self.initial_data.get("prioridad", "Baja"))  # Cargar dato inicial

        # Botones Guardar y Cancelar
        button_frame = tk.Frame(container, bg=Colors.BACKGROUND_LIGHT)
        button_frame.grid(row=4, column=0, columnspan=2, pady=20)

        save_button = tk.Button(
            button_frame,
            text="Guardar Cambios",
            font=("Roboto", 12, "bold"),
            bg=Colors.BUTTON_PRIMARY,
            fg=Colors.WHITE,
            relief="flat",
            command=self.save_task,
        )
        save_button.pack(side="left", padx=15, ipadx=10, ipady=5)

        cancel_button = tk.Button(
            button_frame,
            text="Cancelar",
            font=("Roboto", 12, "bold"),
            bg=Colors.BUTTON_SECONDARY,
            fg=Colors.WHITE,
            relief="flat",
            command=self.window.destroy,
        )
        cancel_button.pack(side="left", padx=15, ipadx=10, ipady=5)

        # Ajustar columnas para un diseño más limpio
        container.grid_columnconfigure(1, weight=1)

    def save_task(self):
        """
        Valida y guarda los cambios realizados en la tarea.
        """
        titulo = self.title_entry.get().strip()
        descripcion = self.description_entry.get().strip()
        estado = self.status_combobox.get()
        prioridad = self.priority_combobox.get()

        if not titulo:
            messagebox.showerror("Error", "El título es obligatorio.")
            return

        if estado not in ["Pendiente", "En Progreso", "Completada"]:
            messagebox.showerror("Error", "El estado seleccionado no es válido.")
            return

        if prioridad not in ["Alta", "Media", "Baja"]:
            messagebox.showerror("Error", "La prioridad seleccionada no es válida.")
            return

        try:
            # Llama al callback para guardar los cambios
            self.on_save_callback(titulo, descripcion, estado, prioridad)
            messagebox.showinfo("Éxito", "Los cambios se han guardado correctamente.")
            self.window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron guardar los cambios: {str(e)}")
