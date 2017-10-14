import sys
import time
from bigo import Fibonacci
class MenuMain:
    """Menu principal de metodos de Notacion Big O"""
    def __init__(self):
        self.fibo = Fibonacci()
        self.opciones = {
            "1" : self.fibonacci_recur,
            "2" : self.fibonacci_optimo,
            "3" : self.fibonacci_matriz,
            "4" : self.quit
            }

    def mostrar_menu(self):
        print("""
Menu Notacion Big O

1 Fibonacci con Recursividad
2 Fibonacci con For
3 Fibonacci con Cache
4 Salir
""")

    def run(self):
        """Muestra el menu"""
        while True:
            self.mostrar_menu()
            opcion = input("Escriba el número de opción: ")
            accion = self.opciones.get(opcion)
            if(accion):
                accion()
            else:
                print("{0} no es una opción válida.".format(opcion))

    def fibonacci_recur(self, fibo=None):
        if not fibo:
            fibo = Fibonacci()
        numeroTest = int(input("Ingrese el numero para la secuencia: "))
        start_time = time.time()
        print(">> "+str(fibo.fibonaccirecur(numeroTest)))
        elapsed_time = time.time() - start_time
        print(">> Tiempo trasncurrido: "+time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))

    def fibonacci_optimo(self, fibo=None):
        if not fibo:
            fibo = Fibonacci()
        numeroTest = int(input("Ingrese el numero para la secuencia: "))
        start_time = time.time()
        print(">>"+fibo.fibonaccifor(numeroTest))
        elapsed_time = time.time() - start_time
        print(">> Tiempo trasncurrido: "+time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))

    def fibonacci_matriz(self, fibo=None):
        if not fibo:
            fibo = Fibonacci()
        numeroTest = int(input("Ingrese el numero para la secuencia: "))
        start_time = time.time()
        print(">> "+str(fibo.fibonacciarreglo(numeroTest)))
        elapsed_time = time.time() - start_time
        print(">> Tiempo trasncurrido: "+time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))


    def quit(self):
        print("Finaliza Laboratorio 1")
        sys.exit(0)

if __name__ == "__main__":
    MenuMain().run()
              
