

inicio=0

while inicio <1:  

    print("bienvenido a...",
"""
                                       _      
                                      | |     
 ___ _   _ _ __   ___ _ __    ___ __ _| | ___ 
/ __| | | | '_ \ / _ \ '__|  / __/ _` | |/ __|
\__ \ |_| | |_) |  __/ |    | (_| (_| | | (__ 
|___/\__,_| .__/ \___|_|     \___\__,_|_|\___|
          | |                                 
          |_|                                 

by: RAL
                    comandos:

sumar--- para sumar     multiplicar----para multiplicar

restar--- para restar   dividir----para dividir

potencia----para resolver potencias  exit---para salir


"""
)
    

    operacion = input("ingresar la operacion a realizar ")
    
   

    while operacion ==''or operacion ==' ':
        print('hubo un error vuelva a intertar')
        operacion=input('ingresar la operaracin a realizar ')
    if operacion == 'exit':
        inicio+= 1
    
    if operacion == "sumar":
       print("""
  _____                            
 / ____|                           
| (___  _   _ _ __ ___   __ _ _ __ 
 \___ \| | | | '_ ` _ \ / _` | '__|
 ____) | |_| | | | | | | (_| | |   
|_____/ \__,_|_| |_| |_|\__,_|_|   
                                   
    """)
    if operacion== 'sumar':
        numero_1=int(input("ingresar el primer numero a sumar "))
        numero_2=int(input("ingresar el segundo numero a sumar "))
        resultado=numero_1+numero_2    
    
        print("su resultado es ", resultado)
        salir=input('volver a realizar otra operacion: si,no ')
        if salir == 'no':
            inicio+=1  

    if operacion == "restar":
        print("""
 _____           _             
|  __ \         | |            
| |__) |___  ___| |_ __ _ _ __ 
|  _  // _ \/ __| __/ _` | '__|
| | \ \  __/\__ \ || (_| | |   
|_|  \_\___||___/\__\__,_|_|   
                                                  
    """)
        numero_1=int(input("ingresar el primer numero a restar "))
        numero_2=int(input("ingresar el segundo numero a restar "))
        resultado=numero_1-numero_2
        print("su resultado es ", resultado)
        salir=input('volver a realizar otra operacion: si,no ')
        if salir == 'no':
            inicio+=1  

    if operacion == "multiplicar":
        print(""" 
                 _ _   _       _ _                
                | | | (_)     | (_)               
 _ __ ___  _   _| | |_ _ _ __ | |_  ___ __ _ _ __ 
| '_ ` _ \| | | | | __| | '_ \| | |/ __/ _` | '__|
| | | | | | |_| | | |_| | |_) | | | (_| (_| | |   
|_| |_| |_|\__,_|_|\__|_| .__/|_|_|\___\__,_|_|   
                        | |                       
                        |_|
    """)
        numero_1=int(input("ingresar el primer numero a multiplicar "))
        numero_2=int(input("ingresar el segundo numero a multiplicar "))
        resultado=numero_1*numero_2            
        print("su resultado es ", resultado)
        salir=input('volver a realizar otra operacion: si,no ')
        if salir == 'no':
            inicio+=1  


    if operacion == "dividir" :
        print("""
     _ _       _     _ _      
    | (_)     (_)   | (_)     
  __| |___   ___  __| |_ _ __ 
 / _` | \ \ / / |/ _` | | '__|
| (_| | |\ V /| | (_| | | |   
 \__,_|_| \_/ |_|\__,_|_|_|  
                                                  
    """)
        numero_1=int(input("ingresar el primer numero a dividir "))
        numero_2=int(input("ingresar el segundo numero a dividir "))
        resultado=numero_1/numero_2
        print("su resultado es ", resultado)
        salir=input('volver a realizar otra operacion: si,no ')
        if salir == 'no':
            inicio+=1  


    if operacion == "potencia":
        print("""
 _____      _                  _       
|  __ \    | |                (_)      
| |__) |__ | |_ ___ _ __   ___ _  __ _ 
|  ___/ _ \| __/ _ \ '_ \ / __| |/ _` |
| |  | (_) | ||  __/ | | | (__| | (_| |
|_|   \___/ \__\___|_| |_|\___|_|\__,_|
                                                       
    """)
        numero_1=int(input("ingresar la base de la potencia "))
        numero_2=int(input("ingresar el exponente de la potencia "))
        resultado=numero_1**numero_2
        print("su resultado es ", resultado)
        salir=input('volver a realizar otra operacion: si,no ')
        if salir == 'no':
            inicio+=1  

            
