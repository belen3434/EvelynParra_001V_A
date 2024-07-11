
import csv
import random

def asignar_sueldos_aleatorios(trabajadores):
    sueldos_asignados_trabajadores = {}
    for trabajador in trabajadores:
        credito = random.randint(300000,2500000)
        sueldos_asignados_trabajadores[trabajador] = credito
    return sueldos_asignados_trabajadores


def clasificar_sueldos(sueldos_trabajadores):
    menores_800 = {}
    entre800_2000000 = {}
    superior_2000000 = {}
    acumuladorSueldo = 0

    for trabajador, sueldo in sueldos_trabajadores.items():
        acumuladorSueldo = acumuladorSueldo + sueldo
        if sueldo <800:
            menores_800[trabajador] = sueldo
        elif sueldo <= 2000000:
            entre800_2000000[trabajador] = sueldo
        else:
            superior_2000000[trabajador] = sueldo

    print("EL TOTAL DE LOS SUELDOS MENORES A $800.000 ES DE: ",len(menores_800))
    for trabajador, sueldo in menores_800.items():
        print(trabajador," :$",sueldo)

    print("EL TOTAL DE LOS SUELDOS ENTRE $800000 Y $2.000.000 ES DE: ",len(entre800_2000000))
    for trabajador, sueldo in entre800_2000000.items():
        print(trabajador,": $",sueldo)

    print("EL TOTAL DE LOS SUELDOS SUPERIORES A $2.000.000 ES DE: ",len(superior_2000000))
    for trabajador, sueldo in superior_2000000.items():
        print(trabajador," : $",sueldo)

    print("EL TOTAL DE SUELDOS ES DE: $",acumuladorSueldo)

def ver_estadisticas(sueldos_trabajadores):
    lista_estadisticas = list(sueldos_trabajadores.values())

    sueldoMasAlto = max(lista_estadisticas)
    sueldoMasBajo = min(lista_estadisticas)
    promedioSueldos = sum(lista_estadisticas)/len(lista_estadisticas)

    return {"sueldoAlto": sueldoMasAlto, "sueldoBajo": sueldoMasBajo, "promedioSueldos": promedioSueldos}


def reporte_sueldos(sueldos_trabajadores):

    detalleDeSueldos = []

    for trabajador, sueldo in sueldos_trabajadores.items():
        descuentoSalud = sueldo*0.7
        descuentoAfp = sueldo*0.12
        sueldoLiquido = sueldo - descuentoSalud - descuentoAfp

        trabajador = {
            "Nombre Empleado" : trabajador,
            "Sueldo Base" : sueldo,
            "Descuento Salud" : descuentoSalud,
            "DescuentoAfp" : descuentoAfp,
            "SueldoLiquido" : sueldoLiquido

        }

        detalleDeSueldos.append(trabajador)




    with open("reporte_sueldos.csv","w",newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["Nombre Empleado","Sueldo Base","Descuento Salud","DescuentoAfp","SueldoLiquido"])

        for trabajador in detalleDeSueldos:
            escritor.writerow([trabajador["Nombre Empleado"],trabajador["Sueldo Base"],trabajador["Descuento Salud"],trabajador["DescuentoAfp"],trabajador["SueldoLiquido"]])
            

    print("archivo guardado correctamente")


