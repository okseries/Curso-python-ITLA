import os
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ReloadHandler(FileSystemEventHandler):
    def __init__(self, script_name):
        self.script_name = script_name
        self.process = None
        self.start_process()

    def start_process(self):
        """Inicia el proceso de la aplicación."""
        if self.process:
            self.process.terminate()
        self.process = subprocess.Popen(["python", self.script_name])

    def on_modified(self, event):
        """Reinicia el proceso cuando se detectan cambios."""
        if event.src_path.endswith(".py"):
            print(f"Detectado cambio en {event.src_path}. Reiniciando...")
            self.start_process()

    def stop_process(self):
        """Detiene el proceso antes de salir."""
        if self.process:
            self.process.terminate()

if __name__ == "__main__":
    script_to_watch = "main.py"  # Reemplaza con el nombre de tu archivo principal
    event_handler = ReloadHandler(script_to_watch)
    observer = Observer()
    observer.schedule(event_handler, ".", recursive=True)  # Observa el directorio actual
    observer.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        event_handler.stop_process()
        observer.stop()

    observer.join()
