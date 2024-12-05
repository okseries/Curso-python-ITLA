import sqlite3
import os

class Database:
    def __init__(self, db_name="data/task.db"):
        """
        Inicializa la conexión a la base de datos y asegura que la tabla esté creada.
        """
        self.db_name = db_name

        # Crear el directorio si no existe
        os.makedirs(os.path.dirname(db_name), exist_ok=True)

        # Conectar a la base de datos
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        """
        Crea la tabla 'task' si no existe.
        """
        query = """
        CREATE TABLE IF NOT EXISTS task (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descripcion TEXT,
            estado TEXT CHECK(estado IN ('Pendiente', 'Completada')) NOT NULL DEFAULT 'Pendiente',
            prioridad TEXT CHECK(prioridad IN ('Baja', 'Media', 'Alta')) NOT NULL DEFAULT 'Baja'
        );
        """
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()

    def close(self):
        """
        Cierra la conexión con la base de datos.
        """
        self.connection.close()
