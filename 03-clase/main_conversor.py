from conversor_temperatura import celsius, fahrenheit, kelvin
from conversor_longitud import metros, kilometros, pies, millas

def mostrar_encabezado(titulo):
    print("\n" + "-" * 40)
    print(f"{titulo}".center(40))
    print("-" * 40)

def main():
    mostrar_encabezado("Bienvenido al Conversor de Unidades")
    print("¿Qué te gustaría convertir?")
    print("1. Temperatura")
    print("2. Longitud")
    print("-" * 40)
    opcion = input("Elige una opción (1 o 2): ")

    if opcion == '1':
        mostrar_encabezado("Conversión de Temperatura")
        print("1. Celsius a Fahrenheit o Kelvin")
        print("2. Fahrenheit a Celsius o Kelvin")
        print("3. Kelvin a Celsius o Fahrenheit")
        print("-" * 40)
        sub_opcion = input("Elige una opción (1, 2 o 3): ")
        cantidad = float(input("Introduce la cantidad: "))

        if sub_opcion == '1':
            mostrar_encabezado("Resultado de Conversión")
            print(f"{cantidad} °C a Fahrenheit: {celsius.celsius_a_fahrenheit(cantidad)} °F")
            print(f"{cantidad} °C a Kelvin: {celsius.celsius_a_kelvin(cantidad)} K")
        elif sub_opcion == '2':
            mostrar_encabezado("Resultado de Conversión")
            print(f"{cantidad} °F a Celsius: {fahrenheit.fahrenheit_a_celsius(cantidad)} °C")
            print(f"{cantidad} °F a Kelvin: {fahrenheit.fahrenheit_a_kelvin(cantidad)} K")
        elif sub_opcion == '3':
            mostrar_encabezado("Resultado de Conversión")
            print(f"{cantidad} K a Celsius: {kelvin.kelvin_a_celsius(cantidad)} °C")
            print(f"{cantidad} K a Fahrenheit: {kelvin.kelvin_a_fahrenheit(cantidad)} °F")
        else:
            print("Opción no válida.")
        print("-" * 40)

    elif opcion == '2':
        mostrar_encabezado("Conversión de Longitud")
        print("1. Metros a Kilómetros, Pies o Millas")
        print("2. Kilómetros a Metros, Pies o Millas")
        print("3. Pies a Metros, Kilómetros o Millas")
        print("4. Millas a Metros, Kilómetros o Pies")
        print("-" * 40)
        sub_opcion = input("Elige una opción (1, 2, 3 o 4): ")
        cantidad = float(input("Introduce la cantidad: "))

        if sub_opcion == '1':
            mostrar_encabezado("Resultado de Conversión")
            print(f"{cantidad} m a Kilómetros: {metros.metros_a_kilometros(cantidad)} km")
            print(f"{cantidad} m a Pies: {metros.metros_a_pies(cantidad)} ft")
            print(f"{cantidad} m a Millas: {metros.metros_a_millas(cantidad)} mi")
        elif sub_opcion == '2':
            mostrar_encabezado("Resultado de Conversión")
            print(f"{cantidad} km a Metros: {kilometros.kilometros_a_metros(cantidad)} m")
            print(f"{cantidad} km a Pies: {kilometros.kilometros_a_pies(cantidad)} ft")
            print(f"{cantidad} km a Millas: {kilometros.kilometros_a_millas(cantidad)} mi")
        elif sub_opcion == '3':
            mostrar_encabezado("Resultado de Conversión")
            print(f"{cantidad} ft a Metros: {pies.pies_a_metros(cantidad)} m")
            print(f"{cantidad} ft a Kilómetros: {pies.pies_a_kilometros(cantidad)} km")
            print(f"{cantidad} ft a Millas: {pies.pies_a_millas(cantidad)} mi")
        elif sub_opcion == '4':
            mostrar_encabezado("Resultado de Conversión")
            print(f"{cantidad} mi a Metros: {millas.millas_a_metros(cantidad)} m")
            print(f"{cantidad} mi a Kilómetros: {millas.millas_a_kilometros(cantidad)} km")
            print(f"{cantidad} mi a Pies: {millas.millas_a_pies(cantidad)} ft")
        else:
            print("Opción no válida.")
        print("-" * 40)

    else:
        print("Opción no válida.")
        print("-" * 40)

if __name__ == "__main__":
    main()
