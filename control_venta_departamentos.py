# Autor: einzelentwickler (GitHub: einzelentwickler)

import datetime

pisos = 10
departamentos_por_piso = 4
tipos_departamento = ['A', 'B', 'C', 'D']
precios = {'A': 3800, 'B': 3000, 'C': 2800, 'D': 3500}
departamentos_disponibles = [[True] * departamentos_por_piso for _ in range(pisos)]
compradores = {}


def mostrar_menu():
    print("==== Menú ====")
    print("1. Comprar departamento")
    print("2. Mostrar departamentos disponibles")
    print("3. Ver listado de compradores")
    print("4. Mostrar ganancias totales")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion


def comprar_departamento():
    print("=== Comprar departamento ===")
    piso = int(input("Ingrese el número de piso (1-{}): ".format(pisos)))
    tipo_departamento = input("Ingrese el tipo de departamento (A, B, C, D): ")
    departamento = "{}{}".format(tipo_departamento, piso)

    if not (1 <= piso <= pisos) or tipo_departamento not in tipos_departamento:
        print("Error: Opción inválida")
        return

    fila = piso - 1
    columna = tipos_departamento.index(tipo_departamento)

    if not departamentos_disponibles[fila][columna]:
        print("El departamento no está disponible")
        return

    run = input("Ingrese el RUN del comprador (sin puntos ni guion): ")
    if run in compradores:
        print("Error: El RUN ya ha sido registrado")
        return

    compradores[run] = departamento
    departamentos_disponibles[fila][columna] = False
    print("Operación realizada correctamente")


def mostrar_departamentos_disponibles():
    print("=== Departamentos disponibles ===")
    for piso, fila in enumerate(departamentos_disponibles, start=1):
        print("Piso", piso)
        for tipo, disponible in zip(tipos_departamento, fila):
            if disponible:
                print("{}{}".format(tipo, piso))
            else:
                print("{}{}".format(tipo, piso), "X")
        print()


def mostrar_listado_compradores():
    print("=== Listado de compradores ===")
    for run, departamento in sorted(compradores.items(), key=lambda x: x[0]):
        print("RUN: {}, Departamento: {}".format(run, departamento))


def mostrar_ganancias_totales():
    print("=== Ganancias totales ===")
    total_por_tipo = {tipo: 0 for tipo in tipos_departamento}
    total_general = 0

    for run, departamento in compradores.items():
        tipo = departamento[0]
        total_por_tipo[tipo] += precios[tipo]
        total_general += precios[tipo]

    for tipo, total in total_por_tipo.items():
        cantidad = total // precios[tipo]
        print("Tipo {}: {} UF, {} unidades".format(tipo, total, cantidad))

    print("TOTAL: {} UF".format(total_general))


def obtener_fecha_actual():
    fecha_actual = datetime.date.today()
    return fecha_actual.strftime("%d/%m/%Y")


def salir():
    fecha_actual = obtener_fecha_actual()
    print("Saliendo del sistema -", fecha_actual)
    exit()


def main():
    while True:
        opcion = mostrar_menu()

        if opcion == '1':
            comprar_departamento()
        elif opcion == '2':
            mostrar_departamentos_disponibles()
        elif opcion == '3':
            mostrar_listado_compradores()
        elif opcion == '4':
            mostrar_ganancias_totales()
        elif opcion == '5':
            salir()
        else:
            print("Error: Opción inválida")


if __name__ == "__main__":
    main()
