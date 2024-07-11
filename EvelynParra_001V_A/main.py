import funciones as fn

trabajadores = ["Juan Perez","Maria Garcia","Carlos Lopez","Ana Martinez","Pedro Rodriguez","Laura Hernandez","Miguel Sanchez","Isabel Gomez","Francisco Diaz","Elena Fernandez"]

sueldos_trabajadores = {trabajador : 0 for trabajador in trabajadores}

while True:
    try:
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")

        opcionMenu = int(input("INGRESE OPCION: "))

        if opcionMenu == 1:
            sueldos_trabajadores = fn.asignar_sueldos_aleatorios(trabajadores)
            print("Sueldos asignados correctamente")

            
        elif opcionMenu == 2:
            fn.clasificar_sueldos(sueldos_trabajadores)

        elif opcionMenu == 3:
            estadisticas = fn.ver_estadisticas(sueldos_trabajadores)
            print("")
            print("Sueldo mas alto", estadisticas["sueldoAlto"])
            print("Sueldo mas bajo", estadisticas["sueldoBajo"])
            print("Promedio Sueldo", estadisticas["promedioSueldos"])
            print("")


        elif opcionMenu == 4:
            fn.reporte_sueldos(sueldos_trabajadores)

        elif opcionMenu == 5:
            print("FINALIZANDO PROGRAMA")
            print("DESARROLLADO POR EVELYN PARRA")
            print("RUT 17.480.311-0")
            break
        else:
            print("INGRESE OPCION VÁLIDA")
    except ValueError:
        print("INGRESE OPCION NUMÉRICA")