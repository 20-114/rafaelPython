# # creando variables
# titulo = "Clima de hoy" #string
# diaDelMes = 13 #int
# mes = 4 #int
# temperatura = 22.3 #float
# llueve = False #boolean

# print(titulo)
# print("Temperatura actual ", temperatura, " grados")
# print(diaDelMes, "-", mes)

# if llueve: #las variables booleanas por si mismas se responden 
#     print("Tiene que llevar paraguas")
# else:
#     print("Puede llevar polera sin mangas")


#pedir password y pin
#pida la usuario password en palabras que deben ser "TEMU"TEMU
#ademas pida el pinn que debe ser 3435
#los dos deben estar correctos para acceder el sistema


# log = "temu"
# passw = 3435

# print("Para entrar a su cuenta ingrese")
# login = input("Ususario ")
# pin = int(input("Clave "))

# if login == log and pin == passw:
#     print("Ingresando al sistema...")
# else:
#     print("Error en ingreso de datos")
    

tramo1_desde = 500000
tramo1_hasta = 1000000
tramo1_credito = 300000

tramo2_desde = 1000000
tramo2_hasta = 1500000
tramo2_credito = 650000

tramo3_desde = 1500000
tramo3_hasta = 100000000000
tramo3_credito = 650000

credito = 0
#Nivel educacional
basico = 1
medio = 1.3
superior = 1.5

credito_nacionalidad = 300000

print("Ingrese los datos solicitados a continuación")
ingresos = int(input("Ingresos mensuales: "))
educacion = (input("Nivel educacional (básico, medio o superiror): "))
nacionalidad = (input("Nacionalidad: "))

if ingresos >= tramo1_desde and ingresos < tramo1_hasta:
    credito = credito + tramo1_credito
elif ingresos >= tramo2_desde and ingresos < tramo2_hasta:
    credito = credito + tramo2_credito
elif ingresos >= tramo3_desde and ingresos < tramo3_hasta:
    credito = credito + tramo3_credito
else:
    print("")

if ingresos >= tramo1_desde:
    if educacion == "basico":
        credito = credito * basico
    elif educacion == "medio":
        credito = credito * medio
    elif educacion == "superior":
        credito = credito * superior
    else:
        print("Error de ingreso en nivel educacional")

    if nacionalidad == "chilena" or nacionalidad == "chileno":
        credito = credito + credito_nacionalidad
    else:
        print("Error de ingreso en nacionalidad")

    print("Puede acceder a un crédito de ", credito, " pesos.")

else:
    print("Ingresos induficientes para acceder a un credito")









