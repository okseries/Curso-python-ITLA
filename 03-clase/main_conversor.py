from conversor_temperatura import celsius, fahrenheit, kelvin
from conversor_longitud import metros, kilometros, pies, millas
from historiales import HistorialLongitud, HistorialTemperatura
import csv

historial_temperatura = HistorialTemperatura()
historial_longitud = HistorialLongitud()

def mostrar_encabezado(titulo):
    print("\n" + "-" * 40)
    print(f"{titulo}".center(40))
    print("-" * 40)

def ver_historial():
    mostrar_encabezado("Ver Historial")
    print("\n1. Historial de Temperatura")
    print("2. Historial de Longitud")
    print("3. Historial Completo\n")
    opcion = input("Elige una opción: ")

    if opcion == '1':
        print("\nHistorial de Temperatura:\n")
        for item in historial_temperatura.ver_historial():
            print(f"Conversión: {item['conversion']} -> Resultado: {item['resultado']}\n")
    elif opcion == '2':
        print("\nHistorial de Longitud:\n")
        for item in historial_longitud.ver_historial():
            print(f"Conversión: {item['conversion']} -> Resultado: {item['resultado']}\n")
    elif opcion == '3':
        print("\nHistorial Completo:\n")
        print("Historial de Temperatura:\n")
        for item in historial_temperatura.ver_historial():
            print(f"Conversión: {item['conversion']} -> Resultado: {item['resultado']}\n")
        print("\nHistorial de Longitud:\n")
        for item in historial_longitud.ver_historial():
            print(f"Conversión: {item['conversion']} -> Resultado: {item['resultado']}\n")
    else:
        print("\nOpción no válida.\n")

def exportar_historial():
    mostrar_encabezado("Exportar Historial")
    print("\n1. Exportar Historial de Temperatura")
    print("2. Exportar Historial de Longitud")
    print("3. Exportar Historial Completo\n")
    opcion = input("Elige una opción: ")

    try:
        if opcion == '1':
            historial_temperatura.exportar_csv("historial_temperatura.csv")
            print("\nHistorial de Temperatura exportado con éxito.\n")
        elif opcion == '2':
            historial_longitud.exportar_csv("historial_longitud.csv")
            print("\nHistorial de Longitud exportado con éxito.\n")
        elif opcion == '3':
            with open("historial_completo.csv", mode='w', newline='') as file:
                fieldnames = ["Tipo", "Conversión", "Resultado"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for item in historial_temperatura.ver_historial():
                    writer.writerow({"Tipo": "Temperatura", "Conversión": item['conversion'], "Resultado": item['resultado']})
                for item in historial_longitud.ver_historial():
                    writer.writerow({"Tipo": "Longitud", "Conversión": item['conversion'], "Resultado": item['resultado']})
            print("\nHistorial Completo exportado con éxito en 'historial_completo.csv'.\n")
        else:
            print("\nOpción no válida.\n")
    except Exception as e:
        print(f"\nError al exportar historial: {e}\n")

def main():
    while True:
        mostrar_encabezado("Bienvenido al Conversor de Unidades")
        print("\n1. Convertir Temperatura")
        print("2. Convertir Longitud")
        print("3. Ver Historial")
        print("4. Exportar Historial")
        print("5. Salir\n")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            mostrar_encabezado("Conversión de Temperatura")
            print("\n1. Celsius a Fahrenheit o Kelvin")
            print("2. Fahrenheit a Celsius o Kelvin")
            print("3. Kelvin a Celsius o Fahrenheit\n")
            sub_opcion = input("Elige una opción (1, 2 o 3): ")
            cantidad = float(input("\nIntroduce la cantidad: "))

            if sub_opcion == '1':
                resultado_f = celsius.celsius_a_fahrenheit(cantidad)
                resultado_k = celsius.celsius_a_kelvin(cantidad)
                print(f"\n{cantidad} °C a Fahrenheit: {resultado_f} °F")
                print(f"{cantidad} °C a Kelvin: {resultado_k} K\n")
                historial_temperatura.agregar_registro(
                    f"{cantidad} °C", f"{resultado_f} °F, {resultado_k} K"
                )
            elif sub_opcion == '2':
                resultado_c = fahrenheit.fahrenheit_a_celsius(cantidad)
                resultado_k = fahrenheit.fahrenheit_a_kelvin(cantidad)
                print(f"\n{cantidad} °F a Celsius: {resultado_c} °C")
                print(f"{cantidad} °F a Kelvin: {resultado_k} K\n")
                historial_temperatura.agregar_registro(
                    f"{cantidad} °F", f"{resultado_c} °C, {resultado_k} K"
                )
            elif sub_opcion == '3':
                resultado_c = kelvin.kelvin_a_celsius(cantidad)
                resultado_f = kelvin.kelvin_a_fahrenheit(cantidad)
                print(f"\n{cantidad} K a Celsius: {resultado_c} °C")
                print(f"{cantidad} K a Fahrenheit: {resultado_f} °F\n")
                historial_temperatura.agregar_registro(
                    f"{cantidad} K", f"{resultado_c} °C, {resultado_f} °F"
                )
            else:
                print("\nOpción no válida.\n")

        elif opcion == '2':
            mostrar_encabezado("Conversión de Longitud")
            print("\n1. Metros a Kilómetros, Pies o Millas")
            print("2. Kilómetros a Metros, Pies o Millas")
            print("3. Pies a Metros, Kilómetros o Millas")
            print("4. Millas a Metros, Kilómetros o Pies\n")
            sub_opcion = input("Elige una opción (1, 2, 3 o 4): ")
            cantidad = float(input("\nIntroduce la cantidad: "))

            if sub_opcion == '1':
                resultado_km = metros.metros_a_kilometros(cantidad)
                resultado_ft = metros.metros_a_pies(cantidad)
                resultado_mi = metros.metros_a_millas(cantidad)
                print(f"\n{cantidad} m a Kilómetros: {resultado_km} km")
                print(f"{cantidad} m a Pies: {resultado_ft} ft")
                print(f"{cantidad} m a Millas: {resultado_mi} mi\n")
                historial_longitud.agregar_registro(
                    f"{cantidad} m", f"{resultado_km} km, {resultado_ft} ft, {resultado_mi} mi"
                )
            elif sub_opcion == '2':
                resultado_m = kilometros.kilometros_a_metros(cantidad)
                resultado_ft = kilometros.kilometros_a_pies(cantidad)
                resultado_mi = kilometros.kilometros_a_millas(cantidad)
                print(f"\n{cantidad} km a Metros: {resultado_m} m")
                print(f"{cantidad} km a Pies: {resultado_ft} ft")
                print(f"{cantidad} km a Millas: {resultado_mi} mi\n")
                historial_longitud.agregar_registro(
                    f"{cantidad} km", f"{resultado_m} m, {resultado_ft} ft, {resultado_mi} mi"
                )
            elif sub_opcion == '3':
                resultado_m = pies.pies_a_metros(cantidad)
                resultado_km = pies.pies_a_kilometros(cantidad)
                resultado_mi = pies.pies_a_millas(cantidad)
                print(f"\n{cantidad} ft a Metros: {resultado_m} m")
                print(f"{cantidad} ft a Kilómetros: {resultado_km} km")
                print(f"{cantidad} ft a Millas: {resultado_mi} mi\n")
                historial_longitud.agregar_registro(
                    f"{cantidad} ft", f"{resultado_m} m, {resultado_km} km, {resultado_mi} mi"
                )
            elif sub_opcion == '4':
                resultado_m = millas.millas_a_metros(cantidad)
                resultado_km = millas.millas_a_kilometros(cantidad)
                resultado_ft = millas.millas_a_pies(cantidad)
                print(f"\n{cantidad} mi a Metros: {resultado_m} m")
                print(f"{cantidad} mi a Kilómetros: {resultado_km} km")
                print(f"{cantidad} mi a Pies: {resultado_ft} ft\n")
                historial_longitud.agregar_registro(
                    f"{cantidad} mi", f"{resultado_m} m, {resultado_km} km, {resultado_ft} ft"
                )
            else:
                print("\nOpción no válida.\n")

        elif opcion == '3':
            ver_historial()
        elif opcion == '4':
            exportar_historial()
        elif opcion == '5':
            print("\nGracias por usar el conversor.\n")
            break
        else:
            print("\nOpción no válida.\n")

main()
