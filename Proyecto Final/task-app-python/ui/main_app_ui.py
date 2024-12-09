import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.filedialog import asksaveasfilename, askopenfilename
import csv
from style.globalStyles import Colors
from ui.createTaskWindow import CreateTaskWindow
from ui.editTaskWindow import EditTaskWindow
from gestorTarea.gestorTarea import GestorTarea


class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")
        self.center_window(1100, 600)
        self.root.config(bg=Colors.BACKGROUND_LIGHT)
        self.setup_ui()

    def center_window(self, width, height):
        """
        Centra la ventana principal en la pantalla.
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

        # TITULO
        header = tk.Label(
            container,
            text="Gestión de Tareas",
            font=("Roboto", 24, "bold"),
            bg=Colors.PRIMARY,
            fg=Colors.WHITE,
        )
        header.pack(pady=10, fill="x")

        # Filtros
        self.setup_filters(container)

        # Listado de tareas
        self.setup_task_list(container)

        # Botones de acción
        self.setup_buttons(container)

        # Cargar tareas al iniciar
        self.load_tasks()

    def setup_filters(self, container):
        filter_frame = tk.Frame(container, bg=Colors.SECONDARY)
        filter_frame.pack(pady=10, padx=10, fill="x")

        tk.Label(
            filter_frame,
            text="Filtrar por título:",
            font=("Roboto", 12),
            bg=Colors.SECONDARY,
            fg=Colors.TEXT_PRIMARY,
        ).grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.title_filter = tk.Entry(filter_frame, font=("Roboto", 12))
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

    def setup_task_list(self, container):
        self.task_list = ttk.Treeview(
            container,
            columns=("ID", "TITULO", "DESCRIPCION", "ESTADO", "PRIORIDAD"),
            show="headings",
        )
        for col, width in [("ID", 50), ("TITULO", 200), ("DESCRIPCION", 300), ("ESTADO", 100), ("PRIORIDAD", 100)]:
            self.task_list.heading(col, text=col)
            self.task_list.column(col, width=width, anchor="center")

        self.task_list.pack(pady=10, padx=10, expand=True, fill="both")

    def setup_buttons(self, container):
        action_frame = tk.Frame(container, bg=Colors.BACKGROUND_LIGHT)
        action_frame.pack(fill="x", pady=10, padx=10)

        tk.Button(
            action_frame,
            text="Agregar",
            font=("Roboto", 14, "bold"),
            bg=Colors.SUCCESS,
            fg=Colors.WHITE,
            relief="flat",
            command=self.open_create_task_window,
        ).pack(side="left", padx=5, ipadx=10, ipady=5)

        tk.Button(
            action_frame,
            text="Editar",
            font=("Roboto", 14, "bold"),
            bg=Colors.WARNING,
            fg=Colors.WHITE,
            relief="flat",
            command=self.open_edit_task_window,
        ).pack(side="left", padx=5, ipadx=10, ipady=5)

        tk.Button(
            action_frame,
            text="Eliminar",
            font=("Roboto", 14, "bold"),
            bg=Colors.ERROR,
            fg=Colors.WHITE,
            relief="flat",
            command=self.delete_task,
        ).pack(side="left", padx=5, ipadx=10, ipady=5)

        tk.Button(
            action_frame,
            text="Exportar csv",
            font=("Roboto", 14, "bold"),
            bg=Colors.BUTTON_PRIMARY,
            fg=Colors.WHITE,
            relief="flat",
            command=self.export_tasks,
        ).pack(side="right", padx=5, ipadx=10, ipady=5)

        tk.Button(
            action_frame,
            text="Importar csv",
            font=("Roboto", 14, "bold"),
            bg=Colors.BUTTON_PRIMARY,
            fg=Colors.WHITE,
            relief="flat",
            command=self.import_tasks,
        ).pack(side="right", padx=5, ipadx=10, ipady=5)

    def load_tasks(self):
        self.task_list.delete(*self.task_list.get_children())
        tasks = GestorTarea.get_all()
        for task in tasks:
            self.task_list.insert("", "end", values=(task.id, task.titulo, task.descripcion, task.estado, task.prioridad))

    def apply_filters(self):
        """
        Aplica los filtros seleccionados por el usuario y actualiza el TreeView.
        """
        titulo = self.title_filter.get().strip()
        estado = self.status_filter.get()
        prioridad = self.priority_filter.get()

        # Ajustar valores para coincidir con la base de datos
        estado = None if estado == "Todos" else estado
        prioridad = None if prioridad == "Todos" else prioridad

        tasks = GestorTarea.get_all(titulo=titulo, estado=estado, prioridad=prioridad)
        self.task_list.delete(*self.task_list.get_children())
        for task in tasks:
            self.task_list.insert("", "end", values=(task.id, task.titulo, task.descripcion, task.estado, task.prioridad))


    def delete_task(self):
        selected_items = self.task_list.selection()
        if not selected_items:
            messagebox.showerror("Error", "Selecciona una tarea para eliminar.")
            return

        confirm = messagebox.askyesno("Eliminar Tarea", "¿Estás seguro de eliminar la tarea seleccionada?")
        if confirm:
            for item in selected_items:
                task_id = self.task_list.item(item)["values"][0]
                if GestorTarea.delete(task_id):
                    self.task_list.delete(item)
                else:
                    messagebox.showerror("Error", f"No se pudo eliminar la tarea con ID: {task_id}")

    def open_create_task_window(self):
        def save_callback(id, titulo, descripcion, estado, prioridad):
            self.load_tasks()

        CreateTaskWindow(self.root, save_callback)
        
        

    def open_edit_task_window(self):
        """
        Abre una ventana para editar la tarea seleccionada.
        """
        selected_items = self.task_list.selection()
        if not selected_items:
            messagebox.showerror("Error", "Selecciona una tarea para editar.")
            return

        task_id = self.task_list.item(selected_items[0])["values"][0]

        # Obtener la tarea por ID
        task = GestorTarea.get_by_id(task_id)
        if not task:
            messagebox.showerror("Error", "No se encontró la tarea seleccionada.")
            return

        def save_callback(titulo, descripcion, estado, prioridad):
            """
            Callback para guardar cambios de la tarea.
            """
            success = GestorTarea.update(task_id, titulo=titulo, descripcion=descripcion, estado=estado, prioridad=prioridad)
            if success:
                messagebox.showinfo("Éxito", "Tarea actualizada correctamente.")
                self.load_tasks()  # Recargar tareas en la tabla
            else:
                messagebox.showerror("Error", "No se pudo actualizar la tarea.")

        # Abrir la ventana para editar
        EditTaskWindow(self.root, save_callback, initial_data={
            "titulo": task.titulo,
            "descripcion": task.descripcion,
            "estado": task.estado,
            "prioridad": task.prioridad,
        })

        
        
        
    def mark_task_as_completed(self):
        """
        Marca la tarea seleccionada como completada.
        """
        selected_items = self.task_list.selection()
        if not selected_items:
            messagebox.showerror("Error", "Selecciona una tarea para marcar como completada.")
            return

        for item in selected_items:
            task_id = self.task_list.item(item)["values"][0]
            success = GestorTarea.mark_as_completed(task_id)
            if success:
                messagebox.showinfo("Éxito", f"Tarea con ID {task_id} marcada como completada.")
            else:
                messagebox.showerror("Error", f"No se pudo completar la tarea con ID: {task_id}")

        self.load_tasks()  # Recargar tareas en la tabla




    def export_tasks(self):
        file_path = asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if not file_path:
            return

        with open(file_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "TITULO", "DESCRIPCION", "ESTADO", "PRIORIDAD"])
            for row in self.task_list.get_children():
                writer.writerow(self.task_list.item(row)["values"])

        messagebox.showinfo("Éxito", f"Tareas exportadas a {file_path}")

    def import_tasks(self):
        file_path = askopenfilename(filetypes=[("CSV files", "*.csv")])
        if not file_path:
            return

        with open(file_path, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                GestorTarea.create(
                    titulo=row["TITULO"],
                    descripcion=row["DESCRIPCION"],
                    estado=row["ESTADO"],
                    prioridad=row["PRIORIDAD"],
                )

        messagebox.showinfo("Éxito", "Tareas importadas correctamente.")
        self.load_tasks()


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
