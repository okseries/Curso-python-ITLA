class Task:
    def __init__(
        self,
        id=None,
        titulo=None,
        descripcion=None,
        estado="pendiente",
        prioridad="baja",
    ):
        """
        Clase que representa una tarea.
        :param id: Identificador único de la tarea (por defecto None).
        :param titulo: Título de la tarea (por defecto None).
        :param descripcion: Descripción de la tarea (por defecto None).
        :param estado: Estado de la tarea ('pendiente' por defecto).
        :param prioridad: Prioridad de la tarea ('baja' por defecto).
        """
        self.id = id
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado
        self.prioridad = prioridad

    def __repr__(self):
        """
        Representación en forma de cadena de la tarea.
        """
        return (
            f"Task(id={self.id}, titulo='{self.titulo}', estado='{self.estado}', "
            f"prioridad='{self.prioridad}')"
        )

    def to_dict(self):
        """
        Convierte la tarea a un diccionario.
        """
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "estado": self.estado,
            "prioridad": self.prioridad,
        }

    @classmethod
    def from_dict(cls, data):
        """
        Crea una instancia de `Task` a partir de un diccionario.
        :param data: Diccionario con los datos de la tarea.
        :return: Instancia de Task.
        """
        return cls(
            id=data.get("id"),
            titulo=data.get("titulo"),
            descripcion=data.get("descripcion"),
            estado=data.get("estado", "pendiente"),
            prioridad=data.get("prioridad", "baja"),
        )
