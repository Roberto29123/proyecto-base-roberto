import math

class Operaciones:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.resultado = 0
        
    def leerNumeros(self):
        while True:
            try:
                self.num1 = int(input("Número 1:"))
                break
            except Exception:
                print("Número inválido")
                continue
        while True:
            try:
                self.num2 = int(input("Número 2:"))
                break
            except Exception:
                print("Número inválido")
                continue   

    def mayorque(self):
        if(self.num1 > self.num2):
            self.resultado = "El numero " + str(self.num1) + "es mayor que " + str(self.num2)

        else:
            self.resultado = "El numero " + str(self.num2) + "es mayor que " + str(self.num1)
            print('hola')
    
    def potencia(self):
        self.resultado = "La potencia de " + str(self.num1) + " elevado a la " + str(self.num2) + " es igual a " + str(self.num1**self.num2)
    
    def mostrarResultado(self):
        print(self.resultado)