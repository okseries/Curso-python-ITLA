import tkinter as tk
from tkinter import ttk
from style.globalStyles import Colors
from ui.createTaskWindow import CreateTaskWindow
from gestorTarea.gestorTarea import GestorTarea


class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")
        self.center_window(1100, 600)  # Centrar la ventana principal
        self.root.config(bg=Colors.BACKGROUND_LIGHT)

        # Configurar UI principal
        self.setup_ui()

    def center_window(self, width, height):
        """
        Centra la ventana principal en la pantalla.
        :param width: Ancho de la ventana
        :param height: Alto de la ventana
        """
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def setup_ui(self):
        # Contenedor principal
        container = tk.Frame(self.root, bg=Colors.BACKGROUND_LIGHT)
        container.pack(expand=True, fill="both")

        # Título
        header = tk.Label(
            container,
            text="Gestión de Tareas",
            font=("Roboto", 24, "bold"),
            bg=Colors.PRIMARY,
            fg=Colors.WHITE,
        )
        header.pack(pady=10, fill="x")

        # Filtros
        filter_frame = tk.Frame(container, bg=Colors.SECONDARY)
        filter_frame.pack(pady=10, padx=10, fill="x")

        tk.Label(
            filter_frame,
            text="Filtrar por título:",
            font=("Roboto", 12),
            bg=Colors.SECONDARY,
            fg=Colors.TEXT_PRIMARY,
        ).grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.title_filter = tk.Entry(filter_frame, font=("Roboto", 12), bg=Colors.BACKGROUND_LIGHT, fg=Colors.TEXT_PRIMARY, relief="flat")
        self.title_filter.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        tk.Label(
            filter_frame,
            text="Estado:",
            font=("Roboto", 12),
            bg=Colors.SECONDARY,
            fg=Colors.TEXT_PRIMARY,
        ).grid(row=0, column=2, padx=10, pady=5, sticky="w")

        self.status_filter = ttk.Combobox(
            filter_frame,
            values=["Todos", "Pendiente", "Completada"],
            state="readonly",
            font=("Roboto", 12),
        )
        self.status_filter.grid(row=0, column=3, padx=10, pady=5, sticky="ew")
        self.status_filter.set("Todos")

        tk.Label(
            filter_frame,
            text="Prioridad:",
            font=("Roboto", 12),
            bg=Colors.SECONDARY,
            fg=Colors.TEXT_PRIMARY,
        ).grid(row=0, column=4, padx=10, pady=5, sticky="w")

        self.priority_filter = ttk.Combobox(
            filter_frame,
            values=["Todos", "Baja", "Media", "Alta"],
            state="readonly",
            font=("Roboto", 12),
        )
        self.priority_filter.grid(row=0, column=5, padx=10, pady=5, sticky="ew")
        self.priority_filter.set("Todos")

        # Botón de Filtrar
        filter_button = tk.Button(
            filter_frame,
            text="Aplicar Filtro",
            font=("Roboto", 12, "bold"),
            bg=Colors.BUTTON_SECONDARY,
            fg=Colors.WHITE,
            relief="flat",
            command=self.apply_filters,
        )
        filter_button.grid(row=0, column=6, padx=10, pady=5)

        # Listado de tareas
        self.task_list = ttk.Treeview(
            container,
            columns=("ID", "Título", "Descripción", "Estado", "Prioridad"),
            show="headings",
        )
        self.task_list.heading("ID", text="ID")
        self.task_list.heading("Título", text="Título")
        self.task_list.heading("Descripción", text="Descripción")
        self.task_list.heading("Estado", text="Estado")
        self.task_list.heading("Prioridad", text="Prioridad")

        # Ajustar tamaño de columnas
        self.task_list.column("ID", width=50, anchor="w")
        self.task_list.column("Título", width=200, anchor="w")
        self.task_list.column("Descripción", width=300, anchor="w")
        self.task_list.column("Estado", width=100, anchor="center")
        self.task_list.column("Prioridad", width=100, anchor="center")

        self.task_list.pack(pady=10, padx=10, expand=True, fill="both")
        
        
        # Contenedor principal para los botones (fila única)
        action_container = tk.Frame(container)
        action_container.pack(fill="x", pady=10, padx=10)

        # Contenedor para botones CRUD (izquierda)
        button_crud = tk.Frame(action_container, bg=Colors.BACKGROUND_LIGHT)
        button_crud.pack(side="left", fill="x", expand=True )

        # Contenedor para botones Archivo (derecha)
        button_file = tk.Frame(action_container, bg=Colors.BACKGROUND_LIGHT)
        button_file.pack(side="left", fill="x", expand=True, )

        # Botones CRUD
        add_task_button = tk.Button(
            button_crud,
            text="Agregar",
            font=("Roboto", 14, "bold"),
            bg=Colors.SUCCESS,
            fg=Colors.WHITE,
            relief="flat",
            command=self.open_create_task_window,
        )
        add_task_button.pack(side="left", padx=5, ipadx=10, ipady=5)

        edit_task_button = tk.Button(
            button_crud,
            text="Editar",
            font=("Roboto", 14, "bold"),
            bg=Colors.WARNING,
            fg=Colors.WHITE,
            relief="flat",
            command=self.open_create_task_window,
        )
        edit_task_button.pack(side="left", padx=5, ipadx=10, ipady=5)

        delete_task_button = tk.Button(
            button_crud,
            text="Eliminar",
            font=("Roboto", 14, "bold"),
            bg=Colors.ERROR,
            fg=Colors.WHITE,
            relief="flat",
            command=self.delete_task,
        )
        delete_task_button.pack(side="left", padx=5, ipadx=10, ipady=5)

        # Botones Archivo
        export_task_button = tk.Button(
            button_file,
            text="Exportar",
            font=("Roboto", 14, "bold"),
            bg=Colors.BUTTON_SECONDARY,
            fg=Colors.WHITE,
            relief="flat",
            command=self.open_create_task_window,
        )
        export_task_button.pack(side="right", padx=5, ipadx=10, ipady=5)

        import_task_button = tk.Button(
            button_file,
            text="Importar",
            font=("Roboto", 14, "bold"),
            bg=Colors.BUTTON_SECONDARY,
            fg=Colors.WHITE,
            relief="flat",
            command=self.open_create_task_window,
        )
        import_task_button.pack(side="right", padx=5, ipadx=10, ipady=5)

        
         # Cargar tareas al iniciar
        self.load_tasks()
    
    def delete_task(self):
        selected_items = self.task_list.selection()  # Obtener los ítems seleccionados
        if not selected_items:
            tk.messagebox.showerror("Error", "Por favor, selecciona una tarea para eliminar.")
            return

        confirm = tk.messagebox.askyesno("Eliminar Tarea", "¿Estás seguro de eliminar la tarea seleccionada?")
        if confirm:
            for item in selected_items:
                task_values = self.task_list.item(item)["values"]
                task_id = task_values[0]  # Asegúrate de que el ID está en la primera columna
                success = GestorTarea.delete(task_id)
                if success:
                    self.task_list.delete(item)  # Elimina del Treeview
                else:
                    tk.messagebox.showerror("Error", f"No se pudo eliminar la tarea con ID: {task_id}")


        
    def load_tasks(self):
        """
        Carga todas las tareas desde la base de datos y las muestra en el Treeview.
        """
        # Limpia la lista actual
        for item in self.task_list.get_children():
            self.task_list.delete(item)

        # Obtén todas las tareas
        tasks = GestorTarea.get_all()
        for task in tasks:
            self.task_list.insert(
                "", "end", values=(task.id, task.titulo, task.descripcion, task.estado, task.prioridad)
            )

    def apply_filters(self):
        """
        Lógica para aplicar filtros en la base de datos y actualizar el Treeview.
        """
        titulo = self.title_filter.get().strip()
        estado = self.status_filter.get()
        prioridad = self.priority_filter.get()

        # Obtener tareas filtradas
        tasks = GestorTarea.get_all(titulo=titulo, estado=estado, prioridad=prioridad)
        

        # Actualizar el Treeview
        self.task_list.delete(*self.task_list.get_children())  # Limpiar el Treeview actual
        for task in tasks:
            self.task_list.insert("", "end", values=(task.id, task.titulo, task.descripcion, task.estado, task.prioridad))

            """
            Lógica para filtrar tareas por título, estado y prioridad.
            """
            title = self.title_filter.get().lower()
            status = self.status_filter.get()
            priority = self.priority_filter.get()

            # Lógica de filtrado se conectará con la base de datos.
            print(f"Filtrando por título: {title}, estado: {status}, prioridad: {priority}")

    def open_create_task_window(self):
        def save_callback(id, title, description, status, priority):
            # Agrega la tarea al listado y opcionalmente a la base de datos
            print(f"Tarea guardada: {id}, {title}, {description}, {status}, {priority}")
            self.task_list.insert("", "end", values=(id, title, description, status, priority))

        CreateTaskWindow(self.root, save_callback)


if __name__ == "__main__":
    from style.globalStyles import Colors  # Asegúrate de tener esta clase configurada
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
