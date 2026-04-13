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


log = "temu"
passw = 3435

print("Para entrar a su cuenta ingrese")
login = input("Ususario ")
pin = int(input("Clave "))

if login == log and pin == passw:
    print("Ingresando al sistema...")
else:
    print("Error en ingreso de datos")
    

