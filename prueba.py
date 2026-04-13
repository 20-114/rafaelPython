# creando variables
titulo = "Clima de hoy" #string
diaDelMes = 13 #int
mes = 4 #int
temperatura = 22.3 #float
llueve = False #boolean

print(titulo)
print("Temperatura actual ", temperatura, " grados")
print(diaDelMes, "-", mes)

if llueve: #las variables booleanas por si mismas se responden 
    print("Tiene que llevar paraguas")
else:
    print("Puede llevar polera sin mangas")