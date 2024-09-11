#Damos las instrucciones para ingresar los datos
print("Ingresa los datos en formato numerico")

#Declaramos variables
dia=int(input("Ingresa tu dia de nacimiento: "))
mes=int(input("Ingresa tu mes: "))

#Se realiza la logica del programa
if(mes==3 and dia>=21 or mes==4 and dia<=19):
    signo="Tu eres Aries"
elif(mes==4 and dia>=20 or mes==5 and dia<=20):
    signo="Tu eres Tauro"
elif(mes==5 and dia>=21 or mes==6 and dia<=20):
    signo="Tu eres Geminis"
elif(mes==6 and dia>=21 or mes==7 and dia<=22):
    signo="Tu eres Cancer"
elif(mes==7 and dia>=23 or mes==8 and dia<=22):
    signo="Tu eres Leo"
elif(mes==8 and dia>=23 or mes==9 and dia<=22):
    signo="Tu eres Virgo"
elif(mes==9 and dia>=23 or mes==10 and dia<=22):
    signo="Tu eres Libra"
elif(mes==10 and dia>=23 or mes==11 and dia<=21):
    signo="Tu eres Escorpio"
elif(mes==11 and dia>=22 or mes==12 and dia<=21):
    signo="Tu eres Sagitario"
elif(mes==12 and dia>=22 or mes==1 and dia<=19):
    signo="Tu eres Capricornio"
elif(mes==1 and dia>=20 or mes==2 and dia<=18):
    signo="Tu eres Acuario"
elif(mes==2 and dia>=19 or mes==3 and dia<=20):
    signo="Tu eres Sagitario"

#Se muestra el signo
print(signo)