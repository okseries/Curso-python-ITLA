import csv

class HistorialTemperatura:
    def __init__(self):
        self.registros = []

    def agregar_registro(self, conversion, resultado):
        self.registros.append({"conversion": conversion, "resultado": resultado})

    def ver_historial(self):
        return self.registros

    def exportar_csv(self, archivo):
        with open(archivo, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["conversion", "resultado"])
            writer.writeheader()
            writer.writerows(self.registros)
