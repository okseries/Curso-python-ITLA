from database.database import Database
from models.task import Task

class GestorTarea:
    @staticmethod
    def create(titulo, descripcion, estado="pendiente", prioridad="baja"):
        db = Database()
        query = """
        INSERT INTO task (titulo, descripcion, estado, prioridad)
        VALUES (?, ?, ?, ?)
        """
        try:
            cursor = db.connection.cursor()
            cursor.execute(query, (titulo, descripcion, estado, prioridad))
            db.connection.commit()
            task_id = cursor.lastrowid
            return Task(
                id=task_id,
                titulo=titulo,
                descripcion=descripcion,
                estado=estado,
                prioridad=prioridad,
            )
        except Exception as e:
            print(f"Error creando la tarea: {e}")
        finally:
            db.close()

    @staticmethod
    def get_all(titulo=None, estado=None, prioridad=None):
        db = Database()
        query = """
        SELECT * FROM task
        WHERE 1=1
        """
        params = []

        # Agregar filtros dinámicos
        if titulo:
            query += " AND titulo LIKE ?"
            params.append(f"%{titulo}%")
        if estado:
            query += " AND estado = ?"
            params.append(estado)
        if prioridad:
            query += " AND prioridad = ?"
            params.append(prioridad)

        try:
            cursor = db.connection.cursor()
            cursor.execute(query, params)
            rows = cursor.fetchall()
            tasks = [Task(*row) for row in rows]
            return tasks
        except Exception as e:
            print(f"Error obteniendo tareas con filtros: {e}")
            return []
        finally:
            db.close()
            
    @staticmethod
    def get_by_id(task_id):
        """
        Obtiene una tarea específica por su ID.
        """
        db = Database()
        query = """
        SELECT * FROM task WHERE id = ?
        """
        try:
            cursor = db.connection.cursor()
            cursor.execute(query, (task_id,))
            row = cursor.fetchone()
            if row:
                return Task(*row)  # Crear un objeto Task a partir del resultado
            return None  # Devolver None si no se encuentra la tarea
        except Exception as e:
            print(f"Error obteniendo la tarea con ID {task_id}: {e}")
            return None
        finally:
            db.close()



    @staticmethod
    def get_by_estado(estado):
        db = Database()
        query = """
        SELECT * FROM task WHERE estado = ?
        """
        try:
            cursor = db.connection.cursor()
            cursor.execute(query, (estado,))
            rows = cursor.fetchall()
            tasks = [Task(*row) for row in rows]
            return tasks
        except Exception as e:
            print(f"Error filtrando por estado: {e}")
            return []
        finally:
            db.close()

    @staticmethod
    def get_by_prioridad(prioridad):
        db = Database()
        query = """
        SELECT * FROM task WHERE prioridad = ?
        """
        try:
            cursor = db.connection.cursor()
            cursor.execute(query, (prioridad,))
            rows = cursor.fetchall()
            tasks = [Task(*row) for row in rows]
            return tasks
        except Exception as e:
            print(f"Error filtrando por prioridad: {e}")
            return []
        finally:
            db.close()

    @staticmethod
    def update(task_id, titulo=None, descripcion=None, estado=None, prioridad=None):
        db = Database()
        query = """
        UPDATE task
        SET titulo = COALESCE(?, titulo),
            descripcion = COALESCE(?, descripcion),
            estado = COALESCE(?, estado),
            prioridad = COALESCE(?, prioridad)
        WHERE id = ?
        """
        try:
            cursor = db.connection.cursor()
            cursor.execute(query, (titulo, descripcion, estado, prioridad, task_id))
            db.connection.commit()
            return cursor.rowcount > 0  # Devuelve True si se actualizó la fila
        except Exception as e:
            print(f"Error actualizando la tarea: {e}")
            return False
        finally:
            db.close()

    @staticmethod
    def delete(task_id):
        db = Database()
        query = """
        DELETE FROM task WHERE id = ?
        """
        try:
            cursor = db.connection.cursor()
            cursor.execute(query, (task_id,))
            db.connection.commit()
            return cursor.rowcount > 0  # Devuelve True si se eliminó la fila
        except Exception as e:
            print(f"Error eliminando la tarea: {e}")
            return False
        finally:
            db.close()

    @staticmethod
    def mark_as_completed(task_id):
        db = Database()
        query = """
        UPDATE task SET estado = 'Completada' WHERE id = ?
        """
        try:
            cursor = db.connection.cursor()
            cursor.execute(query, (task_id,))
            db.connection.commit()
            return cursor.rowcount > 0  # Devuelve True si se actualizó la fila
        except Exception as e:
            print(f"Error marcando la tarea como completada: {e}")
            return False
        finally:
            db.close()

